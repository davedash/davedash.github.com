---
layout: post
title: "Testing Redis in Django"
tags: [amo, mozilla, redis, mock, django, test]
published: true
time: 4:58PM
---
[amo]: http://addons.mozilla.org/en-US/firefox/
[redis]: http://code.google.com/p/redis/
[django]: http://www.djangoproject.com/
[mock]: https://github.com/mozilla/nuggets/blob/master/redisutils.py#L47

For the [Firefox Add-ons][amo] we've been using [redis][] here and there mostly
for cache, but lately for a few things we'd love to persist.

Unfortunately relying on redis does mean we need to be able to test it.  Since
redis touches some of our core components of the site, we can't just raise a
`SkipTest` like we would for Sphinx search related tests.  I also don't want to
rely on our developers to have redis installed in order to run the
test-suite.

So I built a simple [Mock Redis client][mock].  It's part of our
`redisutils.py` that handles connections to redis.  If a test's `setUp` method
calls `mock_redis` you'll get this phony object that can do a few minimal
redis-like operations.

It works great for our specific cases, but feel free to fork it and make it
better.

Note: This `MockRedis` is specifically designed to work with [django][].
