---
wordpress_id: 206
layout: post
title: Python String Formatting
wordpress_url: http://spindrop.us/?p=206
site: spindrop
tags: [spindrop, python, string]
---
Python 2.6 (and Py3K) introduce a new way to format strings.  Perviously you did this:

	"%s, Here is my string, %s!" % ('Salutations', 'Dave')

Now you do this:

	"{0}, Here is my string, {1}!".format('Salutations','Dave')

At first glance this looks like syntactical-sugar.  But now you can do some clever things (which you could have done before, but I think are more intuitive now).  You can easily repeat strings:

	def tag(name, value):
		return "<{0}>{1}</{0}>".format(name, value)

