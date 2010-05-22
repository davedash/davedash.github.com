---
wordpress_id: 309
layout: post
title: Resolving Django dumpdata errors
wordpress_url: http://spindrop.us/?p=309
site: spindrop
tags: [reviewsby.us, django, testing, fixtures]
---
Recently I recieved this wonderful piece of news when I ran `./manage.py dumpdata` for the first time:

	Error: Unable to serialize database: User matching query does not exist.

I knew this might not work out since I was dealing with a legacy database, but the resolution is quite simple.  First I had to narrow it down to which app was causing this.  Naturally I assumed it was one of the two apps I had, either `common` or `restaurant`.  So I ran: `./manage.py dumpdata common` and `./manage.py dumpdata restaurant`.  The latter had no problem whatsoever.

This made sense, since my `common` application was the only one that made any reference to a `User`.  By looking in my `models.py` for that application, I narrowed it down to my `Profile` object.  Sure enough, commenting it out meant I could get my data.

It ended up being a foreign key mismatch between the `profile` and `user` tables.  Since this is legacy data, this mismatch made sense.  A simple `SELECT id,userid FROM profile WHERE userid NOT IN (SELECT id FROM auth_user)` gave me a list of bad profiles.  Removing them allowed me to create my Django fixtures.
