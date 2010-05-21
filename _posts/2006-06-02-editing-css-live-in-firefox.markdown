--- 
wordpress_id: 34
layout: post
title: Editing CSS live in Firefox
wordpress_url: http://spindrop.us/2006/06/02/editing-css-live-in-firefox
---
### Summary
`Firefox + Web Developer Extension = Live CSS Editing` if that makes sense to you, you probably don't need to read on any further, except perhaps the "caveats" section.

[Firefox]: http://www.getfirefox.com/

Trusting a <acronym title="What You See Is What You Get">WYSIWYG</acronym> editor for <acronym title="Cascading Style Sheets">CSS</acronym> can be quite inaccurate and after viewing a site within [Firefox] and <acronym title="Internet Explorer">IE</acronym> it can be quite different than intended.  This leads <acronym title="Cascading Style Sheets">CSS</acronym> developers into the Edit&rarr;Save&rarr;Reload&rarr;repeat&#8617; cycle.

What if you could edit the <acronym title="Cascading Style Sheets">CSS</acronym> that [Firefox] is using without having to go through this cycle?

<!--more-->

[l]: http://www.themoleskin.com/archives/10-firefox-extensions-for-web-development/
[wde]: http://chrispederick.com/work/webdeveloper/

### Firefox and the Web Developer Extension

[Firefox]'s saving grace is the support for extensions.<sup id="fnr1">[1]</sup>  There's a few extensions that appear on just about everyone's top ten list of extensions for Firefox ([here's one list][l]).  Chris Pederick's [Web Developer Extension][wde] is one of those.  Use it to manipulate cookies, style sheets, forms, images as well as get helpful information about the web page.

### Editing <acronym title="Cascading Style Sheets">CSS</acronym>

[worthless]: http://www.contentwithstyle.co.uk/Articles/106/

The way I use <acronym title="Cascading Style Sheets">CSS</acronym> is by writing [semantic HTML][worthless] and then individually styling elements of my site.  Sure a lot can be done without having to look at a page.  If I want to mimic this site, I can try for:

	body {
		     color: white;
		background: #333;
	}
	
	h2 { 
		color: #f6861a; /* orange */
	}

Depending on how imaginative you are, you can get quite far without viewing a page.  Now, however, you can just open up your unstyled page, select `Edit CSS` under the `CSS` menu of the [Web Developer Extension][wde] and **see** the changes *as you make them*.  You can throw Dreamweaver out.  This is what you really need.

The greatest advantage of this is if you need to do pixel moving.  Let's say you have a complicated layout with absolutely positioned `div`s.  Now you can move them a pixel at a time until they look *just* right.

### Caveat

One major hang-up that I have with the `Edit CSS` feature is that it breaks relative references if you use `url()`.  For example.  Let's say you have a `/theme` folder for your web site's theme.  Under the `/theme` you have `theme.css` and `background.png`.  In `theme.css` you have:

	body {
		background: url(background.png);
	}

This will work fine, `url()` is relative to the file containing the <acronym title="Cascading Style Sheet">CSS</acronym>.  When you go to `Edit CSS`, however, the relativity is broken, because `Edit CSS` adds the <acronym title="Cascading Style Sheets">CSS</acronym> to the currently viewed document.  Therefore unless your <acronym title="Cascading Style Sheets">CSS</acronym> is in the same directory as your web page, anything relatively linked with `url()` is broken.

If this is a show stopper for you, use absolute references whenever possible.  Of course with themed sites, this is often not possible.  I'm sure someone clever can make some changes to this extension to fix it.


### What about Internet Explorer

This method does leave out <acronym title="Internet Explorer">IE</acronym>.  You will still need to do some back and forth when looking at <acronym title="Internet Explorer">IE</acronym>.  There are a few things that can alleviate this process.

* __Use standards compliance mode.__  Having a similar enough box-model to work with will eliminate most of the differences noted in <acronym title="Internet Explorer">IE</acronym> and [Firefox].
* __Know the problem areas.__  There's a few spots in <acronym title="Internet Explorer">IE</acronym> that are problem areas.  <acronym title="Portable Network Graphics">PNG</acronym> is one, negative margins are another.  If you know what they are, then when you use them you'll be aware that you'll need to adjust them for <acronym title="Internet Explorer">IE</acronym>.
* __If you use hacks use the same ones.__ If you use a "hack" to make <acronym title="Internet Explorer">IE</acronym> cooperate, try sticking to the same hack.  It makes your code easier to read, and consistancy makes life a bit easier.

If you do all that, you'll probably still save quite a bit of time in your <acronym title="Cascading Style Sheets">CSS</acronym> development.

### CSS Vista

[CSS Vista]: http://www.sitevista.com/cssvista/

[CSS Vista] is a promising product.  I tried it out recently (May 2006) and decided it isn't stable enough to be useful.  I would like it to be more integrated with <acronym title="Internet Explorer">IE</acronym> as well as be a lot faster.  I'm sure when they release 0.2, the stability will improve.  It may have been a fluke with my laptop as well.  Try it out, it might be able to be a good solution for Internet Explorer (and [Firefox]).  Unfortunately it's Windows only.

[1]: #fn1

<div id="footnotes">
	<hr />
	<ol>
		<li id="fn1">In a heartbeat I would switch to Camino or Safari if they supported such a wide array of extensions. <a href="#fnr1" class="footnoteBackLink"  title="Jump back to footnote 1 in the text.">&#8617;</a></li>
	</ol>
</div>
