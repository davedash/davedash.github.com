--- 
wordpress_id: 30
layout: post
title: Quicksilver + TextMate = craZy delicious development environment
wordpress_url: http://spindrop.us/2006/05/28/quicksilver-textmate-crazy-delicious-development-environment
---
<strong>UPDATE:</strong>Cmd-T allows you to search for the files in your currently opened TextMate project.  I learned this shortly after writing this post, but forgot to mention it.  Thanks again to Tyson Tune for pointing that out.

[osx]: http://www.apple.com/macosx/
[qs]: http://quicksilver.blacktree.com/
[textmate]: http://macromates.com/
[flickr]: http://flickr.com/
[symfony]: http://symfony-project.com/
[sl]: http://www.symfony-project.com/trac/browser/trunk/lib
[php]: http://php.net/

<div class="article_logo">
	<img src="http://spindrop.us/wp-content/uploads/2006/05/qs+tm.png" alt="Quicksilver + Textmate" />
</div>
There's a number of tools for the [OS X][osx] that help me with my productivity (and unfortunately have no equivalents on other platforms).  [Quicksilver][qs], a launcher, and [TextMate], a text editor work wonders and together work fairly well.

[Quicksilver][qs] is a the <acronym title="Graphical User Interface">GUI</acronym> equivalent to the command line.  You can launch applications or files or perform any number of operations on those files or applications.  With its powerful collection of plugins you can have it do much more, for example you can take a music file and play it in iTunes within the iTunes party shuffle.  Or take an image file and have it submit to [flickr] with a few simple keystrokes.  Initially, I couldn't get an idea of the application, other than a lot of people loved it.  Now, I'm barely using it to its potential and I love it.  Using a computer without it is quite a drag.

[TextMate] is similarly feature rich and elegant.  Just using a small number of its features makes it worth its cost.  All my [symfony] projects are written using [TextMate] as are my articles for this web site.  It's strength for me is its automation.
Together Quicksilver and Textmate make a winning combination.
<!--more-->

### Projects in [TextMate]

<div class="screenshot_thumb">
	<a href="http://static.flickr.com/49/154779362_e044c75c04_o.png" title="Larger Photo">
		<img src="http://static.flickr.com/49/154779362_e044c75c04_m.jpg" width="240" height="180" alt="reviewsby.us textmate project screenshot" />
	</a>
</div>

I like the concept of "projects" in [TextMate][] (its common to a lot of text editors).  You can drag files or folders into [TextMate] and group them as you see fit.  

Many of my projects are written using [symfony], so I'll try to keep the entire project folder in my [TextMate] project.  Additionally I'll keep the [symfony libraries][sl] if not the entire [PHP] libraries referenced in the project as well.  Now I have access to all of my files with relative ease.  I generally create a file group in [TextMate] of frequently accessed files to bypass the pain going through hierarchies of folders.

If I have a [TextMate] project open, anytime I open a file that belongs in that project, it will open in that project window.  That means if I use the `mate` command line utility, Finder or even [Quicksilver][qs], it'll still open in the project window.  This is useful.<sup id="fnr1">[1]</sup>

<div class="screenshot_thumb_alt">
<a href="http://static.flickr.com/51/154781466_ca0f67a703_o.png" title="Zoom In"><img src="http://static.flickr.com/51/154781466_ca0f67a703_m.jpg" width="240" height="214" alt="Quicksilver Catalogue" /></a>	
</div>
### Catalogues in [Quicksilver][qs]

When you open up [Quicksilver][qs] and type in some letters, it searches some catalogues by default (e.g. Applications, Documents, Desktop, etc) in an attempt to figure out what the "subject" of your action to be.  These catalogues are fully customizable, so it's trivial to add the directories of your project and your libraries into [Quicksilver][qs].

### New Workflow

<div class="screenshot_thumb">
<a href="http://static.flickr.com/68/154785728_9e7a5a815d_o.png" title="Zoom In"><img src="http://static.flickr.com/68/154785728_9e7a5a815d_m.jpg" width="240" height="82" alt="Quicksilver finding reviewsby.us" /></a>
</div>
Now that you've setup your project in [TextMate] and added the same directories to [Quicksilver][qs], you'll have a much improved workflow.  If you save your [TextMate] project in your Documents directory, you need only open [Quicksilver][qs] (I use Command+Space as a shortcut) and type a few letters of the project (for example, I named my project file `reviewsby.us` for my restaurant review site).

When that's open, I can now open any file of that project in anyway I feel necessary.  Let's say I need to open a library file, like `sfFeed.class.php`.  I need only type in a few letters and it opens inside my project.

This process now saves me a ton of time in digging through hierarchies of folders upon folders.  It's many times quicker than Spotlight.  [Give it a try][qs], there's thousands of uses for it, this is just one way I use it.

[1]: #fn1

<div id="footnotes">
	<hr/>
	<ol>
		<li id="fn1">While debugging errors in a project, if PHP tells you a certain file gave you a certain error, you can highlight the filename in Safari (or any other Cocoa browser), hit Command Escape (or whatever custome keystroke you setup for sending selection to Quicksilver), hit Enter and have it show up in TextMate. <a href="#fnr1" class="footnoteBackLink"  title="Jump back to footnote 1 in the text.">&#8617;</a></li>
	</ol>
</div>
