---
wordpress_id: 162
layout: post
title: Keep a second web server around for luck...
wordpress_url: http://spindrop.us/2008/02/12/keep-a-second-web-server-around-for-luck/
site: spindrop
tags: [spindrop, symfony, apache, nginx, fastcgi]
---
I had one of those mid-day "what's going on with my server" heart-atacks.  I have a service that emails me when [reviewsby.us][rbu] is down.  On my old server if it went down, I could just restart the server and it'd be back up.  That was big old apache, running out of memory or something.

[Reviewsby.us][rbu] is a medium sized site.  It gets a fair amount of traffic at a steady pace.  Even in this case I decided I was in need for a new server, so I looked into nginx.  It's fast and it can serve static content well and pass things to fastcgi.  Joshua Schachter explains the [proxy in front](http://joshua.schachter.org/2008/01/proxy.html) concept pretty well.

Back to my web developer heart attack...

Well this setup had been holding up for a better part of a month fairly well... then I saw that a lot of the pages just lagged.  I restarted fastcgi and nginx (it was a fastcgi issue).  Rather than try to debug something I couldn't, I quickly installed apache2 and setup the server the tried and tested way.

This all took place in a half an hour.  Not the end of the world, but not elegant either.  In the future, I'll revert to using nginx (possibly nginx+apache versus nginx+fastcgi) but I'll keep my other configurations around when all hell breaks loose.

[rbu]: http://reviewsby.us/
