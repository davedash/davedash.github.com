---
wordpress_id: 144
layout: post
title: Templating
wordpress_url: http://spindrop.us/2008/01/28/templating/
site: spindrop
tags: [programming, symfony, symfony, php, python, django, smarty]
---
[tags]smarty, symfony, php, python, django[/tags]

I used to use the Smarty templating system quite heavily in my PHP apps.  Then after switching over to [symfony][], I broke that habit.

PHP *is* a templating language for better or worse.  Smarty was a way of saying that "well things could be easier", but that's against the grain of what PHP fundamentally is.

One frustration of PHP is this.  A "pure" PHP file with no HTML looks like this:

<div><textarea name="code" class="php">
	<?php
	
	// code goes here
	// ...
	
	// end of file
</textarea></div>

PHP is an HTML templating system, by default everything in PHP is just stuff waiting to be sent untouched to the browser.  So in essence, PHP web apps aren't really web apps... they are very complicated templates all talking to each other.

So you'll note in the above example, even a pure PHP file must begin with `<?php`, and signal that we're actually doing code.  In fact, to prevent any unintended whitespace being sent to the browser, a PHP only file will by convention omit the closing `?>`.

So my shiny new Django framework is a breath of fresh air.  There's no `<?py` tags, it's all just python.  And template files are explicitly template files parsed by a template engine built on top of a scripting language.

I can easily see PHP evolving into something similar one day.  Where all PHP files are just PHP by default.  It would be more in line with the way MVC development is going. 

[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/
