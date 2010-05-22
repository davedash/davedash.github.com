---
wordpress_id: 31
layout: post
title: ReviewsBy.Us bugfixes
wordpress_url: http://spindrop.us/2006/05/30/reviewsbyus-bugfixes
site: spindrop
---
A lot of bugs have popped up recently.  

### Logins

The logins weren't redirecting people to the correct place.  Unfortunately the login system still needs a lot of work.  I am probably going to rewrite it completely.  It doesn't consistantly remember where you are coming from or where you intend to go after logging in.  I'll be jotting down a clean system to log people in propperly.

### Tags

Tags work a bit better.  They follow the flickr style of tagging, which is each word is a tag, unless surrounded in double quotes.  Previously they weren't producing a lot of empty tags.

### Latitude and Longitude even more precise.

A small error in the database definitions resulted in lat/longitudes of restaurants that were greater than 100 (or rather `abs(x) > 100` where `x` is latitude or longitude were being truncated to `100` or `-100`.  This was easily fixed so things should look just right on the maps.
