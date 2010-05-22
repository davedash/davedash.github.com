---
wordpress_id: 198
layout: post
title: sfGuardUser -> django.contrib.auth
wordpress_url: http://spindrop.us/?p=198
site: spindrop
tags: [spindrop, symfony, django]
---
If you find yourself moving from symfony to Django, here's how you `sf_guard_user`'s user table to `django.contrib.auth` user table:

	INSERT INTO 
		auth_user (id, username, password, is_active, last_login, date_joined)
	SELECT 
		id, 
		username, 
		CONCAT(algorithm,'$', salt, '$', password), 
		1, 
		last_login, 
		created_at 
	FROM sf_guard_user;

	DROP TABLE sf_guard_user;

Luckily, django uses a similar salting and encryption strategy as symfony, so it's easy to go back and forth.
