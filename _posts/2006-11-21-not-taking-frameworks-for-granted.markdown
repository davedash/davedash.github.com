--- 
wordpress_id: 75
layout: post
title: Not taking frameworks for granted
wordpress_url: http://spindrop.us/2006/11/21/not-taking-frameworks-for-granted/
---
One of my clients approached me with a relatively easy project.  She gave me a log file of PHP errors and I was supposed to fix her scripts.  I fixed about 100+ different errors in a few hours.  It was fairly straightforward.

Throughout the site I could understand the previous developer and the choices he or she made for better or worse.  It did look like a struggle however.

<!--more-->

Ultimately it felt that there were some fairly simple things that each script needed to do, but each task was a challenge.  Validating forms, storing data across pages, decorating the site, interacting with the database.  Everything seemed very kludged together.

I realized that this is exactly how I used to write code, sure... my way of course was better and more logical, yada, yada, yada... but ultimately I was there before.

My client noted that these scripts were made from another contract programmer, and then a light-bulb went on... frameworks (whether it be [symfony][], <acronym title="Ruby On Rails">ROR</acronym>, Django, CakePHP, etc) help iron out and standardize these tasks.

Since I know [symfony][] best, I'll cover what I think could have helped in this last project.  I'm sure other major frameworks have their equivalents.

* **Form validation**: [symfony][] lets you define form validation in a very simple manner.  The validation logic is also separate from the rest of the code.
* **Storing Data**: Without a framework, you generally have to rely on the `$_SESSION` array in PHP.  While very useful and easy to use, storing parameters and attributes to a user object is done a lot more cleanly. 
* **decorating the site**: My biggest problem was with each page I had,, I used to have to call headers, sidebars, etc, etc.  [symfony][]'s layout system was a boon.  I had a common layout for all pages (maybe a few alternates) and hooks inside them if they needed to be adjusted.  Then the various actions had their own seperate templates that were injected into the common layout.  It made adding new pages easy, since I didn't need to remember `header()` and `footer()` functions for each and every page.
* **Interacting with the database**: [I've covered before the benefits of ORM][s].

Not only do the bulk of these problems disappear with a framework, a lot of the difficulties of switching developers melt away.  If you tell me, a developer, that I'm walking into a project made with a framework, I can learn about the framework and be able to understand its ins and outs.  

If you just tell me it's written in PHP, chances are I'm going to want to do things my own way.  It's hard to understand the logic that another programmer was using so we fall back to standards whether they are your own or borrowed.

When we use a framework, we can find some mutually agreed upon standards and usually people who specialize in that framework and are willing to help.  So my advice: stick to frameworks.  The coding style will be no worse than the whims of a programmer, but at best it'll be something that anyone can pick up.  The general case is that even a bad coder can only do so much damage within a framework.  The bullet points I covered above will cut down on development time tremendously.


[symfony]: http://symfony-project.com/
[s]: http://spindrop.us/2006/08/07/how-object-relational-mapping-saves-time-and-makes-your-code-sexy/
