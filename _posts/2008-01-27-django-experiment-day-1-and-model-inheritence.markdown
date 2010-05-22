---
wordpress_id: 142
layout: post
title: "django experiment: Day 1 and Model Inheritence"
wordpress_url: http://spindrop.us/2008/01/27/django-experiment-day-1-and-model-inheritence/
site: spindrop
tags: [programming, inheritance, django]
---
[tags]django, inheritance[/tags]

I spent a few hours diving into Django.  I knew enough python to get around, and also to be dangerous.

Here's a summary of what I've learned.

<!--more-->


### Model Inheritence
So far I've learned that [ModelInheritence is not quite ready](http://code.djangoproject.com/wiki/ModelInheritance). In other words, you can't define in your `models.py` something like this:

<div><textarea name="code" class="python">
from django.db import models

class ContentZone(models.Model):
  slug     = models.SlugField()
  content  = models.TextField()
  notes    = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')
  def __unicode__(self):
    return self.slug

class Page(ContentZone):
  title    = models.CharField(max_length=200)
  def __unicode__(self):
    return self.title
</textarea></div>

The model itself will work, and it will save, but things like `Page.objects.all()` will return empty lists.

### Where I'm still shaky

I...
* still have to learn how to create templates.
* want better understanding of the available field types.
* want to find a good CMS plugin
* want to know if there's the idea of environments in Django (like in symfony)
* want to override `.save()` on my models
* want to learn how to have self-referencing models (E.g. a hierarchical category)

I'm going to keep on plugging along, it's really easy to figure out django.
