---
wordpress_id: 57
layout: post
title: "Usability for Nerds: Traversing URLs"
wordpress_url: http://spindrop.us/2006/07/30/usability-for-nerds-traversing-urls/
site: spindrop
---
A recent peeve of mine is <acronym title="Universal Resource Locator">URL</acronym>s that you can't manually traverse.  Let me explain.  Let's say you visit `http://reviewsby.us/restaurant/cheesecake-factory`.  You should manually be able to remove `cheesecake-factory` and see an index page of restaurants at `http://reviewsby.us/restaurant/`.  It makes logical sense for that page to be something that would enable you to find more restaurants.  

This is a throwback to static web sites, that consisted of directories and files.  If you accessed a file by its name, you would see the contents of the file (possibly filtered by the server).  If you accessed a directory, you would see an index of files.  In the world of web apps, however, <acronym title="Universal Resource Locator">URL</acronym>s are made up.  
<!--more-->
Web apps where these gaps are missing can be especially frustrating when you use your browser's history.  Often I reference the [symfony api][sa].  The <acronym title="Universal Resource Locator">URL</acronym> is `http://www.symfony-project.com/api/symfony.html`.  All the other <acronym title="Universal Resource Locator">URL</acronym>s in the <acronym title="Application Programing Interface">API</acronym> listing begin with `http://www.symfony-project.com/api/`, so you could assume that `http://www.symfony-project.com/api/` is an index page.

<div style="">
<img src="http://static.flickr.com/60/200898792_9de3c68eb1.jpg" width="500" height="101" alt="URL autocomplete" />
</div>

It's not the index page (`http://symfony-project.com/api/symfony.html` is).  If you googled for `sfConfig` and got to `http://symfony-project.com/api/symfony/config/sfConfig.html` and didn't feel like figuring out the navigation structure... or let's say at a later date you're using your browser's <acronym title="Universal Resource Locator">URL</acronym> auto-complete feature, you will get a 404 Error[1].

Web applications can try to mirror directory indexes with pretty <acronym title="URL">URL</acronym>s, but often have a few gaps as every <acronym title="Universal Resource Locator">URL</acronym> (or level of <acronym title="Universal Resource Locator">URL</acronym>) needs to be designated in the app.  Its a good idea to fill those in as it is another way to navigate a web site.

[sa]: http://www.symfony-project.com/api/symfony.html
[1]: #fn1


<div id="footnotes">
	<hr/>
	<ol>
		<li id="fn1">Not to pick on the wonderful symfony development team, but I truly do see this a lot on their site.  I'm sure they'll setup a redirect or something to fix this.  Or probably call me out on the fact that many of my sites violate this principle. <a href="#fnr1" class="footnoteBackLink"  title="Jump back to footnote 1 in the text.">&#8617;</a></li>
	</ol>
</div>
