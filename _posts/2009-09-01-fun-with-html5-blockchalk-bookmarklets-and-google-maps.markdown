---
wordpress_id: 301
layout: post
title: Fun with HTML5, Blockchalk, Bookmarklets and Google Maps
wordpress_url: http://spindrop.us/?p=301
site: spindrop
---
[bc]: http://blockchalk.com/developers
[j]: http://twitter.com/joshu/status/3679085168
[b1]: javascript:navigator.geolocation.getCurrentPosition(function(p){window.location='http://maps.google.com/maps?q=http://blockchalk.com/api/v0.6/chalks/'+p.coords.latitude+','+p.coords.longitude;})
[b2]: javascript:c=gApplication.getMap().getCenter();window.location="http://maps.google.com/maps?q=http://blockchalk.com/api/v0.6/chalks/"+c.lat()+","+c.lng()

I've been filing away neat things that I've learned.  Like:

* Firefox supports GeoLocation (which varies in accuracy, but is really accurate for me)
* Stephen Hood released the [Blockchalk API][bc]
* [Google Maps lets you use GeoRSS feeds as a term][j]

This solves the problem I had with BlockChalk, which is I wanted a way that I could see what's going on near where I am - and I don't have an iPhone.

So I wrote two bookmarklets:

[Blockchalk Me][b1] which will list Blockchalk listings near you

and

[Blockchalk this Google Map][b2] which only works if Google Maps is open.  It will load Blockchalks that are near the center of the open Google Map.

Unfortunately Blockchalk doesn't have a lot of data yet, and will return no results if there's nothing within a mile radius.  Hopefully a radius parameter will be included for the API call.

So there's no guarantees on the first bookmarklet, but the second bookmarklet should yield nice results for [this location](http://maps.google.com/maps?q=37.74339,-122.428924).

Enjoy.
