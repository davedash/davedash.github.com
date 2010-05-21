--- 
wordpress_id: 348
layout: post
title: "&lambda;^2: safely doing class based views in Django"
wordpress_url: http://spindrop.us/?p=348
---
[a]: https://addons.mozilla.org/
[call]: http://github.com/davedash/zamboni/blob/b5a147820840e66b542691e7239f15eccdebeec9/apps/api/views.py#L39
[lambda]: http://github.com/davedash/zamboni/blob/b5a147820840e66b542691e7239f15eccdebeec9/apps/api/urls.py#L10
[classview]: http://github.com/davedash/zamboni/blob/609ec5467dd6db6a6647f375e95abced5203a1b2/apps/api/urls.py#L9

When I started rewriting the API for [addons.mozilla.org][a], my views were mostly the same: get some data and render it as either JSON or XML.  I also wanted all my API methods to take an `api_version` parameter, so I decided class based views would be best.  This way my classes could just inherit from a base class.

To do this I had to implement a [`__call__` method][call].  This works fine, except I wanted to store things into the class -- after all the whole point of my use of classes was to keep the code a bit more compact, and cleaner.  So, why pass the api_version around everywhere?  Unfortunately thread-safety comes to play, and you need a separate instance of your class for each request.

<!--more-->

### &lambda;

Django's `urlpatterns` expects a callable object.  So you can't give it an instance of `AddonDetailView()`.  But you could give it a callable that creates an instance of `AddonDetailView()` and passes it `*args` and `**kwargs`.  Luckily python has `lambda` functions.  You can [note how we solved that in our `urlpatterns`][lambda].

### &lambda; &lambda;

But wrapping all your urls with `lambda` is tedious and remembering to pass `*args` and `**kwargs` is error prone.

So let's make a `lambda` function that returns... a `lambda` function that [turns an instance of our class into a callable][classview].

We can now return to coding and not think about thread safety.

&lambda;&lambda;&lambda;
