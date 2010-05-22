---
wordpress_id: 145
layout: post
title: "django experiment: day 2 templates, and that's it?"
wordpress_url: http://spindrop.us/2008/01/28/django-experiment-day-2-templates-and-thats-it/
site: spindrop
tags: [spindrop, symfony, django]
---
[tags]django, symfony[/tags]

[**Note**: This really does have something to do with symfony.]

So I finished the tutorials on Django, but the Django tutorial is nothing compared to the Askeet Advent Calendar.  Askeet was 24 one hour tutorials that go in depth to each nook and cranny of [symfony][], whereas I still feel like there's got to be more to Django.

I get Templating now, and I really like the flexibility offered in Django.  The one major difference is the layout structure.

[symfony][] has this nice structure of defining a general layout, and then all following templates automatically inherit from the default layout (unless otherwise specified).  Django on the other hand requires you to explicitly extend other layouts and define regions within those layouts.

* I like the symfony style because I inherit almost always from the general template.
* The Django style however offers the flexibility of having subsections (which inherit from the base style) which you can inherit from.  E.g. you may have a site which has 1. a blog and 2. a gallery.  Both the blog and gallery sections share common elements from a main template, but all the pages within blog all have some unique bloggish features that the gallery lacks.

I've got a lot more to learn with Django, but I am enjoying it so far.  

I...

* <del>still have to learn how to create templates.</del>
* <del>want better understanding of the available field types.</del>
* want to find a good CMS package
* want to know if there's the idea of environments in Django (like in symfony)
* want to override .save() on my models
* want to learn how to have self-referencing models (E.g. a hierarchical category)


[symfony]: http://symfony-project.com/
