--- 
wordpress_id: 335
layout: post
title: Retrieving elements in a specific order in Django and mySQL
wordpress_url: http://spindrop.us/?p=335
---
[z]: http://github.com/jbalogh/zamboni

If you have a list of ordered ids and you want to turn them into an ordered result set you can use `FIELD()` in mysql:

	SELECT * FROM addons
	ORDER BY FIELD(id, 3, 5, 9, 1);
	
This is a handy trick if you use an external search engine which gives you an ordered list of ids and you want to pull out entire row sets.

We do this in [addons.mozilla.org][z] using the Django ORM like so:

<script src="http://gist.github.com/301162.js"></script>

[The code in action](http://github.com/jbalogh/zamboni/commit/a0166108e8a62f386b4310cab0ceb3502575d520#L1R219).
