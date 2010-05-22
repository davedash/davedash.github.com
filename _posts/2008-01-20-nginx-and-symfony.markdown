---
wordpress_id: 133
layout: post
title: nginx and symfony
wordpress_url: http://spindrop.us/2008/01/20/nginx-and-symfony/
site: spindrop
tags: [symfony, symfony, nginx, server]
---
[tags]nginx, server, symfony[/tags]

I almost gave up on nginx and was going to settle on lighttpd or Apache, but I decided to check the symfony list and in minutes Kiril Angov (Kupokomapa) answered with a working nginx configuration.  This is why I like the symfony community :)

Here's what works (Note: This requires a running FastCGI server):

    server {
      listen       80;
      server_name  mysite.com *;
      root /var/www/mysite.com/web;
      index  index.php;

      charset utf-8;

      location / {
        # If the file exists as a static file serve it directly without
        # running all the other rewite tests on it
        if (-f $request_filename) {
          expires max; 
          break; 
        }

        if ($request_filename !~ "\.(js|htc|ico|gif|jpg|png|css)$") {
          rewrite ^(.*) /index.php last;
        }
      }

      location ~ \.php($|/) {
        set  $script     $uri;
        set  $path_info  "";

        if ($uri ~ "^(.+\.php)(/.+)") {
          set  $script     $1;
          set  $path_info  $2;
        }

        fastcgi_pass   127.0.0.1:9000;

        include /etc/nginx/fastcgi_params;

        fastcgi_param  SCRIPT_FILENAME  /var/www/mysite.com/web$script;
        fastcgi_param  PATH_INFO        $path_info;
      }
    }

This works in my Ubuntu instance of nginx.  Other customziations to this might need to occur, but it's fairly solid so far.
