---
wordpress_id: 54
layout: post
title: How to remove file extensions from URLs
wordpress_url: http://spindrop.us/2006/07/26/how-to-remove-file-extensions-from-urls/
site: spindrop
---
<acronym title="Universal Resource Locator">URL</acronym>s should be treated as prime real estate.  Their primary purpose is to locate resources on the Internet.  So for a web developer, it makes sense to make things as user-friendly as possible.  One effort is to remove the extensions from files.  I don't mean things like `.html` or `.pdf`, as those give you an idea that you're reading a page of content or a <acronym title="Portable Document Format">PDF</acronym> document.  I meant things like `.php` or `.asp` or `.pl`, etc.  These are unnecessary items that just clutter the location bar on most browsers.


There are two ways to do this.  The easy way which just looks at a request, if the requested filename doesn't exist, then it looks for the filename with a `.php` (or `.asp` or whatever) extension.  In an `.htaccess` file:

	RewriteEngine On
	RewriteCond %{REQUEST_FILENAME} !-f
	RewriteCond %{REQUEST_FILENAME} !-d
	RewriteRule ^(.*)$ $1.php [L,QSA]

Now if you go to: `http://domain/about` the server will interpret it as if you went to `http://domain/about.php`.

Makes sense, but if we're already breaking the relation between <acronym title="Universal Resource Locator">URL</acronym> and filename, we may as well break it intelligently.  <!--next page-->Change that `.htaccess` file:

	RewriteEngine On
	RewriteCond %{REQUEST_FILENAME} !-f
	RewriteCond %{REQUEST_FILENAME} !-d
	RewriteRule ^(.*)$ index.php?q=$1 [L,QSA]

Now if you go to: `http://domain/about` the server will interpret it as if you went to `http://domain/index.php?q=about`.  How is this useful?  Well now `index.php` is *always* called, so it can do anything common to all pages (which might be nothing) and do something based on the `$_GET['q']` variable.

For example:

	require_once('html_functions.php');
	switch ($_GET['q']) {
		case 'about':
			echo myhead('about page');
			break;
		default:
			echo myhead('home page')
			break;
	}
	include($_GET['q'] . '.php');
	echo myfoot();

We're loading a hypothetical library `html_functions.php` which contains some simple functions (`myhead()` and `myfoot()`) that print out a simple header or footer for this site.  The `switch` statement dynamically sets the `<head/>`.  After the `switch` we include a file based on the query string.  In our case it will still pull up `about.php`.  Granted, this is not what I use personally, but it's the general idea behind how [symfony] works.

### Why?

So why go through all this nonsense?  Extensions for the most part don't mean much to an end user.  Sure, `jpg`, `png` or `gif` mean images and `html` mean web page and `pdf` means the file is a <acronym title="Portable Document Format">PDF</acronym> document.  Dynamic pages, however usually come from `cgi`, `php`, `pl` , `asp`  pages or some other 3 or 4 letter extension that the server uses as a hint to determine how to parse, but the output is usually `html`.  Servers are smart though.  They don't need hints, and the above code eliminates the need to reveal so explicitly just how a page is delivered.  Take our [restaurant review site][rbu], for the most part you can't tell that it's done in `php`.  In fact all the <acronym title="Universal Resource Locator">URL</acronym>s are "clean" and somewhat logical.  The benefit of having clean simple <acronym title="Universal Resource Locator">URL</acronym>s is if we decide to change from PHP to <acronym title="Active Server Pages">ASP</acronym> for example, we won't need to change our <acronym title="Universal Resource Locator">URL</acronym>s. 

[symfony]: http://symfony-project.com/
[rbu]: http://reviewsby.us/
