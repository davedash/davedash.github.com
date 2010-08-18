---
layout: post
title: "The Perils of One Giant Fixture"
tags: [mozilla, amo, django]
published: true
time: 9:50AM
---

![Timing](/static/images/2010/08/12/time.jpg)

A while back, I thought it would be good to consolidate all the data used in
testing the django-layer of [AMO][amo] into a single data fixture.
Unfortunately we have 600 tests, which were now loading and unloading large
amounts of data each time the test would run.  This made our tests take 20
minutes.

I decided to cut this down quite a bit, by using smaller fixture files.  Each
fixture file attempts to be a singular primary object (e.g. an Addon or a
Collection or a User) and its associated supporting objects.  It's far from
perfect, but it's achieved tests that run in under 10 minutes.

The other side effect is tests will be simpler.  They'll only include the
addons needed to generate an effect, and if something can't be done easily with
the fixtures in place, we can always alter the data during the test.

[amo]: https://addons.mozilla.org/
