--- 
wordpress_id: 172
layout: post
title: Yahoo Pipes and reducing information overload
wordpress_url: http://spindrop.us/2008/02/28/yahoo-pipes-and-reducing-information-overload/
---
I've been suffering from some information overload.  I subscribed to Engadget and Gizmodo because I wanted to keep up with some home based network devices like homeplug/powerline and wireless routers.  But Engadget and Gizmodo are overwhelming.

Finally I decided... to write a [pipe][pipes].  If you're not familiar with [Yahoo's Pipes][pipes] it is the best thing to come out of Yahoo! ([Flickr](http://flickr.com/) and [del.icio.us](http://delicious.com/) are acquisitions originally).  Pipes is what Yahoo! should be doing:

* It's niche oriented: It appeals highly to geeks who understand pipes, yet it's very learnable, so you don't need to know how to program to use it.
* It's got a great UI.  The user interface is great, you drag and drop inputs and outputs - again very learnable.
* It's very useful.  As I'll show you, below.
* It harnesses the technology that a large company that Yahoo! can provide that might otherwise be difficult: Pipes has to store a lot of data from RSS feeds, to screen scrapes, to anything that you feed it.  Using Yahoo! technology it's trivial to obtain and process all that.
* It's not a clone or a "me too" of other products: This is completely original, and very appealing.

So my [pipes](http://pipes.yahoo.com/davedash) take a regexp filter (e.g. "delicious" or if your clever "delicious|Yahoo|Google") and give me items that match in a selection of RSS feeds.  So it aggregates things like Engadget and Gizmodo and gives you just what you want to see:

Take a look: [Gadget Filter][gf]

I also made a copy called [Technology Filter][tf] which aggregates the SF Chronicle and TechCrunch.

Try them out, remember you can customize the filters... not everyone likes what I like ;)

[pipes]: http://pipes.yahoo.com/
[gf]: http://pipes.yahoo.com/davedash/gadgets
[tf]: http://pipes.yahoo.com/davedash/tech
