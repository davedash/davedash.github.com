---
layout: post
title: "Choosing a New Web Stack"
tags: [mozilla, flask, django, babysj]
published: true
time: 10:49PM
---

I like building web sites, a lot.  Usually every few years I need to re-
evaluate the stack I use for a side-project.  Joshua's
[Stack Parts](http://stackparts.com/) site is handy for this.

At Mozilla Webdev we stick to redis + mysql + elasticsearch + celery + rabbitmq
+ memcache + git + [virtualenv][v] + python + django + jinja2 + modwsgi + commander
+ puppet + apache + less + jquery as our go-to stack.  It's tried and true and
it's been working and been evolving for two years.

[v]: /tutorial/virtualenv

So I'm at re-evaluation time.  The first element of the stack I needed to
decide upon was the web framework.  I initially thought I'd use Django, and
maybe alternate a few supporting libraries just to color my experience.  But
Flask caught my attention.

Flask is from Pocoo who have given me great things like:

* lodgeit
* Werkzeug
* Jinja2
* Sphinx

It was a microframework, which meant that it didn't contain as many things as
Django, but at the same time, I didn't use that much of Django.

Flask was a nice way to stay mostly in my comfort-zone, and in some ways, focus
me on just writing an app, and not working in a framework.  Since it's python,
if I start to miss Django, I can probably rewrite my code without too much
effort.

Overall I'm excited, and I just got past, "Hello World."

I'm not sure what my stack will look like, I'm imagining it will evolve into:

postgresql + memcache + git + flask + jinja2 + gunicorn + fabric + puppet +
nginx + less + backbonejs + jquery

This will give me a chance to learn more about things I'm interested in, and
utilize what I think might be better options along the stack.
