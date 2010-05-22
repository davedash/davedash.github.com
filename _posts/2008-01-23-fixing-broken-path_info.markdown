---
wordpress_id: 137
layout: post
title: Fixing broken PATH_INFO
wordpress_url: http://spindrop.us/2008/01/23/fixing-broken-path_info/
site: spindrop
tags: [symfony, symfony, php, nginx, path_info, cgi]
---
[tags]php, cgi, path_info, nginx, symfony[/tags]

[symfony][] and other applications rely on the server's `PATH_INFO` being set properly.  According to [NCSA](http://hoohoo.ncsa.uiuc.edu/cgi/env.html):

	The extra path information, as given by the client. In other words, scripts can be accessed by their virtual pathname, followed by extra information at the end of this path. The extra information is sent as `PATH_INFO`. This information *should be decoded by the server* if it comes from a URL before it is passed to the CGI script.

Unfortunately, I use a nonstandard server that doesn't natively support CGI, so everything sent to the FastCGI server is done so via parameters that are usually obtained from the HTTP request, but I can't figure out how to do a `urldecode` in my configuration.

So to workaround this I used the `auto_prepend_file` directive in `php.ini`.  With OP code caching this shouldn't hurt too much:

	auto_prepend_file = /var/www/pathinfofix.php

I then added the following script:

	<?php 
	$_SERVER['PATH_INFO'] = urldecode($_SERVER['ORIG_PATH_INFO']);

Voila, the `PATH_INFO` is in a format that symfony (and any other PHP script that depends on `PATH_INFO`) needs.

[symfony]: http://symfony-project.com/
