---
wordpress_id: 115
layout: post
title: "symfony + mod_rewrite: moving smoothly from development to production environments"
wordpress_url: http://spindrop.us/2007/08/14/symfony-mod_rewrite-moving-smoothly-from-development-to-production-environments/
site: spindrop
---
[tags]symfony, mod_rewrite, 404, url, pretty urls, development, production[/tags]

I think a common problem for some symfony developers that aren't too familiar with Apache's Mod Rewrite is when they move from a development environment that uses an explicit controller (e.g. `frontend_dev.php` is requested from the server explicitly) to their production app which implicitly calls `index.php` (e.g. '/' or some other route is passed to `index.php`) things stop working.

This is probably a `mod_rewrite` issue.  Mod Rewrite handles implicitly directing (almost) all traffic to `index.php` in a symfony application.

The default `.htaccess` for symfony is defined as such:

    Options +FollowSymLinks +ExecCGI

    <IfModule mod_rewrite.c>
      RewriteEngine On

      # uncomment the following line, if you are having trouble
      # getting no_script_name to work
      #RewriteBase /

      # we skip all files with .something
      RewriteCond %{REQUEST_URI} \..+$
      RewriteCond %{REQUEST_URI} !\.html$
      RewriteRule .* - [L]

      # we check if the .html version is here (caching)
      RewriteRule ^$ index.html [QSA]
      RewriteRule ^([^.]+)$ $1.html [QSA]
      RewriteCond %{REQUEST_FILENAME} !-f

      # no, so we redirect to our front web controller
      RewriteRule ^(.*)$ index.php [QSA,L]
    </IfModule>

    # big crash from our front web controller
    ErrorDocument 500 "<h2>Application error</h2>symfony application failed to start properly"

As you can see if the `mod_rewrite.c` module is not enabled this will not work.   

Luckily most packages of Apache have the module, it just needs to be enabled by uncommenting the right line of `.htaccess`:

    LoadModule rewrite_module     libexec/httpd/mod_rewrite.so

Restarting apache should give you full rewrite control.  This is fairly basic Apache administration, but for a lot of people symfony is their first foray into URL rewriting.
