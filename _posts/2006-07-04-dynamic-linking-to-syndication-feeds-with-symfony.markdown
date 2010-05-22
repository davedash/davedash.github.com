---
wordpress_id: 47
layout: post
title: Dynamic Linking to Syndication Feeds with symfony
wordpress_url: http://spindrop.us/2006/07/04/dynamic-linking-to-syndication-feeds-with-symfony/
site: spindrop
tags: [reviewsby.us, programming, symfony]
---
[sf1]: http://www.symfony-project.com/content/book/page/syndication.html "How to build a syndication feed"
[symfony]: http://symfony-project.com/
[rbu]: http://reviewsby.us/


[Adding a statically-linked syndication feed][sf1], a feed that is the same no matter where on the site you are, is a cinch with [symfony], but what about dynamically linked syndication feeds?  Let's say we're building the [latest and greatest Web 2.0 app][rbu], there's going to be hundreds of <acronym title="Really Simple Syndication">RSS</acronym> feeds, not just the most recent items.  We'll want the latest comments to a post, the favorite things of a website member and it all has to be feed enabled.  Sure, we can slap a link to the <acronym title="Real Simple Syndication">RSS</acronym> feed and call it a day, but let's go a step further and stick it in the `<head/>` area as well.  That way when someone clicks on the <acronym title="Real Simple Syndication">RSS</acronym> icon in their browser, or adds a web page to [Bloglines](http://bloglines.com) those extra feeds can be found.

<!--break-->

## Expanding your head

A typical `layout.php` for a symfony app will have a `<head/>` section like this:

	<head>
		<?php echo include_http_metas() ?>
		<?php echo include_metas() ?>
		<?php echo include_title() ?>
		<?php echo auto_discovery_link_tag('rss', 'feed/latest')?> 	
		<?php echo auto_discovery_link_tag('rss', '@feed_latest_georss', 
		array('title' => 'Latest Restaurants\' Locations (GeoRSS)' ))?> 	
		<?php echo include_feeds() ?><!-- this is the custom feed includer -->
		<link rel="shortcut icon" href="/favicon.ico" />
	</head>

Since this is in the [reviewsby.us][rbu] `layout.php`, the latest feed and the latest GeoRSS feed (which we developed in [this article][sp1]) will show up on every page.  So for example, if you use [FireFox], you can subscribe to either link when you click on the orange feed icon (![feed][feed]) in the <acronym title="Universal Resource Locator">URL</acronym> bar no matter where you are in the web-application.

To expand this to allow for multiple feeds, we need to include `<?php echo include_feeds() ?>` (before or after the `auto_discovery_link_tag` calls makes the most sense).  

## Making the Feed Helper

Let's created a `FeedHelper.php` to put the `include_feeds()` function (don't forget to add `use_helper('Feed')` to your `layout.php`).

The function looks like this:

	function include_feeds()
	{
		$type = 'rss';
		$already_seen = array();
		foreach (sfContext::getInstance()->getRequest()->getAttributeHolder()->getAll('helper/asset/auto/feed') as $files)
		{
			if (!is_array($files))
			{
				$files = array($files);
			}
			foreach ($files as $file)
			{
				if (isset($already_seen[$file])) continue;
				$already_seen[$file] = 1;
				echo tag('link', array('rel' => 'alternate', 'type' => 'application/'.$type.'+xml', 'title' => ucfirst($type), 'href' => url_for($file, true)));
			}
		}
	}

The function is doing what the deprecated `include_javascripts` and `include_stylesheets` functions did, just with syndication feeds.  Also note, I stuck to just using <acronym title="Really Simple Syndication">RSS</acronym> feeds.  This function can no doubt be extended to Atom or other feed types, but for my purposes it was unnecessary<sup id="fnr1">[1]</sup>.

[1]: #fn1

## Dynamically setting the feeds

