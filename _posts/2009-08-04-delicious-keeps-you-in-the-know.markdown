---
wordpress_id: 281
layout: post
title: Delicious keeps you in the know
wordpress_url: http://spindrop.us/?p=281
site: spindrop
tags: [spindrop, python, del.icio.us]
---
My last task at Delicious was to build along with the amazing [Vik Singh](http://zooie.wordpress.com/) was to build a new feed of bookmarks that was heavily influenced by Twitter.  It was one of the most interesting and enjoyable pieces of code that I worked on at Delicious.

Over two months since my final check-in, the code is [now in production](http://delicious.com/).  It is mostly as intended, but is lacking an RSS or JSON feed (which I had already built).  This is somewhat disappointing since I was hoping that Delicious would remain as open as it had been in the past.

The algorithm is fairly simple we take a look at what trending topics exist at any moment in time (via Google Trends and Twitter) and we combine it with a list of popular terms.  We take the whole lot of these items and   query search twitter and store an in-memory data table of tweets.  We also take a snapshot of new URLs to the Delicious corpus (basically anything on [Delicious recent](http://delicious.com/recent/) with 1 save).  We cluster the Delicious URLs and then find tweets that are similar to each of these clusters.

The code for this is similar to [Vik's TweetNews](http://zooie.wordpress.com/2009/01/15/twitter-boss-real-time-search/) - but I think the Delicious data is a nicer fit.

We optimized this quite a bit and built a very fast inverted-index and tweaked the code to run in about a minute.  Like TweetNews the heart of this was built using Python.  Python while being a dynamic language is quite amazing for manipulating and iteratiting over sets of data.

While building this tool, it became my way to feel pulse of what's going on.  I could ditch a lot of my RSS feeds and rely solely on Delicious to be on the up and up.  Unfortunately I can't subscribe to a feed for this.  Either delicious has made a mistake and didn't launch their feeds at the same time as their web (entirely possible, since Delicious hasn't been updated for most of 2009) or they are deliberately taking a step backwards. 

This step backwards is weird from the usability issue.  Delicious has always been a tool that allowed for multiple types of consumers and a tool that appealed to developers thanks to its myriad of RSS and JSON feeds.    I'm glad I didn't have to be on the losing side of that decision.  Delicious relies heavily on Google Trends and Twitter Search.  While there is no requirement for them to share the data they are mashing up, it would be the right thing to do.

Let me know what you think of the new feeds.  I wish I could share a github link or something snazzy so you could play around with it, but this post should be a good starting point for other real-time data mashups.

**Update**: Read [Vik's account of this on the Delicious Blog](http://blog.delicious.com/blog/2009/08/delicious-homepage-gets-%E2%80%9Cfresh%E2%80%9D.html).
