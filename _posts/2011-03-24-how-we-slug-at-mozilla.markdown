---
layout: post
title: "How we slug at Mozilla"
tags: [unicode, slugs, mozilla, django, python]
published: true
time: 5:07PM
---

One problem we find with slug generators, is they do an awful job with unicode.
For a string like this: `Bän...g (bang)` you get something like
`bng---g--bang-` or at best `bang-bang`.  But it's 2011, urls can have
unicode... here's what we really want: `bäng-bang`.

In some cases transliteration might be acceptable.  But if we look at Django's
approach it fails at Russian.  Here's a comparison with ours for the Russian
phrase "Быстрее и лучше!" ("Faster and better!"):

    >>> from django.template.defaultfilters import slugify as djslugify
    >>> from slugify import slugify
    >>> str = u'Быстрее и лучше!'
    >>> print djslugify(str)

    >>> print slugify(str)
    быстрее-и-лучше

So as you can see, the built-in Django `slugify` could be disastrous.  So take
a look at [ours][g].  If you have some more test cases, please fork it.

[g]: https://github.com/mozilla/unicode-slugify

