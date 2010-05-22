---
wordpress_id: 135
layout: post
title: Serving Firefox xpi extensions over ssl/https
wordpress_url: http://spindrop.us/2008/01/22/serving-firefox-xpi-extensions-over-sslhttps/
site: spindrop
---
[tags]firefox, cache, xpi, https[/tags]

Apparently serving XPI extensions over HTTPS is a headache.  What happens is you may have a link to an XPI served over HTTPS, but Firefox will ask intercept the download and ask you to add your domain to the allowed hosts.  After allowing it, you can't re-download the file (it gets cached, incorrectly, even if you request it to not do so).

So the workaround is this:

Don't link directly to the XPI file.  Link to an action (e.g. `/getxpi`).  Have this action link to the actual XPI file with a random `GET` parameter, e.g. `https://mydomain.com/xpi/myextension.xpi?ts=123456`.

This will result in any XPI downloaded from `/getxpi` to not be cached.

This is a cruddy work-around for a problem with Firefox, but unfortunately I'm not a XUL hacker.

-d
