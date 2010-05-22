---
wordpress_id: 179
layout: post
title: nginx proxying to apache
wordpress_url: http://spindrop.us/?p=179
site: spindrop
---
I gave up on fastcgi with NginX and django.  Too many things just didn't work, so I decided to keep Apache, but lock it down and thrown NginX in the front to serve static content and to prevent max client issues.

I also applied a similar approach for symfony.  Server configurations after the jump...
<!--more-->
### Apache

You should configure Apache as you would if you were serving directly from Apache.  In otherwords, if you are already using Apache, you don't need to do anything different, save changing a port.

The one tweak I made to a standard configuration is to limit the allowed hosts to just the ones I want.

Here's my django app's `apache.conf`:

	NameVirtualHost *
	<VirtualHost *>
        ServerName onyxfoundation.org

        SetEnvIf X-Magic-Header ^secret$ let_me_in
        <Location "/">
                SetHandler python-program
                PythonHandler django.core.handlers.modpython
                SetEnv DJANGO_SETTINGS_MODULE onyx.settings
                PythonDebug On
                PythonPath "['/var/www/django/'] + sys.path"
                Order Deny,Allow
                Deny from all
                Allow from env=let_me_in
        </Location>
	</VirtualHost>

Note the `SetEnvIf` it can be set however you want, I prefer to match a specific header that I send from `nginx`.

If you are using symfony, something like this will be more appropriate:


    <VirtualHost *>
            ServerName reviewsby.us
            DocumentRoot /var/www/reviewsby.us/web
            DirectoryIndex index.php
	       SetEnvIf X-Magic-Header ^secret$ let_me_in

            <Directory /var/www/reviewsby.us/web>
                    Options Indexes FollowSymLinks

                    RewriteEngine On

                    RewriteRule ^$ index.html [QSA]
                    RewriteRule ^([^.]+)$ $1.html [QSA]

                    RewriteCond %{REQUEST_FILENAME} !-f
                    RewriteRule ^(.*)$ index.php [QSA]
                    Order Deny,Allow
                    Deny from all
                    Allow from env=let_me_in
            </Directory>
    </VirtualHost>


You'll also need to listen on a different port (preferably one that is not exposed to the outside world):

	Listen 8080

### NginX

Now NginX needs to be configured to do 2 things:
1. Serve all static content
2. Pass requests that need interpreting to django or symfony

The Django conf of Nginx is very easy:

    server {
      listen   80;
      server_name onyxfoundation.org;

      location ^~ /static/ {
        alias        /var/www/django/onyx/static/;
        access_log   off;
        expires      30d;
      }

      location / {
        proxy_pass      http://127.0.0.1:8080/;
        proxy_redirect  off;

        proxy_set_header   Host             $host;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;

        proxy_set_header        X-Magic-Header "secret";
        client_max_body_size       10m;
        client_body_buffer_size    128k;

        proxy_connect_timeout      90;
        proxy_send_timeout         90;
        proxy_read_timeout         90;

        proxy_buffer_size          4k;
        proxy_buffers              4 32k;
        proxy_busy_buffers_size    64k;
        proxy_temp_file_write_size 64k;

      }
    }

The settings are trivial.  Everything that's `/static` gets served straight from NginX and the django application is served over Apache.

The same thing is a bit trickier in symfony:

    server {
      listen   80;
      server_name  reviewsby.us;

      charset utf-8;

      location  /sf/ {
        alias  /var/www/reviewsby.us/lib/vendor/symfony/data/web/sf/;
      }
      location /css/ {
        alias /var/www/reviewsby.us/web/css/;
      }
      location /images/ {
        alias /var/www/reviewsby.us/web/images/;
      }

      location /js/ {
        alias /var/www/reviewsby.us/web/js/;
      }

      location / { 
        proxy_pass http://reviewsby.us:8080/;
        proxy_redirect off;

        proxy_set_header   Host             $host;
        proxy_set_header   X-Real-IP        $remote_addr;
        proxy_set_header   X-Forwarded-For  $proxy_add_x_forwarded_for;

        proxy_set_header        X-Magic-Header "secret";
        client_max_body_size       10m;
        client_body_buffer_size    128k;

        proxy_connect_timeout      90;
        proxy_send_timeout         90;
        proxy_read_timeout         90;

        proxy_buffer_size          4k;
        proxy_buffers              4 32k;
        proxy_busy_buffers_size    64k;
        proxy_temp_file_write_size 64k;
      }
    }
    
The added difficulty with symfony is specific to this app (and most default apps) since static content is split amongst the web root (`/js`, `/css`, `/images`, etc) versus the suggested django approach of throwing everything in `/static`.  I now adopt this approach for symfony as well.  It makes everything more flexible in the long-run.

### Conclusion

If you've been hesitating about putting a reverse proxy in front of Apache, hopefully this can help you out.  NginX is a lightweight fast server that can handle far more requests than Apache.  By putting it on the front-lines you can give your app that extra inch it needs to keep churning out requests.

Let me know if this configuration works for you.
