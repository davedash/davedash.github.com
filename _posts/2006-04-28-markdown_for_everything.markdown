---
wordpress_id: 13
layout: post
title: Markdown for everything
excerpt: |
  [mphp]: http://www.michelf.com/projects/php-markdown/
  [mwe]: http://spindrop.us/files/markdown_everywhere-2006-04-28.tar.bz
  [symfony]: http://www.symfony-project.com/
  [markdown]: http://daringfireball.net/projects/markdown/
  [TinyMCE]: http://tinymce.moxiecode.com/
  [rbu1]: http://reviewsby.us/restaurant/cheesecake-factory/menu/orange-chicken
  [df]: http://daringfireball.net/
  [lj]: http://davedash.livejournal.com/
  [textmate]: http://macromates.com/
  [drupal]: http://drupal.org
  
  Today, in a matter of minutes, I wrote a [really simple markdown web environment][mwe] in PHP.  It's nothing complicated by any stretch of the imagination, but for me at least it'll be quite useful.

tags: [programming, Related Websites, javascript, symfony, reviewsby.us, php, markdown, tinymce, textmate, drupal, mod_rewrite, xhtml]
---
[mphp]: http://www.michelf.com/projects/php-markdown/
[mwe]: http://spindrop.us/files/markdown_everywhere-2006-04-28.tar.bz
[symfony]: http://www.symfony-project.com/
[markdown]: http://daringfireball.net/projects/markdown/
[TinyMCE]: http://tinymce.moxiecode.com/
[rbu1]: http://reviewsby.us/restaurant/cheesecake-factory/menu/orange-chicken
[df]: http://daringfireball.net/
[lj]: http://davedash.livejournal.com/
[textmate]: http://macromates.com/
[drupal]: http://drupal.org

Today, in a matter of minutes, I wrote a [really simple markdown web environment][mwe] in PHP.  It's nothing complicated by any stretch of the imagination, but for me at least it'll be quite useful.

<!-- break -->
<!-- more -->
### My intro to markdown


[symfony] had me seriously investigating [Markdown] for use in my own apps.  The [symfony] Team has made a lot of design choices which for the most part seemed to ones that I liked.  [Markdown] was interesting because my first thought was "that's all fine and dandy, but I think I'll stick with a [TinyMCE] editor instead."  

<!--more-->

But, that's a bit JavaScript heavy, and a bit much for [comment fields][rbu1], for example, or even an entire blog post.  And after reading some posts from [Daring Fireball][df] over the years, I've started to take notice of its elegant format, and the captivating writing style.  Obviously this was all the doing of [Markdown]... or not, but it served as a good selling point.

A month ago, I decided to start writing --- not my [boring day-to-day journal entries][lj], but my more web related musings.  I do a lot of coding that seemingly goes nowhere<sup id="fnr1">[1]</sup>, but I generally learn some very cool things.  So I wanted to start documenting.  I was writing for the web, but I really didn't feel like writing things out was saving me any time, so I decided to take another peek at [Markdown].

I was sold pretty quickly, and with [TextMate] having support, I was sold right away.  There's something comforting about having easy to write code, that didn't require me to write the same <acronym title="Universal Resource Locator">URL</acronym>s over and over and generated consistent <acronym title="eXtended HyperText Markup Language">XHTML</acronym>.  They even had a plugin for it for [Drupal].

### Building the markdown environment

For an article I was writing, I needed to put up some filler pages really quickly.  I didn't need an elegant environment, so even plain <acronym title="HyperText Markup Language">HTML</acronym> would do.  I wasn't looking forward to writing plain boring <acronym title="eXtended HyperText Markup Language">XHTML</acronym> though...

So I took some `mod_rewrite` and a [Michael Fortin][mphp]'s PHP port of [Markdown] and had all my web requests for a folder go through a Markdown processor.

.htaccess:

	RewriteEngine On
	RewriteCond %{REQUEST_FILENAME} !-f
	RewriteCond %{REQUEST_FILENAME} !-d
	RewriteRule ^(.*)$ index.php?q=$1 [L,QSA]

snippet of PHP:

	require('markdown.php');
	$q = $_GET['q'] ? $_GET['q'] : 'index';
	$file = $q . '.markdown';
	if (is_file($file)) {
		$text = Markdown(file_get_contents($file));
	} else {
		$text = 'file not found';
	}
	// ... some fancy decoration and then we just echo $text

Not too much going on here.  The script just looks for a relevant `.markdown` file and converts it to <acronym title="eXtended HyperText Markup Language">XHTML</acronym> and displays it.

### Give it a try

Again, it's not incredibly useful, but it saves me time.  It would probably take you less time to write this than to download it, but who cares: [markdown_everywhere-2006-04-28.tar.bz][mwe].  Enjoy<sup id="fnr2">[2]</sup>.


[1]: #fn1
[2]: #fn2
<div id="footnotes">
	<ol>
		<li id="fn1">Over the last few years I've tried to write (or rewrite) a yearbook site, a random sentence generator, a photo sharing site, a scheduling software, some google map enabled toys and some school related applications. <a href="#fnr1" class="footnoteBackLink"  title="Jump back to footnote 1 in the text.">&#8617;</a></li>
		<li id="fn2">Note that this includes PHP-Markdown which is copywrited by others. <a href="#fnr2" class="footnoteBackLink"  title="Jump back to footnote 2 in the text.">&#8617;</a></li>
	</ol>
</div>
