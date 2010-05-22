---
wordpress_id: 307
layout: post
title: Snow Leopard for Macports and Mysql users
wordpress_url: http://spindrop.us/?p=307
site: spindrop
tags: [spindrop, mysql, osx, mozilla, snow leopard, macports]
---
I use mysql and macports on OSX and both were broken when I upgraded to Snow Leopard.

Mysql was a quick fix:

	ln -s /usr/local/mysql-5.1.35-osx10.5-x86 /usr/local/mysql

(you're installed version might be different).  It turns out a symlink was removed during the Snow Leopard upgrade.

As for MacPorts, I had to install Xcode from the Snow Leopard CD, install the Snow Leopard version of MacPorts and then follow [this migration guide](http://trac.macports.org/wiki/Migration).
