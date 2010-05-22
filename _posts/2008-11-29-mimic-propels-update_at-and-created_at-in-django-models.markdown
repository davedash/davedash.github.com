---
wordpress_id: 204
layout: post
title: Mimic propel's update_at and created_at in Django models
wordpress_url: http://spindrop.us/?p=204
site: spindrop
tags: [spindrop, symfony, propel, django]
---
One "trick" that propel offers you is tables with fields `created_at` and `updated_at`.

The fields are self explanatory and within Propel you just define them and they just do their business.

To simulate this in Django just do:

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)


`auto_now` automatically sets a field to the current time, and `auto_now_add` only does this if the object is being added (not updated).
