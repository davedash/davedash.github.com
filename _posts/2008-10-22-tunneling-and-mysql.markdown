--- 
wordpress_id: 192
layout: post
title: tunneling and mysql
wordpress_url: http://spindrop.us/?p=192
---
I have a mysql server for [reviewsby.us][1] that requires tunneling, and after establishing a tunnel like so:

	deveshistan:~ dash* ssh user@host -L3307:database_server:3306


I thought I could just do this:

	mysql -u mysql_user -P3307 -h localhost

But I was wrong, `localhost` should be `127.0.0.1`, otherwise mysql will do things in socket mode:

	mysql -u mysql_user -P3307 -h 127.0.0.1



[1]: http://reviewsby.us/
