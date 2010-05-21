--- 
wordpress_id: 254
layout: post
title: "Designing a tagging system: what is tagging"
wordpress_url: http://spindrop.us/?p=254
---
<img src="http://farm3.static.flickr.com/2080/1592127385_eca211d6af_m.jpg" class="alignright" />

There's a lot of collective knowledge about tagging and how it works, but everybody seems to have their own way of doing it and understanding it.

As the delicious engineer who was responsible for making sure the data integrity was maintained during transitions, I ran a series of audit tests on our bookmarks.  This kept me cozy with our tags on a product level but with some insight into the engineering behind it as well.

I think the biggest struggle with tagging is that its surrounded with "Web2.0" hype.  Technologically tagging is not new.  The way its used is very clever, but its fundamentally simple.

<!--more-->
### Tagging is search

Tagging is no different than keywords assigned to a document.  I'm using document to mean any such object that might be tagged or indexed by a search indexer.   It's clever because rather than using a machine to index a document, or even a publisher to assign keywords, end-users directly assign keywords.  This creates the "folksonomy."

Let's say I have a tagging system, and I tag a photograph with the term "milkshake".  I can conceivably go to a page called "Things tagged as milkshake" and one of the items will be my photograph.  I've just performed a search.

If this sounds simple, that's because it is.  Tags are a user-instantiated index.  It is different because you can do some cleverly cool things with it.  With delicious, I determine my personal index.  That means, I can very quickly find [comical videos](http://delicious.com/davedash/funny+videos) or neat stuff about [django](http://delicious.com/davedash/django) without too much trouble.

The fact that it's "just search" means when you build a tagging system, you can do the same tricks you can do with search.  A mysql database with a tags table can be your search index - or you could use Lucene or Sphinx.  

The point is tagging and retrieving tags is search, so if you can build a search engine, you can build a tagging system.
