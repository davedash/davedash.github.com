--- 
wordpress_id: 266
layout: post
title: "Question: Building a Better Search Engine"
wordpress_url: http://spindrop.us/?p=266
---
So I finally have one of those jobs where I can tell people almost every little detail about what I'm doing and I'm encouraged to talk to people on the intar-webs and solicit opinions.

Uh - this is more or less how I've operated at previous jobs, just now I can be overt about it.

So my [new task](https://bugzilla.mozilla.org/show_bug.cgi?id=498999) is to work on improving the [addons.mozilla.org](http://addons.mozilla.org) search engine.  I've built various "search engines" over time in PHP, powered by Lucene and most recently in python using an inverted index.

One tool that I've been looking at briefly is [Sphinx](http://sphinxsearch.com/).  While my record count is low (5-10K), Sphinx basically bakes in a lot of the things I would want in a search engine.  Indexing, merging, etc.

Since I'm fairly new to the add-ons team I'm still understanding the basics of what we need:

* Fast automated indexing of addons for Firefox, Thunderbird and any other Mozilla product
* Quick result sets
* Easy deployability
* Extendible
* Customized ranking
* Filtering (e.g. by Firefox version, etc).
* Basics: Stemming and stop-words

Whether it's Sphinx, Lucene or some home grown solution, I have all that to support.  But this should be fairly straight forward.  What are people's thoughts?
