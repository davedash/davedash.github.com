--- 
wordpress_id: 66
layout: post
title: Coming soon to reviewsby.us
wordpress_url: http://spindrop.us/2006/10/02/coming-soon-to-reviewsbyus/
---
In August I took a break from [reviewsby.us][] only to be plagued by spam.  In September, I relinquished portions of the project planning to my wife.  We haven't released anything publicly, yet, but there's a lot in development.

* I updated the development framework to [symfony][] 1.0 alpha and took care of a whole slew of bugs.  
* Katie and I came up with a [wireframe](http://flickr.com/photos/davedash/251518309/) that details some of the upcoming changes.
* I upgraded the user logic to take advantage of sfGuardUser, a user management plugin for symfony.

I'm in progress of writing location specific searches.  I'm slow to implement.  It seems that this month is far busier than I'd like, and I can rarely get in a block of enough time to just crank this out.  The problem with geographic-specific searches is mySQL supports those types of queries, but it's not as easy as I'd like.  Zend Search Lucene with some support from PHP, however, may yield some promising results.  As always, I'll share my findings in a forthcoming tutorial.

Anyway, no visible updates on the actual site, since I didn't want to put alpha software on the live site.  I'm sure by next month symfony will be ready.

[reviewsby.us]: http://reviewsby.us/
[symfony]: http://symfony-project.com/
