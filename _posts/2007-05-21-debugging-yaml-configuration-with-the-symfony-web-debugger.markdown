---
wordpress_id: 99
layout: post
title: Debugging yaml configuration with the symfony web debugger
wordpress_url: http://spindrop.us/2007/05/21/debugging-yaml-configuration-with-the-symfony-web-debugger/
site: spindrop
---
[tags]symfony, yaml, configuration, web debug, debug[/tags]
[symfony]: http://symfony-project.com/

There's no doubt that [yaml](http://www.yaml.org/) configuration files in [symfony][] can be troublesome to debug.

The symfony web debugger comes to the rescue.  

Let's say you're `app.yml` has the following:

	app:
	  admin:
	    email: me@example.com

In your development environment you can look at click on "vars & config"  and under settings see all the `sfConfig::get`able variables.  You'll find the above listed as:

	app_admin_email: me@example.com

This technique is very handy when trying to figure out what key you need to use in `sfConfig::get()`.
