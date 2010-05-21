--- 
wordpress_id: 78
layout: post
title: Semantic (X)HTML is easy
wordpress_url: http://spindrop.us/2007/02/12/semantic-xhtml-is-easy/
---
There's a flippant article, [CSS is Worthless](http://www.contentwithstyle.co.uk/Articles/106/css-is-worthless/) from Mike Stenhouse that alludes to semantic HTML.

There's a number of emerging trends on the web that are leading to more and more people following semantic HTML.  But what is it?

Semantic HTML is writing HTML in such a way that each tag tells something about the text that it surrounds.  E.g. "&lt;em&gt;example&lt;/em&gt;" means the word "example" deserves emphasis --- not necessarily that it needs to be italicized.  Conversely tags like &lt;i/&gt; and &lt;b/&gt; traditionally imply that text should be styled in a specific manner (italicized and bolded respectively).

Stylistic tags couple style and semantics together --- changing semantics means changing style and vice versa.  Semantic-only tags decouple style from semantics making changes to style a lot easier.  This makes your data, your HTML, much more robust.  You might write for a blog, and now the styling that you like for your personal site is decoupled and someone else who might have a different interpretation of what is a heading or what is strongly emphasized can make their own go at stylizing your text.

So get a good understanding of what type of data the text in your documents represent.  Add appropriate tags to mark them up.  Then style with <acronym title="cascading style sheets">CSS</acronym> to your heart's content.  I highly recommend following yahoo's approach of using a file like [reset.css](http://developer.yahoo.com/yui/reset/) which normalizes all your tags to have the same width and appearance.  This is a clean slate to work with and encourages the use of semantic HTML. 
