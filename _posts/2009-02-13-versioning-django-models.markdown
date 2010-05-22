---
wordpress_id: 215
layout: post
title: Versioning Django Models
wordpress_url: http://spindrop.us/?p=215
site: spindrop
---
In symfony, versioning a model was not terribly difficult.  I had my own specialized brute-force way of doing this.

In my experience it's been a lot easier to write python code than PHP code, so naturally I figured this would be an easy task.  It was not.  I suspect that it was not easy because I have a naive understanding of Django and my symfony knowledge was fairly well grounded.

I tried looking for a generic implementation of django model versioning, but failed.  So I came up with a specific solution.
<!--more-->
### How I think of versions

For my app I chose to use a sparse versioning system.  I'd have one interface for interacting with a model.  For example, I have a `Restaurant` model  and a `RestaurantVersion` model.  

`Restaurant` would directly store immutable elements like `name` or `rating` or `approved` and it would encapsulate versioned elements like `description` by proxying to `RestaurantVersion`.

This means I only need to interface with one class and let the versioning happen behind the scenes.

### The Django implementation of `RestaurantVersion`

`RestaurantVersion` held the data that I thought might suffer from corruption, and therefore require reversion.  Therefore there's nothing surprising in this table:

<div><textarea name="code" class="python">
class RestaurantVersion(models.Model):
    restaurant       = models.ForeignKey('Restaurant', null=True, blank=True)
    user             = models.ForeignKey(Profile, null=True, blank=True)
    description      = models.TextField(blank=True)
    html_description = models.TextField(blank=True)
    url              = models.CharField(max_length=765, blank=True)
    created_at       = models.DateTimeField(auto_now_add=True)
    
    def save(self, force_insert=False, force_update=False):
        self.html_description = markdown(self.description)
        super(RestaurantVersion, self).save(force_insert, force_update)
        
    class Meta:
        db_table = u'restaurant_version'

</textarea></div>

The only thing of note is that I'm enforcing a `1:M` relation between `Restaurant` and `RestaurantVersion`.

### The Django implementation of `Restaurant`

`Restaurant` is where the magic happens.  It needs to do a few things:

1. Do what a normal object does.
2. Proxy attributes to the corresponding attribute of a `RestaurantVersion`
3. Generate a new `RestaurantVersion` on demand.
4. (optional) Manage which version is "active".

I say "4" is optional because I don't do this myself.  I built versioning into a few models because it was easier to do upfront than worry about it down the road.

Here's the code I use:

<div><textarea name="code" class="python">

class Restaurant(models.Model):
    name           = models.CharField(max_length=765, blank=True)
    stripped_title = models.CharField(max_length=384, blank=True)
    approved       = models.IntegerField(null=True, blank=True)
    version        = models.ForeignKey(RestaurantVersion, related_name="the_restaurant")
    updated_at     = models.DateTimeField(auto_now=True)
    created_at     = models.DateTimeField(auto_now_add=True)
    new_version    = None
    
    def save(self, force_insert=False, force_update=False):
        if not self.stripped_title:
            self.stripped_title = slugify(self.name)
        
        super(Restaurant, self).save(force_insert, force_update)
        if self.new_version:
            self.new_version.restaurant = self
            self.new_version.save()
            self.version = self.new_version
            super(Restaurant, self).save(force_insert, force_update)        
        
    def __setattr__(self, name, value):
        if name == 'description':
            self.get_new_version().description = value
        
        elif name == 'url':
            self.get_new_version().url = value
        
        else:
            object.__setattr__(self, name, value)

    def __getattr__(self, name):
        try:
            if name == 'description':
                return self.version.description

            elif name == 'url':
                return self.version.url
        except RestaurantVersion.DoesNotExist:
            return ''
            
        models.Model.__getattribute__(self, name)
    
    def get_new_version(self):
        if self.new_version == None:
            try:
                rv    = self.version
                rv.id = None
            except RestaurantVersion.DoesNotExist:
                rv = RestaurantVersion()
            
            self.new_version = rv

        return self.new_version
            
    class Meta:
        db_table     = u'restaurant'
