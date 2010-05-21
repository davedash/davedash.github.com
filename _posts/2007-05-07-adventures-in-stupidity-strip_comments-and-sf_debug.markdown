--- 
wordpress_id: 97
layout: post
title: Adventures in stupidity... strip_comments and SF_DEBUG
wordpress_url: http://spindrop.us/2007/05/07/adventures-in-stupidity-strip_comments-and-sf_debug/
---
[tags]symfony, media temple, fast cgi, anomalies, SNAFU, php, configuration[tags]

Often I run into <acronym title="Situation Normal, All Fucked Up">SNAFU</acronym>s... generally these are minimized by clever frameworks, design patterns, normalizers, etc.  Lately I've been working with a [Mark Quezada](http://mirthlab.com/) on a client hosted at [Media Temple](http://mediatemple.com/) on a dedicated virtual server.

Unfortunately some combination of FastCGI, their build of PHP and symfony just wasn't working.  I beat my head for a few hours and we found out that setting `SF_DEBUG` to `true` would get rid of the problem, or more specifically setting `strip_comments` to `off` would fix this.

Without getting my hands too dirty, something in the way that `sfToolkit::stripComments` strips comments (and I don't know when this happens, but I imagine it happens for compiling and caching parts of the code) doesn't jive well with our servers configuration.

Needless to say, I very much prefer having full control on as many layers of "LAMP" as possible to ensure that what I want done is getting done, even if it means compiling Apache and PHP by hand.
