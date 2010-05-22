---
wordpress_id: 158
layout: post
title: "the magic of django: get_callable"
wordpress_url: http://spindrop.us/2008/02/08/the-magic-of-django-get_callable/
site: spindrop
tags: [spindrop, openid, symfony, php, python, django, magic functions, sfopenidplugin]
---
[django]: http://djangoproject.com/
[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/


[symfony][] is an amazing framework simply because of the uphill battle it has with PHP.  There's a lot of behind the scenes magic that ameliorates the frustrations one might have with PHPs lack of syntactical magic.

A lot of work is done to make sure certain things are autoloaded and that certain things behave the way you expect.

I hadn't had a chance to peek under Django's hood too much myself, but it appears that despite the inherent magic of python, there were some much needed additions.  My savior for today was `get_callable`.
<!--more-->
I have a very particular vision of interacting with OpenID.  Basically I like to decouple as much of the OpenID interactions away from the inner workings of my web site.  I do, however, want a hook where I can supply some of my own logic after OpenID has been verified.

It's roughly how I implimented the sfOpenIDPlugin.   Luckily this time, I was able to rely on the [OpenID 2.1 libraries](http://www.openidenabled.com/openid/libraries/python/) from OpenIDEnabled.

I did ditch their example code, because I wanted a sexy package.  The package isn't quite ready for primetime, but you can [have a gander](http://svn.spindrop.us/django/trunk/) (and yes, I do welcome collaborators and am open to merging my work with the myriad of work that's out there).

### Getting to the point

Anyway, `get_callable` is what allowed me to write my "hook" into my OpenID logic.

In my `settings.py` I defined:

<div><textarea name="code" class="python">
OPENID_SUCCESS = 'myproject.myapp.views.openid_handler'
</textarea></div>

The way my OpenID library works, is it does it's business and when it verifies a url belongs to someone it then delivers he request to the `OPENID_SUCCESS` hook.  Here's how:

<div><textarea name="code" class="python">
            if settings.OPENID_SUCCESS:
                view = get_callable(settings.OPENID_SUCCESS)
                return view(request, result)
</textarea></div>

`get_callable` works some python magic by splitting `myproject.myapp.views.openid_handler` into the module: `myproject.myapp.views` and the attribute `openid_handler`.  It uses this to produce a callable object.  In the example above I gave it parameters of `request` and `result` as they were required by my app.
