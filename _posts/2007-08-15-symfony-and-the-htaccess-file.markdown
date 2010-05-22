---
wordpress_id: 116
layout: post
title: symfony and the .htaccess file
wordpress_url: http://spindrop.us/2007/08/15/symfony-and-the-htaccess-file/
site: spindrop
tags: [spindrop, symfony, performance, apache, .htaccess]
---

One performance boost that can be garnered from a symfony app (or any app for
that matter) is disabling `.htaccess`.  `.htaccess` does not need to be parsed
on each visit to your app.  Disabling `.htaccess` is trivial in your
VirtualHost or another relevant part of your apache configuration place:

	AllowOverride None

symfony does require the Rewrite recipes in .htaccess to properly give you
pretty urls, so place those statements right after `AllowOverride None`.

In my specific case I used this:

	<VirtualHost *>
	  ServerName contest.spindrop.sf
	  DocumentRoot    /Users/davedash/Sites/spindrop/web/
	  DirectoryIndex  frontend_dev.php

	  <Directory /Users/davedash/Sites/spindrop/web/>
	    Options Indexes FollowSymLinks MultiViews
	    AllowOverride None
	    <IfModule mod_rewrite.c>
	      RewriteEngine On

	      RewriteCond %{REQUEST_URI} \..+$
	      RewriteCond %{REQUEST_URI} !\.html$
	      RewriteRule .* - [L]

	      RewriteRule ^$ index.html [QSA]
	      RewriteRule ^([^.]+)$ $1.html [QSA]
	      RewriteCond %{REQUEST_FILENAME} !-f

	      RewriteRule ^(.*)$ frontend_dev.php [QSA,L]
	    </IfModule>
	  </Directory>
	</VirtualHost>

Now all these rewriting rules are loaded when the server is restarted and the
`.htaccess` is not examined upon each request.
