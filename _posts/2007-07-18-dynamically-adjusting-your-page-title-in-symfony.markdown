---
wordpress_id: 109
layout: post
title: Dynamically adjusting your page title in symfony
wordpress_url: http://spindrop.us/2007/07/18/dynamically-adjusting-your-page-title-in-symfony/
site: spindrop
tags: [reviewsby.us, symfony, symfony, reviewsby.us, seo, title, view.yml, view]
---
[tags]view, view.yml, symfony, reviewsby.us, title, seo[/tags]

[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/

A lot of the content on [reviewsBy.us][rbu] and other sites we make using [symfony][] have dynamic content.  We try to have our page titles reflect the content by prepending the name of the specific restaurant, document or menu item before the site name.

To do this we use a method called `prependTitle`.  I define this in a file called `myActions.class.php` which almost all of my actions subclass in my projects.  This way I can enhance all the actions simply by adjusting the common ancestor, `myActions`:

<div><textarea name="code" class="php">
	  public function prependTitle($title)
	  {
	    $r = $this->getResponse();
	    $d = sfConfig::get('app_title_delimiter', ' &laquo; ');
	    $t = sfConfig::get('app_title');
	    $r->setTitle($title.$d.$t, false);
	  }
</textarea></div>

The page title isn't stored anywhere, so we have to put it in `app.yml`:

	app:
      title: reviewsby.us

Voila!
