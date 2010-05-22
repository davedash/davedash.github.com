---
wordpress_id: 79
layout: post
title: Making anchor links smarter... and sexier
wordpress_url: http://spindrop.us/2007/02/14/making-anchor-links-smarter-and-sexier/
site: spindrop
---

[1]: #fn1
[2]: #fn2
[script.aculo.us]: http://script.aculo.us/
[prototype]: http://prototypejs.org/
[symfony]: http://symfony-project.com/

So I have a small bone to pick with Jacob Nielsen and his [opinion on within-page links](http://www.useit.com/alertbox/within_page_links.html) or anchor links<sup id="fnr1">.[1][]</sup>  There clearly is a benefit to not just linking to a specific page, but linking to a specific part of a page.

With a little help from [script.aculo.us][] we can spice up our anchor links by highlighting them as well as linking to them.

For this article we'll limit our scope to internal anchors only.<sup>[2][]</sup>  We'll write the code using the symfony framework and in straight up <acronym title="eXtended HypterText Markup Language">XHTML</acronym>.  This is really dirt simple and is more of a design pattern with an example than a tutorial.

Let's do the <acronym title="eXtended HypterText Markup Language">XHTML</acronym> first:

<div>
	
	<textarea name="code" class="xhtml" rows="10" cols="50">
	&lt;a href=&quot;#test&quot; onclick=&quot;new Effect.Highlight(&apos;test&apos;)&quot;&gt;this is a test&lt;/a&gt;
</textarea>

</div>

Yup, that's it... I told you it was dirt simple.  You just need to include the proper [prototype][] and [script.aculo.us][] libraries.

In [symfony][] we avoid repeating ourselves with a helper function:

<div>
	
<textarea name="code" class="php" rows="10" cols="50">
	function link_to_anchor($text, $target)
	{
		return link_to($text, '#'.$target, 'onclick='.visual_effect('highlight',$target);
	}
</textarea>

</div>

and call it by doing:

<div>
	
	<textarea name="code" class="php" rows="10" cols="50">
	echo link_to_anchor('this is a test', 'test');
	</textarea>

</div>

That's it.


<div class="footnotes">
	<hr/>
	<ol>
		<li id="fn1">Jacob Nielsen is an easy target. <a href="#fnr1" class="footnoteBackLink"  title="Jump back to footnote 1 in the text.">&#8617;</a></li>
		
		<li id="fn2">Anchors on other pages are equally useful.  To implement that, you need to have an event listener to examine the URL for an anchor and appropriately highlight the correct element. <a href="#fnr2" class="footnoteBackLink"  title="Jump back to footnote 2 in the text.">&#8617;</a></li>
	</ol>
</div>
