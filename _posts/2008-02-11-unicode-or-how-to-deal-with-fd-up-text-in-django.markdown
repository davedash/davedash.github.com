---
wordpress_id: 160
layout: post
title: Unicode or How to deal with f'd up text in Django
wordpress_url: http://spindrop.us/2008/02/11/unicode-or-how-to-deal-with-fd-up-text-in-django/
site: spindrop
---
So I've been going out of my mind trying to figure out why something like:

Pham's would look like Phamâ€™s

After searching as much as I could into django and unicode, I found [this article][a] which worked.

As near as my feeble USA-centric "cafes not cafés" understood it, my data was encoded incorrectly, and PHP's mysql ignores encoding and expects UTF-8 whereas django tries to understand the encoding.


[a]: http://automatthias.wordpress.com/2006/12/10/mysql-encoding-problems-on-dreamhost/
