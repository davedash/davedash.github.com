---
wordpress_id: 134
layout: post
title: ddAccessibleFormPlugin updated
wordpress_url: http://spindrop.us/2008/01/22/ddaccessibleformplugin-updated/
site: spindrop
tags: [symfony]
---
[tags]
yui, jquery, javascript, forms, symfony, plugin
[/tags]

[trac]: http://trac.symfony-project.com/wiki/plugins/ddAccesibleFormPlugin
[svn]: http://svn.symfony-project.com/plugins/ddAccessibleFormPlugin
[m]: http://alistapart.com/articles/prettyaccessibleforms

I updated the [symfony] plugin for [Pretty Accesible Forms][m] available [via svn][svn].  Feel free to read about it on [trac][].

Unfortunately jQuery the Javascript library I know and love wasn't helping me in the auto-complete department.  While a very good plugin exists, it wasn't working as well as I'd like.

So I looked toward YUI.  It's what we use at my work (duh) and I wanted to see what all the fuss was about.  So I rewrote the handful of jQuery scripts on [reviewsby.us][rbu] in YUI.  It didn't take too long despite the verbose syntax.

Unfortunately that meant the accessible form plugin which I depend on needed to be updated as well.  So now you've got a choice between jQuery and YUI.

[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/
