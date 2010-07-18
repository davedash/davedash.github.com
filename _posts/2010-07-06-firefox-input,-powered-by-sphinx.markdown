---
layout: post
title: Firefox Input, powered by Sphinx
tags: [mozilla, firefox, sphinx, search]
published: true
time: 9:02AM
---
[fi]: http://aakash.doesthings.com/2010/06/25/hi-my-name-is-firefox-input/
[amo]: https://addons.mozilla.org/en-US/firefox/
[sumo]: http://support.mozilla.com/en-US/kb/
[dj]: http://fredericiana.com/2010/06/23/under-the-hood-of-firefox-input/
[n]: /tag/baby
[z]: http://github.com/jbalogh/zamboni/
[fg]: http://github.com/fwenzel/reporter
[prod]: http://input.mozilla.com/

Thursday, I decided to take a half-day for my sanity, but saw an email about
how Whoosh wasn't going to cut it for [Firefox Input][fi].  I was CC'd about
this and there was mention that Sphinx might be possible.

Sphinx is my hammer, and everything is a nail.  So I said, let's do this.
That translated into me spending my weekend, soothing [my newborn][n] and
working on Sphinx.  Luckily this was easy, since [AMO][amo] and [SUMO][sumo]
are both running Sphinx in a similar [Django environment][dj].

In order to move quickly, I copied code from the [Zamboni][z] project to
[Firefox Input][fg].  Even our deployment into staging and production wasn't
done by our usual "Sphinx guy" in IT.  Ultimately, everything landed in place.

So [try it out][prod] and file bugs or let me know if searches don't go as
planned.
