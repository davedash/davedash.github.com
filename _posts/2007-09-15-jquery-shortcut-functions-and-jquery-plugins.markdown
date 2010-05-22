---
wordpress_id: 122
layout: post
title: jQuery shortcut functions and jQuery plugins
wordpress_url: http://spindrop.us/2007/09/15/jquery-shortcut-functions-and-jquery-plugins/
site: spindrop
tags: [programming, css, javascript, yui, jQuery, shortcuts, readability]
---
[tags]js, javascript, readability, yui, jquery, shortcuts[/tags]

[m]: http://marcgrabanski.com/code/jquery-calendar/

One of the the things that's kept me away from the YUI javascript libraries is longhand.  Or rather, the appeal to jQuery (and Prototype) was the almight $ shorthand.

Of course there are times when it pays to write in long hand.  Marc Grabanski has written a fantastic [calendar plugin][m] which uses a lot of jQuery shorthand.  `$()`, `$.extend` and whatnot are great for quick code, but disaster when you need to be in maximum compatibility mode.  For example, use jQuery with some other libraries and you can get disaster.  It's better to opt for the long-hand `jQuery` and `jQuery.extend` methods.  After some search and replaces, I may have gotten things right, but I think I need to talk to Marc Grabanski and make sure the changes I made make sense.

So remember, long hand is great when other developers are using stuff and namespace conflicts are afoot ;)
