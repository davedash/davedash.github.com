--- 
wordpress_id: 358
layout: post
title: Alphabetical sorting in Sphinx
wordpress_url: http://spindrop.us/?p=358
---
Sphinx 0.9.9 is great at searching full text, but treating actual strings as attributes takes some work.

Initially I employed the strategy of indexing my full text fields *and* storing them as attributes.  E.g.:

	sql_query = SELECT name, name AS name_ord FROM documents
	sql_attr_str2ordinal = name_ord

This stores each attribute in lexical order.  Meaning if your name's are Apple, Aardvark, Button, Choco-room they would be given the ordinal 2, 1, 3, 4 respectively.

However, this is case-insensitive.  So trying this approach:

	sql_query = SELECT name, UPPER(name) AS name_ord FROM documents
	sql_attr_str2ordinal = name_ord

Will allow for case-insensitive alphabetical sorting in Sphinx.
