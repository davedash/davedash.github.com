---
wordpress_id: 356
layout: post
title: Test Driven Confidence
wordpress_url: http://spindrop.us/?p=356
site: spindrop
tags: [spindrop, django, mozilla, addons.mozilla.org, testing, qa]
---
[a]: https://addons.mozilla.org/

If you're already testing your web applications, you can skip this post.

One of the bugs I am working for [AMO][a] on involves porting a small, but moderately complicated checkbox from our PHP site and rewriting it for Django.

I decided to look at the existing implementation and found it to not work correctly at all.  This was frustrating, especially since I verified that my own code worked, and that QA verified that it worked as well.

This is frustrating on many levels.  Chances are some minor assumption I made changed, and thus broke this functionality.  Discovering regressions is never fun, and fixing them is can be long and tedious if you can't automatically verify that everything is working correctly.

Lucky for me, coming up with tests is easy, you just do what you would do to verify the code satisfies the requirements and then code it.  Sometimes the tests can take longer than writing the actual code, but ultimately you can ship with confidence.  You can be confident that your feature won't break in the future without immediate notice, and you can be confident that your new code won't break anything else.
