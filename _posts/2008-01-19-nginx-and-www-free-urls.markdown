--- 
wordpress_id: 132
layout: post
title: nginx and 'www' free urls
wordpress_url: http://spindrop.us/2008/01/19/nginx-and-www-free-urls/
---
[tags]nginx, rewrite[/tags]

I'm not a fan of 'www' in urls and I've been flirting with nginx (pronounced Engine-X as much as I want to call it N-jinx).

Here's a one-liner that'll rewrite your urls:


	# rewrite hostname
	server {
	  server_name www. mydomain.com;
	  rewrite ^/(.*) http://mydomain.com/$1 permanent;
	}

I put this at the end of the definition for `mydomain.com`.
