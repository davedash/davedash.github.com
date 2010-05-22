---
wordpress_id: 121
layout: post
title: "symfonyCamp "
wordpress_url: http://spindrop.us/2007/09/11/symfonycamp/
site: spindrop
---
[tags]symfony, symfonyCamp, sensio, dop, zend search lucene, zsl[/tags]

[sc]: http://symfonycamp.com/
[dop]: http://dop.nu/
[fp]: http://www.symfony-project.com/blog/2007/09/07/symfony-camp
[fl]: http://www.tempus-vivit.net/

<span class="photoright">
![Tents](http://farm2.static.flickr.com/1096/1354502708_97f225a078_m.jpg?v=s)
</span>


Well Katie and I are back from [symfonyCamp][sc] and it was great.  I opted to socialize on the business day, except to hear Fabien Potencier's brief overview of what's to come in symfony 1.1/2.0.

I personally know only a handful of adept symfony developers, so going to camp it was nice to see 50 people or so who knew symfony to varying degrees.  I am a fan of the small successes, such as [Fabian Lange's historical reenactment site][fl] which paid the way for two developers to attend the conference.

One of the most interesting talks to hear was Fabien's overview of symfony 2.0.  It was a 12-step process from going to vanilla PHP to building a strong framework in about 200 lines.  A leaner more robust symfony sounds very appealing, it's also what appeals to me about being a developer.  Every developer builds off of existing technologies and is able to create something great.  I frequently have to dig into the symfony core code to see how things "really" work and everything is simple, easy to follow building blocks.  Effectively giving us a nice framework.  symfony 2.0 seems to be a leaner more flexible framework.

<span class="photoleft">
![Zend talk](http://farm2.static.flickr.com/1283/1341189131_1bfe60a945_m.jpg)
</span>

Later I spoke on Zend Search Lucene as well as Ajax.  Both are somewhat difficult to speak on for 45 minutes.  Zend Search Lucene really only takes 15 minutes to explain, and maybe just as long to implement.  Sure it can be tweaked quite a bit, but it's straightforward - that's the point.  

Ajax on the other hand is hard to explain in terms of symfony.  Sure there's a helper layer, but the Javascript layer is very independent of the PHP layer.  Anything can support Ajax.  So I tried to cover not just the standard helpers, but show a few demos and how easy it is with the helper system.  Unfortunately I don't really code this way, I try to use UJS and the jQuery plugins with new work, but that would move the talk to a more advanced topic.

The next day we ended up cleaning up the symfony project.  We split into teams to take care of some house-work.  Some people cleaned up the wiki.  Some cleaned up tickets, some wrote new modules for the site.  Our team worked on plugins and it went rather well.  We closed a number of tickets, created a good deal of patches (which I have yet to apply), but overall the plugins are all a bit better.

Overall everything was great.  [Dutch Open Projects][dop] was great, especially Stefan for arranging so much, Guido for making sure everyone was comfortable and Floris for the great food.

You can also read [Fabien's overview][fp] of the camp.
