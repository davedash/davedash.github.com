---
wordpress_id: 342
layout: post
title: "django-fixture-magic: Testing issues with real data."
wordpress_url: http://spindrop.us/?p=342
site: spindrop
tags: [spindrop, django, mozilla, addons.mozilla.org, testing, fixtures]
---
[f]: http://github.com/davedash/django-fixture-magic
[amo]: http://addons.mozilla.org/
[django]: http://djangoproject.com/

I just released [Fixture Magic][f].

When dealing with legacy data, you'll run into all kinds of edge cases.  Perhaps, an object might not display correctly unless it has the right parameters, or if it has null parameters it might not display at all.  So when testing [Django][], it's nice to actually use non-dummy data.  

Luckily Django has a way of pulling real data out of your database using `django.core.serializers`:


	from addons.models import Addon
	a = Addon.objects.get(id=3615)
	from django.core.serializers import serialize
	jsonize = lambda a: serialize("json", a, indent=4)
	jsonize([a])

This solution runs well in a Django shell and can be lots of fun for the whole family... until things get complicated.
<!--more-->
### Serializing alone isn't enough.

Serializing a fixture with foreign keys means you'll have an un-loadable fixture unless you serialize the dependent fixtures.  Even for one or two foreign keys, this can be a pain.  For [addons.mozilla.org][amo], we have a spidery-web of dependencies: `File`s need a `Version` which needs an `Addon` which need `Translation`s.

Thus begat the `dump_object` management command.  Give it an app, model name and a `pk` and it will give you not only a serialized JSON of that object, but all the objects that it requires.

Example:

	./manage.py dump_object files.file 64874 64876 > my_new_fixture.json

This looks for the `File` model in the `files` app and pulls out of the database `File`s instances with `pk`s of `64874` and `64876`.  It then recursively searches for any required objects.

### Too much serial

If you create a lot of fixtures, you'll eventually have overlapping serialized objects.  In `addons.mozilla.org` we have `Addon`s, `Version`s (which depend on `Addon`s) and `AddonCategory`s (which depend on `Addon`s and `Category`s).  If we wanted to get serialize a specific `Addon`, it's dependent `Version`s and `AddonCategory`s it makes sense to start with `dump_object`ing the related `Version` and then `dump_objecting` the `AddonCategory`.  Both `dump_object` commands will fetch the `Addon` in question, resulting in duplicated data.

To combat this we can use `merge_fixtures` to dedupe our fixtures:

	./manage.py dump_object versions.version 64874 > 1.json
	./manage.py dump_object categories.addoncategory > 2.json
	./manage.py merge_json 1.json 2.json > happy_fixture.json

This should make creating test data slightly less painful.  So [give it a try][f].
