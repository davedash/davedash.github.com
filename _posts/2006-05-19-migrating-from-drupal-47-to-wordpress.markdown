--- 
wordpress_id: 25
layout: post
title: Migrating from Drupal (4.7) to Wordpress
wordpress_url: http://spindrop.us/2006/05/19/migrating-from-drupal-47-to-wordpress
---
[katie]: http://katiebonn.com/
[drupal]: http://drupal.org/
[wordpress]: http://wordpress.org/
[spindrop.us]: http://spindrop.us/

I helped [Katie][] setup her new blog this weekend and decided that [WordPress] offers much of what I want out of this blog for a lot less effort than [drupal][]<sup id="fnr1">[1]</sup>.  I decided it might be worth my time to now while this blog is in it's infancy to try converting from [drupal][] to [WordPress][].
<!--more-->

The way I start most of my projects is with a plan:

*	[Discovery](#discovery): Find any articles about converting and get a gist of what to do.
*	[Implementation](#implementation)
	*	Create a temporary subdomain to install [WordPress][]
	*	Install [WordPress][]
	*	[Copy all content](#copy_content)
	*	Copy all static pages
	*	[Configure <acronym title="Universal Resource Locator">URL</acronym>s to match the existing site](#urls) <sup id="fnr2">[2]</sup>
	*	[adjust templates](#adjusting_templates)
	*	split entries correctly (i.e. change `<!--break-->` to `<!--more-->`)
*	[Make the switch when I'm satisfied](#make_the_switch)

I'm really confident that this will be easy.  I don't even have to worry about comments or anything, since this blog is pretty new, but I can demonstrate how to take care of the.

<h3 id="discovery">Discovery</h3>

[v]: http://vrypan.net/log/archives/2005/03/10/migrating-from-drupal-to-wordpress/

[This post][v] details a migration path from [drupal][] to [wordpress][].  Some considerations had to be made since I'm using [drupal] 4.7.

<h3 id="implementation">Implementation</h3>

<h4 id="copy_content">Copy content</h4>

I followed most of the instructions, with some alterations from [vrypan.net][v].

I installed [WordPress] and in `mysql` ran the following commands:

	use wordpress;
	delete from wp_categories;
	delete from wp_posts;     
	delete from wp_post2cat;
	delete from wp_comments

I run my [drupal] site in the same database server, so the data copying was a snap.  If you aren't so fortunate, just copy the relevant drupal tables temporarily your wordpress database. 

First we get the [drupal] categories into [WordPress]:

	USE wordpress;
	
	INSERT INTO 
		wp_categories (cat_ID, cat_name, category_nicename, category_description, category_parent)
	SELECT term_data.tid, name, name, description, parent 
	FROM drupal.term_data, drupal.term_hierarchy 
	WHERE term_data.tid=term_hierarchy.tid;

Again with the posts:

	INSERT INTO 
		wp_posts (id, post_date, post_content, post_title, 
		post_excerpt, post_name, post_modified)
	SELECT DISTINCT
		n.nid, FROM_UNIXTIME(created), body, n.title, 
		teaser, 
		REPLACE(REPLACE(REPLACE(REPLACE(LOWER(n.title),' ', '_'),'.', '_'),',', '_'),'+', '_'),
		FROM_UNIXTIME(changed) 
	FROM drupal.node n, drupal.node_revisions r
	WHERE n.vid = r.vid
		AND type='story' OR type='page' ;

And the relation between posts and categories:

	INSERT INTO wp_post2cat (post_id,category_id) SELECT nid,tid FROM drupal.term_node ;

And finally comments:

	INSERT INTO 
		wp_comments 
		(comment_post_ID, comment_date, comment_content, comment_parent)
	SELECT 
		nid, FROM_UNIXTIME(timestamp), 
		concat('',subject, '<br />', comment), thread 
	FROM drupal.comments ;

I ended up moving the one static page I had into [WordPress]'s "pages" section manually.

Since my pages are written in [Markdown], I enabled the [Markdown for WordPress plugin][mp].

[Markdown]: http://daringfireball.net/projects/markdown/
[mp]: http://www.michelf.com/projects/php-markdown/

<h4 id="urls"><acronym title="Universal Resource Locator">URL</acronym>s</h4>

Now for the real test.  I needed to go through each page on my site and see if I could get to it using the same <acronym title="Universal Resource Locator">URL</acronym>s.  Since I had only 14 posts, I did this somewhat manually.  I used [drupal]'s built in admin to do this from most popular to least popular.  Most <acronym title="Universal Resource Locator">URL</acronym>s worked fine.  There were a small number that didn't for various reasons, I used custom `mod_rewrite` rules to handle them.

<h4 id="adjusting_templates">Adjusting Templates</h4>

My [drupal] template was fairly clean and simple.  So I adjusted the <acronym title="Cascading Style Sheet">CSS</acronym> for the default theme in [WordPress] until I got what I liked.  Very minimal changes had to be made to the actual "<acronym title="HyperText Markup Language">HTML</acronym>."

<h3 id="make_the_switch">Make the switch</h3>

Well, time to make the switch.  In the WordPress administration, I just had to tell it that it's now going to be located at `spindrop.us`.  Then I moved my [WordPress] installation to the [spindrop.us] web root.  It was a snap.  Let me know if you have any troubles.

[1]: #fn1
[2]: #fn2
<div id="footnotes">
	<hr/>
	<ol>
		<li id="fn1">Taxonomy, legible <acronym title="Universal Resource Locator">URL</acronym>s and trackback support all seemed quite difficult to master in Drupal.  In Wordpress they appeared to be available standard or with a minor change in the administration panels. <a href="#fnr1" class="footnoteBackLink"  title="Jump back to footnote 1 in the text.">&#8617;</a></li>
		<li id="fn2">This is a prime reason why <acronym title="Universal Resource Locator">URL</acronym>s should be clean and make sense to the end user, not the programmer of the publishing software. <a href="#fnr2" class="footnoteBackLink"  title="Jump back to footnote 2 in the text.">&#8617;</a></li>
	</ol>
</div>
