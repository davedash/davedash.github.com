---
wordpress_id: 277
layout: post
title: Have unique descriptive page titles
wordpress_url: http://spindrop.us/?p=277
site: spindrop
tags: [spindrop, seo, mozilla, github, usabilitiy]
---
[1]: http://www.google.com/search?hl=en&q=+site:www.sphinxsearch.com+sphinx+api+php
[2]: http://github.com/davedash/Title-Variance/tree

<div style="float:right"><a href="http://www.flickr.com/photos/44124375866@N01/3764074726" title="View 'Sphinx - Free open-source SQL full-text search engine - (Build 20090715083437)' on Flickr.com"><div style="text-align:center;"><img src="http://farm4.static.flickr.com/3588/3764074726_0c02ffd18c.jpg" alt="Sphinx - Free open-source SQL full-text search engine - (Build 20090715083437)" border="0" width="483" height="338" /></div></a>
</div>

One of my internet pet-peeves is people using the same page title for every page on their web site.  Take a look at [this search for Sphinx][1].  As you can see virtually all the links for Sphinx are titled "Sphinx - Free open-source SQL full-text search engine" which blows for usability when it comes to searching, or even managing the various pages you might have open in your web browser.

To get an idea of the page I want I need to look at the abstract which may or may not give me a clue.  Even the forum posts which usually have subjects, have their `<title>` set to the site-wide default.

<!--more-->
The first step in solving this, is identifying you have a problem in the first place.  So I wrote [a tool][2] in python to determine how unique the page titles you have are:

	% python measure.py sphinxsearch.com
	1050 titles found for sphinxsearch.com
	483 unique titles found for sphinxsearch.com
	46% of the pages on sphinxsearch.com have unique titles

This is fairly telling.  It means over half the pages on sphinxsearch.com have a generic title.

This site faired a bit better:

	% python measure.py spindrop.us
	988 titles found for spindrop.us
	822 unique titles found for spindrop.us
	83% of the pages on spindrop.us have unique titles

So please, think about people trying to use the information on your site.  Design your templates in such a way that you can come up with unique titles.

Feel free to expand on this tool, it could easily output the offending pages or titles.
