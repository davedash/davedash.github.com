---
wordpress_id: 227
layout: post
title: Resizing Image on upload in Django
wordpress_url: http://spindrop.us/?p=227
site: spindrop
tags: [spindrop, snippet, uploads, django, pil]
---
I had trouble wrapping my head around Django ORM's handling of Images.

The first hurdle was realizing that [there is no easy way to store images in the database](/2009/02/18/database-versus-files-for-images/).  I couldn't be too upset with that, it was a flawed concept at best.  I wrote a dump script to fix this, and converted my app to read from disk.  One of those "good" problems.

When it came to uploading new content... I seemed to hit every roadblock.  So I thought this guide might be of use for people (other than future-me).  What I want to do is upload an image, resize it per the requirements of my app, and save the resized image.

<!--more-->
### The Template

The template was fairly easy, yet I forgot to specify the `enctype` attribute.  Here's what you need:

<div><textarea name="code" class="html">

<h2>Upload a new photo</h2>

<form action="" method="POST" class="cmxform" enctype="multipart/form-data">
  <fieldset>
    <ul>
      <li>
        {% if form.image.errors %}
        <ul class="errorlist">
        {% for error in form.image.errors %}
            <li>{{ error|safe }}</li>
        {% endfor %}
        </ul>
        {% endif %}
        <label for="id_image">Photo</label>
        {{ form.image }}
      </li>
    
    </ul>
  </fieldset>
  <input type="submit" value="Submit" class="submit"/>
</form>

</textarea></div>

### Resizing an image

Resizing an image was straightforward.  The Python Imaging Library is very easy to work with, and very similar to the PHP GD Library.  There was one caveat...

<div><textarea name="code" class="python">

def handle_uploaded_image(i):
    # resize image
    imagefile  = StringIO.StringIO(i.read())
    imageImage = Image.open(imagefile)

    (width, height) = imageImage.size
    (width, height) = scale_dimensions(width, height, longest_side=240)

    resizedImage = imageImage.resize((width, height))

    imagefile = StringIO.StringIO()
    resizedImage.save(imagefile,'JPEG')
	# ...
</textarea></div>

I'm using OS X and didn't have libjpeg installed.  The recommended way was to install it via fink.

### Generating a filename

I like using MD5 to generate filenames for images because MD5 almost guarantees uniqueness ("unique enough").

<div><textarea name="code" class="python">
	...
    filename = hashlib.md5(imagefile.getvalue()).hexdigest()+'.jpg'
	...
</textarea></div>

### Saving the file via the model

The model is supposed to put the files in the right spot and populate the meta data.

You can supposedly do this via:

<div><textarea name="code" class="python">
	...
    my_object = MyDjangoObject()
    my_object.photo.save(filename, content)
	...
</textarea></div>

That will also take care of `my_object.save()`.  The trick is that content needs to be a `django.core.files.File` object or things will never work.  Further more, you can't use a StringIO for your `File` object.  A true file object is best.  Hence rewriting the `JPEG`:

<div><textarea name="code" class="python">
    imagefile = open(os.path.join('/tmp',filename), 'w')
    resizedImage.save(imagefile,'JPEG')
    imagefile = open(os.path.join('/tmp',filename), 'r')
    content = django.core.files.File(imagefile)
</textarea></div>

Note: I also had to reopen the imagefile.

### All together now

<div><textarea name="code" class="python">
@login_required
def my_view(request, slug, item_slug):
    
    if request.method == 'POST':
        form = NewImageForm(request.POST, request.FILES)

        if form.is_valid():
            handle_uploaded_image(request.FILES['image'])
            return HttpResponseRedirect(elsewhere)
    else:
        form       = NewImageForm()
        
    return render_to_response(somewhere, locals(), context_instance=RequestContext(request))

def handle_uploaded_image(i):
    # resize image
    imagefile  = StringIO.StringIO(i.read())
    imageImage = Image.open(imagefile)

    (width, height) = imageImage.size
    (width, height) = scale_dimensions(width, height, longest_side=240)

    resizedImage = imageImage.resize((width, height))

    imagefile = StringIO.StringIO()
    resizedImage.save(imagefile,'JPEG')
    filename = hashlib.md5(imagefile.getvalue()).hexdigest()+'.jpg'
        
    # #save to disk
    imagefile = open(os.path.join('/tmp',filename), 'w')
    resizedImage.save(imagefile,'JPEG')
    imagefile = open(os.path.join('/tmp',filename), 'r')
    content = django.core.files.File(imagefile)

    my_object = MyDjangoObject()
    my_object.photo.save(filename, content)

</textarea></div>

I'm sure there's room to optimize this flow.  But this gets the job done.  I do wish I could have used a StringIO instead of an actual file to save the image.  Writing to disk twice seems silly.
