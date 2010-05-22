---
wordpress_id: 42
layout: post
title: Version numbers need dates
wordpress_url: http://spindrop.us/2006/06/28/version-numbers-need-dates/
site: spindrop
---
What is the point of a version number?  For the most part, it's just a [milestone](http://en.wikipedia.org/wiki/Milestone).  The difference between version `2.3` and `2.4` of a software is a given feature-set.  Between `2.3` and `2.5` is an even larger feature-set that encompasses our previous feature-set.

So if I tell you, I have version `0.9.6.2` of svnX what does that tell you?  For most, absolutely nothing.  If I told you I was on [<acronym title="Interstate">I</acronym>-35W](http://en.wikipedia.org/wiki/Interstate_35W) at marker [7a](http://maps.yahoo.com/beta/index.php#maxp=location&q2=55420&q1=55408&mvt=m&trf=0&lon=-93.296215&lat=44.836182&mag=1) you wouldn't have a clue either... unless you looked at the map.

Version numbers tend to force us to look at "maps."  If my `svn` client acts up, I have to go to the website and see how old it is.  Generally this isn't a big deal.  But some sites don't publish *when* they made updates.  Take [Acquisition](http://www.acquisitionx.com/releasenotes.php).  It's great software, but if I told you I was still using 128.3, you would have no clue how out of date I was.

On the otherhand if version numbers incorporated a date, we'd be set.  If I told you I was using `1.0.20050405` of a piece of software and I was experiencing problems, you'd wonder why I hadn't upgraded to something newer.  If something newer didn't exist, you'd question if development has stopped.  

We can address versioning concerns by using this hybrid versioning.  The developer's own style of versioning (e.g. `1.0`, `2.0`, etc) can be combined with dates: `1.1.20060505`.  Now we know this is a `1.1` style release.  Generally that means, the developer feels the software is complete enough to consider it at least `1.0`, but with some improvements beyond that release.  It tells the rest of the world, at a glance, that it was released in May of 2006.
