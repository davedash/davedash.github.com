--- 
wordpress_id: 457
layout: post
title: PNG and Internet Explorer
excerpt: My &quot;stand in&quot; logo, until I actually work on my crescent moon, is in the top left corner ('be like water').  It was quite an adventure to learn that IE for windows (any version) does not support PNG propperly.

tags: computers web development work
---

My &quot;stand in&quot; logo [**edit:** for a version of this site that no longer exists 26 June 2006], until I actually work on my crescent moon, is in the top left corner ('be like water').  It was quite an adventure to learn that IE for windows (any version) does not support PNG propperly.<!--more-->Essentially the standard for PNG (Portable Network Graphics) calls for web browsers to ignore a &quot;background&quot; color for images.  I saved mine innocently with a background thinking it would be for the best.  It showed up fine in Mozilla, etc.

At work however, I use IE and saw a big black rectangle.  It turns out that it takes the alpha channel and sticks it on top of the image when a background is specified - thus giving an entirely black image.  The alpha channel specifies what's transparent, etc.

Luckily, I have a coworker who's very knowledgable with PNG and we discovered the &quot;fix&quot; for it.  A sad state of affairs.  We did discover that we could - if so desired, create a message for IE/Windows users that others woudln't see.  It would have said &quot;get a real browser.&quot;  Anyway so that's that, and that's why all the graphics on this site are slightly less than perfect, in my opinion.
