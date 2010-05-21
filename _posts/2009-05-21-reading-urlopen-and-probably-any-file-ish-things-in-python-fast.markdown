--- 
wordpress_id: 260
layout: post
title: Reading urlopen and probably any file-ish things in python fast
wordpress_url: http://spindrop.us/?p=260
---
So I've been churning away in my last few days in Delicious-land trying to optimize some python code.

I was doing essentially this:

<div><textarea name="code" class="python">
file = urlopen("http://myhost.com/my.json")

for line in file:
  pass

</textarea></div>

and it was taking almost a minute... for a ~3000 line json feed.  Being the n00b that I am, I started getting my python learn on... and thought... an open url connection seems like a bad idea... let's do this:

<div><textarea name="code" class="python">
file = urlopen("http://myhost.com/my.json")
lines = file.read().split("\n")

for line in lines:
  pass

</textarea></div>

Zoom!  Took less than a second... actually putting real code in their (e.g. `simplejson.loads()`) bumped it to 2 seconds.  Hooray.
