---
layout: post
title: "So your Wordpress has been hacked"
tags: [wordpress, webdev, hacks, mozilla]
---

Last week, someone informed me that my blog had been hacked:

<p>
    <a href="http://www.flickr.com/photos/davedash/4621504223/"
            title="My blog got hacked by davedash, on Flickr">
    <img src="http://farm5.static.flickr.com/4063/4621504223_210d430c1f_m.jpg"
        width="240" height="111" alt="My blog got hacked" /></a>
</p>

I'm not quite sure what the vector was, Wordpress wasn't very secure and I
didn't take too many measures to harden it.  A coworker of mine (on our security
team) decided it might be fun to have a look at the infected Wordpress
Installation)

### Here's how the hack works

* Your blog appears normal to you and your visitors.
* Some rogue PHP code detects if Google is crawling your site and modifies
the text and links so it looks like your website is a viagra phramacy.
* The links go to other infected blogs and thus builds up page rank for this
ring of blogs.  So the upside is that you're blog may be a top result... for
*VIAGRA*.

### Prevention

Here's some tips for prevention, but you can find a lot more by googling for
Wordpress hacks.  My solutions are more technical:

* Don't use Wordpress - I recently switched to Jekyll since it was conceptually
easier to understand, and it's hacker-friendly.
* Remove all users other than your own.
* Change your password.
* Check your code into git so you can see what files have changed.
* Prevent Wordpress from writing to your webroot.

### Restoration

Here's what you'll need to do to de-spam yourself.

1.  Verify that you are still spammed by using
Google Webmaster Tools|Labs|Fetch as Googlebot.
2.  Backup your blog and database.
3.  Move your wordpress installation to a new directory.
4.  Install Wordpress from scratch.
5.  Remove all users except for yourself.
6.  Change your password.
7.  Copy your theme to your new installation.
8.  Install *only* the plugins you need.

By step 4 you should be able to verify using *Fetch as Googlebot*
that your website is no longer an Online Pharmacy.

Good luck.

