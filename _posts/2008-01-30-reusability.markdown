---
wordpress_id: 146
layout: post
title: reusability
wordpress_url: http://spindrop.us/2008/01/30/reusability/
site: spindrop
---
[tags]django, plugins, apps, projects, symfony[/tags]


> A project is a collection of settings for an instance of Django, including database configuration, Django-specific options, and application-specific settings. 
>
> [The Django Book, Chapter 2](http://www.djangobook.com/en/1.0/chapter02/):


A few people have been asking for more comparisons between symfony and Django.  For me it's a great way of understanding Django and python as well as symfony and PHP.

Reusability is at the core of Django, not an afterthought.  The only unique part of an app is the settings and the views.  Everything else is an application that can exist independently of your app.  It's nice and decoupled.

This wouldn't be impossible to do in symfony.  Each module could be designed from the start as a plugin.  Complete with its own set of models and default templates.  The configuration of a project/app could then make the web app unique.

Right now the bulk of my symfony models are tightly coupled to their apps.  It's a little confusing, but there isn't a direct correlation between Django projects, Django apps and symfony Projects, apps and modules.  Each kind of overlaps one another.
