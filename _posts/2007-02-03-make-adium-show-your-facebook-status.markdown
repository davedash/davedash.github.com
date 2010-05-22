---
wordpress_id: 76
layout: post
title: Make Adium show your Facebook status
wordpress_url: http://spindrop.us/2007/02/03/make-adium-show-your-facebook-status/
site: spindrop
tags: [programming, rss, tutorial, programming, facebook, chat]
---
[xml]: http://us3.php.net/simplexml/
[curl]: http://www.php.net/curl

By using a simple <acronym title="Really Simple Syndication">RSS</acronym> feed, you can have Adium report your Facebook status.

I am a late-adopter to social networks.  I participated in LiveJournal years after many of my friends started using it.  I finally got into Facebook months after it was "openned up."  I like this strategy because I can immediately find my friends on the network and add them and amass 100s in a few short days.

Facebook is nice for its simple and clean interface.  Even the features are fairly simple.  I like the status feature... for no good reason.  It's a simple AJAX status update that updates your status on the site.  What I don't like to do is repeat myself.  I wanted Adium to repeat what Facebook said.

<!-- more -->

My first inkling was to use the Facebook <acronym title="Application Programming Interface">API</acronym>, but that seemed less appealing since it would involve authentication.  I almost gave up and then discovered that in Facebook you can go to "My Profile" and under "Status" go to "See All" and there's an RSS link to your status messages.  Awesome.  All I needed to do is grab the first one.

I decided this looked like a task for [Simple XML][xml] which can take an XML string and turn it into a PHP object.

The first step of course was to fetch the <acronym title="Really Simple Syndication">RSS</acronym> feed into a string.  `file_get_contents` made the most sense, but Facebook does a browser check even for getting RSS feeds.  I'm not fond of browser sniffing, but its easy to work around if you use [cURL][].  

<div><textarea name="code" class="php">
&lt;?php
	$url = "http://mynework.facebook.com/feeds/status.php?replace=with&your=own&feed=url";

	// setup curl
	$ch = curl_init();
	curl_setopt ($ch, CURLOPT_URL, $url);
	curl_setopt ($ch, CURLOPT_HEADER, 0);

	//spoof Firefox
	curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.1) Gecko/20061223 Firefox/2.0.0.1");

	// begin output buffering
	ob_start();
	curl_exec ($ch);
	curl_close ($ch);
	// save buffer to string
	$xmlstr = ob_get_contents();

	ob_end_clean();

	// convert string to xml object
	$xml = new SimpleXMLElement($xmlstr);

	// status messages start with 'Dave is...' 
	// I just want everything after my name
	echo str_replace('Dave ', null,$xml->channel->item->title);

</textarea></div>


Excellent... this does exactly what I want - but it's slow.  Like any good script, we should use caching if it makes sense.  Obviously we don't want to overload the servers at Facebook (or for that matter any place that serves up <acronym title="Real Simple Syndication">RSS</acronym> feeds) so we implement <acronym title="PHP Extension and Application Repository">PEAR</acronym>'s [Cache_Lite](http://pear.php.net/package/Cache_Lite) package.  We'll tell it to cache results for 15 minutes.  The code changes are marked with `//+++` at the end of each new line:

<div><textarea name="code" class="php">
&lt;?php

	require_once('Cache/Lite.php'); //+++
	
	$url = "http://mynework.facebook.com/feeds/status.php?replace=with&your=own&feed=url";

	$options = array('cacheDir' => '/tmp/', 'lifeTime' => 600); //+++

	$Cache_Lite = new Cache_Lite($options); //+++

	$data = null; //+++
	// attempt to load the data from cache,  //+++
	// otherwise load it anew from RSS //+++
	if (!($data = $Cache_Lite->get($id))) { //+++
	// setup curl
		$ch = curl_init();
		curl_setopt ($ch, CURLOPT_URL, $url);
		curl_setopt ($ch, CURLOPT_HEADER, 0);

		//spoof Firefox
		curl_setopt($ch, CURLOPT_USERAGENT, "Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en-US; rv:1.8.1.1) Gecko/20061223 Firefox/2.0.0.1");

		// begin output buffering
		ob_start();
		curl_exec ($ch);
		curl_close ($ch);
		// save buffer to string
		$xmlstr = ob_get_contents();

		ob_end_clean();

		// convert string to xml object
		$xml = new SimpleXMLElement($xmlstr);

		// status messages start with 'Dave is...' 
		// I just want everything after my name
		$data = str_replace('Dave ', null,$xml->channel->item->title); // +++

		$Cache_Lite->save($data); //+++

	} //+++

	echo $data; //+++
	
</textarea></div>

That's it on the PHP side.  On the Adium side you'll need to use the [exec AdiumXtra](http://www.adiumxtras.com/index.php?a=xtras&xtra_id=1255).  It'll allow you to set your status to something like:

	/exec {/usr/local/php5/bin/php /usr/local/bin/facebook.php}

Enjoy.
