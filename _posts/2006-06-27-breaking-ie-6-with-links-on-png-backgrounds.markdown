---
wordpress_id: 41
layout: post
title: Breaking IE 6 with links on PNG backgrounds
wordpress_url: http://spindrop.us/2006/06/27/breaking-ie-6-with-links-on-png-backgrounds/
site: spindrop
tags: [reviewsby.us, css]
---
In <acronym title="Internet Explorer">IE</acronym> there's a whole slew of troubles with <acronym title="Portable Network Graphics">PNG</acronym>.  One such trouble is links or anchors will not work in <acronym title="Internet Explorer">IE</acronym> if you have a <acronym title="Portable Network Graphics">PNG</acronym> image that has gone through the Microsoft `[AlphaImageLoader]`, which is the only known way to render <acronym title="Portable Network Graphic">PNG</acronym>s in <acronym title="Internet Explorer">IE</acronym>6.

The solution, involves running the image filter on a separate element, and then positioning all the links within that element in a higher z-order.  This is explained in better detail in [Filter Flaws][ff].

[AlphaImageLoader]: http://msdn.microsoft.com/workshop/author/filter/reference/filters/alphaimageloader.asp "MSDN article on AlphaImageLoader"
[ff]: http://www.satzansatz.de/cssd/tmp/alphatransparency.html

<!--more-->

I've been running into too many designers who have been sending me too many designs that require translucent layers, and alpha-transparencies (and they should be able to, even though the trend is more simple these days).  This of course subjects me to pretty much any strange quirk that <acronym title="Internet Explorer">IE</acronym>6 can dish out with <acronym title="Portable Network Graphic">PNG</acronym>s.

What's frustrating is that [5 years ago](http://davedash.com/2001/10/16/png_and_internet_explorer/) I had <acronym title="Portable Network Graphic">PNG</acronym>s problems.  This is the Internet... very few problems on the Internet last that long.  There's certainly been enough people complaining about this malfunction in <acronym title="Internet Explorer">IE</acronym> for years.

The problem with these problems is there is no "right" solution.  Using `[AlphaImageLoader]` is a hack.  As we can see with laying links upon backgrounds that use the loader, it's prone to behavior we don't normally expect.  We shouldn't have to raise the links above an invisible layer, in order to click on them.

Unfortunately as long as the majority of our users continue to use <acronym title="Internet Explorer">IE</acronym> 6 (or older) we'll be stuck with this problem.  If we look at [adoption rates](http://www.christopherschmitt.com/2006/04/12/adoption-rate-of-internet-explorer-7/) it won't be until a year after Internet Explorer 7 is out until it's the top dog.  Even then, if Firefox is still at 10% marketshare, that leaves another 40% with <acronym title="Internet Explorer">IE</acronym>6 (or less) and the less popular browsers.  We're still stuck with this problem for some time.