In the [reviewsby.us][rbu] site, the menu items are tagged.  There's tags for [chicken], [indian] and [bread] for example.  Each of them are to have an associated GeoRSS feed as described in a [previous tutorial][sp1].  I built our tagging system similar to [Askeet].  So in our `tag` module I created a function in the corresponding `actions.class.php`:

	public function addFeed($feed)
	{
		$this->getRequest()->setAttribute($feed, $feed, 'helper/asset/auto/feed');
	}

This sets the attribute that `include_feeds()` pulls from.  Here `$feed` is simply the route to our feed.  So in our `executeShow()` I just make a call to `$this->addFeed('@feed_tag_georss?tag=' . $tag)`.  We're done.

We can now go to any of our tagged pages.  Let's try [chicken] and see that we can subscribe to a [GeoRSS feed][chicken feed] of restaurants serving [dishes tagged as chicken][chicken]. 

Slight problem.  The `title` attribute of the generated `link` tags are always `Rss`.  That can be mildly unusable.

## Throwing feed titles into the mix

Let's change our `addFeed()` to allow for a second parameter, a title and have it store both the route and the title in the request attribute:

	public function addFeed($feed, $title = null)
	{
		$feedArray = array('url' => $feed, 'title' => $title);
		$this->getRequest()->setAttribute($feed, $feedArray, 'helper/asset/auto/feed');
	}

We'll also need to adapt the `include_feeds` to appropriately accommodate associative arrays:

	function include_feeds()
	{
		$type = 'rss';
		$already_seen = array();
		foreach (sfContext::getInstance()->getRequest()->getAttributeHolder()->getAll('helper/asset/auto/feed') as $feeds)
		{
			if (!is_array($feeds) || is_associative($feeds))
			{
				$feeds = array($feeds);
			}

			foreach ($feeds as $feed)
			{
				if (is_array($feed)) {
					$file = $feed['url'];
					$title = empty($feed['title']) ? $type : $feed['title'];
				} else {
					$file = $feed;
					$title = $type;
				}

				if (isset($already_seen[$file])) continue;

				$already_seen[$file] = 1;
				echo tag('link', array('rel' => 'alternate', 'type' => 'application/'.$type.'+xml', 'title' => $title, 'href' => url_for($file, true)));
			}
		}
	}

Note, there's a function `is_associative()`.  It's a custom function that we can place in another helper:

	function is_associative($array)
	{
	  if (!is_array($array) || empty($array)) return false;
	  $keys = array_keys($array);
	  return array_keys($keys) !== $keys;
	}

It's a clever way of determining if a function is an associative array or not.

## Conclusion

It looks like our GeoRSS feeds are on all our tag pages.  Now we can take our favorite items labeled as [Indian food][indian] and easily add the <acronym title="Universal Resource Locator">URL</acronym> to a service like [Bloglines][b] and have it [keep us up to date on new Indian dishes][b2].  This was simple, especially when much of the work was taken care of by [the framework][symfony].



[sp1]: http://spindrop.us/2006/04/26/easy_yahoo_maps_and_georss_with_symfony	"Easy Yahoo Maps! with symfony"
[firefox]: http://www.mozilla.com/firefox/ "Firefox"
[feed]: http://feedicons.com/images/layout/feed-icon-12x12.gif	"Feed Available"
[chicken]: http://reviewsby.us/tag/chicken
[chicken feed]: http://reviewsby.us/tag/chicken/geo.rss

[indian]: http://reviewsby.us/tag/indian
[bread]: http://reviewsby.us/tag/bread
[b]: http://bloglines.com/
[b2]: http://www.bloglines.com/sub/http://reviewsby.us/tag/indian
[askeet]: http://symfony-project.com/askeet

<div id="footnotes">
	<hr/>
	<ol>
		<li id="fn1">Most clients support <acronym title="Really Simple Syndication">RSS</acronym> so unless there is a compelling need to use Atom or another format, then keeping it down to one choice is always your best bet. <a href="#fnr1" class="footnoteBackLink"  title="Jump back to footnote 1 in the text.">&#8617;</a></li>
	</ol>
</div>
