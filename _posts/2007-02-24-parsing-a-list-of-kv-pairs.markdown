---
wordpress_id: 80
layout: post
title: Parsing a list of Key:Value pairs
wordpress_url: http://spindrop.us/2007/02/24/parsing-a-list-of-kv-pairs/
site: spindrop
tags: [reviewsby.us, programming, symfony, openid, php, best-practices]
---
[tags]best practices,php,openID[/tags]
[PHP]: http://php.net/
[openID]: http://openid.net/ 
[reviewsby.us]: http://reviewsby.us/
[symfony]: http://www.symfony-project.com/

I'm working on implementing [openID][] for [reviewsby.us][] and for use in [symfony][] apps.  One thing I was having trouble with was parsing key value pairs, which is one of the requirements to reading responses.  It's a fairly easy task, but [PHP][] offers so many ways to do this.

[openID][] calls for the following [Key-Value format](http://openid.net/specs/openid-authentication-1_1.html#anchor32):

>Lines of:
>
>    * some_key:some value
>    * There MUST NOT be a space before or after the colon.
>    * Newline characters MUST be Unix-style, just ASCII character 10 ("\n").
>    * Newlines MUST BE at end of each line as well as between lines.
>    * MIME type is unspecified, but text/plain is RECOMMENDED.
>    * Character encoding MUST BE UTF-8.

So here is my attempt at parsing something like this as efficiently and error free as possible:
<!--more-->
<div><textarea name="code" class="php">
function splitKV($response) 
{
	$r = array();
	preg_match_all('|^\s*([^:]+):([^:\n]+)[ ]*$|m', $kvs, $matches);
	for($i = 0; $i < count($matches[0]); $i++) {
		$r[$matches[1][$i]] = $matches[2][$i];
	}
	return $r;
}
</textarea></div>

I wrote this function as I was writing the post... and it came out way faster than my previous implementations using `strtok` or a combination of `explode` and `trim`.  Which is good to hear since I do use `preg_` functions quite a bit in PHP and they definitely have their place.

I'm curious if people have found a faster way of parsing through a string of Key-Value pairs.  I'll run it in a test harness and stand corrected if someone comes through with something faster ;).
