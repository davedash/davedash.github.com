---
wordpress_id: 50
layout: post
title: Safari Fixes
wordpress_url: http://spindrop.us/2006/07/11/safari-fixes/
site: spindrop
tags: [reviewsby.us, css, spindrop]
---
Safari interprets `/* */`s differently than FireFox or <acronym title="Internet Explorer">IE</acronym>.  <acronym title="FireFox">FF</acronym> and <acronym title="Internet Explorer">IE</acronym> will ignore a unmatched `/*` or `*/`, whereas Safari will ignore parts of code if there's a lone `*/`.  Once I found that out, I was able to get the list items that are used throughout the site to render properly.