</textarea></div>

It's not rocket science, but it wasn't necessarily easy either.  Let's look at requirements 2 and 4 in a bit more detail.

#### Proxy attributes to the corresponding `RestaurantVersion` attributes

Proxying attributes is a way of masking the whole versioning infrastructure from the developer.  We do this with `__getattr__` and `__setattr__` methods.

<div><textarea name="code" class="python">
    def __getattr__(self, name):
        try:
            if name == 'description':
                return self.version.description

            elif name == 'url':
                return self.version.url
        except RestaurantVersion.DoesNotExist:
            return ''
            
        models.Model.__getattribute__(self, name)
</textarea></div>

The `__getattr__` determins if you are looking for `description` or `url` attributes of a `Restaurant`.  If you are then it uses the current `RestaurantVersion`'s attribute.

<div><textarea name="code" class="python">
    def __setattr__(self, name, value):
        if name == 'description':
            self.get_new_version().description = value
        
        elif name == 'url':
            self.get_new_version().url = value
        
        else:
            object.__setattr__(self, name, value)
</textarea></div>

`__setattr__` is very similar, except since we're changing a versionable attribute we're going to make a request to a method, `get_new_version()`, which we will detail later.  It does what it says, though, it gets the "new" `RestaurantVersion` of the `Restaurant`.

#### Generate a new `RestaurantVersion` on demand

As you can see from the above code, I am "auto-versioning".  This is done mostly via `get_new_version()`.  We also have to do a few tricks to make sure the bidirectional relationship gets maintained on save.

<div><textarea name="code" class="python">
    def get_new_version(self):
        if self.new_version == None:
            try:
                rv    = self.version
                rv.id = None
            except RestaurantVersion.DoesNotExist:
                rv = RestaurantVersion()
            
            self.new_version = rv

        return self.new_version
</textarea></div>

`get_new_version()` either returns the current "new version", a brand new "new version" or a "copy" of the current version.

The "copy" is done simply by setting the `id` attribute of the new version to `None`.  Django takes care of assigning it a new `id` on save, thus preserving the old version.

Note that when we create a brand new `RestaurantVersion`, we don't immediately set it's `restaurant` attribute.  That's because we haven't saved the current `restaurant` yet.  It's a "chicken and the egg" problem that gets solved in our `save()` method:

<div><textarea name="code" class="python">
    def save(self, force_insert=False, force_update=False):
        if not self.stripped_title:
            self.stripped_title = slugify(self.name)
        
        super(Restaurant, self).save(force_insert, force_update)
        if self.new_version:
            self.new_version.restaurant = self
            self.new_version.save()
            self.version = self.new_version
            super(Restaurant, self).save(force_insert, force_update)
        
</textarea></div>

We first save the `Restaurant`, then we save a new version if there is one.  If we save a new version we want to update the `Restaurant` a second time.  This ensures that there's a `1:1` relationship between `Restaurant` and the current `RestaurantVersion` and it also establishes a `1:M` relationship between `Restaurant` and *all* `RestaurantVersion`s.

### Conclusion and Drawbacks

While, I think that this setup works in my particular situation, I feel like it has some major flaws.

The code is quite messy and very specific to this model.  My goal was to take care of this quickly, not necessarily in a reusable manner.  I also was not familiar enough with the Django model to create some sort of extension.

This way of versioning does not allow for versioned attributes to be set upon instantiation of the model:

	r=Restaurant(description="Great place") 

won't work.  You'll have to do:

	r=Restaurant()
	r.description="Great place"

I figured this was acceptable.

Lastly I'm not entirely happy with having to explicitly save the `Restaurant` model twice, but I think my bidirectional relation requires this.

All in all this works in my particular situation.  I'm hoping that this can be simplified.  I'm curious to hear about other versioning schemes.
