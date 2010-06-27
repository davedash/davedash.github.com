---
layout: post
title: Your objects, and all their friends
tags: [django, fixtures, mozilla, addons.mozilla.org, webdev]
published: true
time: 9:56:AM
---
[fm]: http://pypi.python.org/pypi/django-fixture-magic

This is complicated.

In my ever-evolving quest to [get data out of the AMO database][a] for tests, I
found myself not just extracting a single object, but a list of complicated
requirements in order to fully replicate behavior in production in a testing
environment.

For [AMO][] we can use [fixture magic][fm] to dump a single add-on and all of
it's *database* dependencies so that it will insert safely into a
test-database.  But we need more than just valid data.  We need some supporting
data.  For an add-on to be browsable and searchable it needs to have a valid
version and the version needs to have a valid file.

In our app we can check for these things by using this:

    my_addon.current_version.files.all()[0]

Of course we need to check that `my_addon.current_version` exists and that
`files.all()` has at least one object.  This ends up being a lot of work if you
just know the `id` of the add-on object.

So what I want is something simple, like:

    ./manage.py custom_dump addon 3615

And it should get me everything I need to test add-on 3615, including a Version
object and any files associated with the version.

Turns out this *just works*.  It works if you define the following settings:

{% highlight python %}
## Fixture Magic
CUSTOM_DUMPS = {
    'addon': {  # ./manage.py custom_dump addon id
        'primary': 'addons.addon',  # This is our reference model.
        'dependents': [  # These are items we wish to dump.
            # Magic turns this into current_version.files.all()[0].
            'current_version.files.all.0',
        ],
        'order': ('app1.model1', 'app2.model2',),  # stuff gets sorted
        'excludes': {
            'app1.model1': ('fields', 'to', 'hide',),
        },
    }
}
{% endhighlight %}


Using this we're able to find out that `addon` means an `addons.addon` object
and that you want the `addon` object with an id of `3615`.  From there we'll
try looking for dependent objects.  Using some black magic we can turn:
`current_version.files.all.0` into
`addon.objects.get(pk=3615).current_version.files.all()[0]`.  This gives us a
file.

If we mimic our `dump_object` command we can get the `file` into the database
and everything that the file needs to be valid.  This in turn gives us enough
data (usually) to begin testing a single `addon`.

So have fun with this, if you're database is remotely complicated, this can
save you some time replicating it during testing.

Also note, that you can re-order models and exclude certain fields.  This can
make your fixtures very easy to load.

[a]: /2010/03/05/django-fixture-magic-testing-issues-with-real-data/
[AMO]: https://addons.mozilla.org/en-US/firefox/
