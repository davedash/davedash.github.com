---
wordpress_id: 111
layout: post
title: "Facebook Markup Language: the Dashboard and Action links"
wordpress_url: http://spindrop.us/2007/07/25/facebook-markup-language-the-dashboard-and-action-links/
site: spindrop
tags: [reviewsby.us, symfony, symfony, reviewsby.us, facebook, plugins, sfFacebookPlatformPlugin, apps, fbml]
---
[tags]facebook, fbml, apps, reviewsby.us, symfony, sfFacebookPlatformPlugin, plugins[/tags]

Facebook has the concept of the dashboard:

![dashboard](http://developers.facebook.com/images/fbml_dashboard.gif)

In case the documentation isn't clear, these are where the top buttons for your app go.

I created the FBMLHelper to help you write links from symfony to facebook.

The dashboard itself is easy to create:

	<fb:dashboard>
	</fb:dashboard>

The links are fairly simple, but if you use [symfony][]...  we like helpers... 

So the `FBMLHelper` has an `fb_action` method which is similar to `link_to`:

  	<?php echo fb_action('My Dining', '@homepage') ?>

Will actually render as:

	<a href="http://apps.facebook.com/reviewsbyus/">My Dining</a>

Provided the `app_facebook_canvas_url` is set to your canvas url (for example, our's is http://apps.facebook.com/reviewsbyus/).

This helper takes care of routing and rewriting the URL to something that will work within Facebook's canvas.

... so start writing some apps.  This plugin will be developed further and I'll try to publish tutorials whenever possible.

[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/
