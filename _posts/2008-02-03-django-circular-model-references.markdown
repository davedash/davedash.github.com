---
wordpress_id: 154
layout: post
title: Django circular model references
wordpress_url: http://spindrop.us/2008/02/03/django-circular-model-references/
site: spindrop
tags: [spindrop, django, model, versioning, circular]
---
I'm used to circular references in my model.  Often I do a versioning of an `Item` with an `ItemVersion`.  `Item` will link to the latest `ItemVersion` and `ItemVersion` will link to the relevant `Item`.

Here's how you can define your appropriate [django][] models:

<div><textarea name="code" class="python">
class Item(models.Model):
  id      = models.IntegerField(primary_key=True)
  version = models.ForeignKey('ItemVersion', null=True, blank=True)

class ItemVersion(models.Model):
  id   = models.IntegerField(primary_key=True)
  item = models.ForeignKey(Item, null=True, blank=True)
</textarea></div>

Note in the first model, `Item`, we reference `ItemVersion` in quotes because `ItemVersion` is not yet defined.

[django]: http://djangoproject.com/
