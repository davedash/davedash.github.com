---
wordpress_id: 113
layout: post
title: FBML and embedded CMS
wordpress_url: http://spindrop.us/2007/08/04/fbml-and-embedded-cms/
site: spindrop
---
[tags]fbml, css, reviewsby.us, partials, symfony, sfFacebookPlatformPlugin[/tags]

One problem of going the FBML route<sup id="#fbmlcss_fnr_1">[1](#fbmlcss_fn_1)</sup> is CSS styles.  You can't link to external style sheets so you need to embed everything.

I took the liberty of using a partial that contains all the useful CSS that I use in our app.  Now we can just embed it in our layout by doing:

	<?php include_partial('sfFacebook/css');?>

The following classes are useful:

* `.app_content` is the div surrounding the main content of the page.  It gives the canvas some padding (actually it gives itself some margin as not to butt-up against the canvas.
* `.box` this defines the classic facebook box with a dark blue border at the top and with headers that have the lighter blue background and dark blue text.
* `.box .header` the header for the box described above.  Use an `h2` for the title.
* `.box .content` the main content section of a box, has a bit of padding.




<div class="footnotes">
<ol>
<li id="fbmlcss_fn_1">I'm not completely convinced that the
<a href="http://reviewsby.us/">reviewsby.us</a> app for facebook should be using FBML.

<a href="#fbmlcss_fnr_1" class="footnoteBackLink"  title="Jump back to footnote  in the text.">&#8617;</a>
</li>
</ol>
</div>
