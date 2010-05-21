--- 
wordpress_id: 194
layout: post
title: Django Admin and Cookies
wordpress_url: http://spindrop.us/?p=194
---
I was dusting off an old Django project and everything was working except the admin site:

> Looks like your browser isn't configured to accept cookies. Please enable cookies, reload this page, and try again.

The culprit was `SESSION_COOKIE_DOMAIN = "onyxfoundation.org"` being set.

The project wasn't loading into Development mode (it's triggered by hostname) so it set the cookie domain to what I require in production.  Once remedied, everything worked as expected.
