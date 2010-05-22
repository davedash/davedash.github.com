---
wordpress_id: 189
layout: post
title: Why code rewrites are often coupled with redesigns
wordpress_url: http://spindrop.us/?p=189
site: spindrop
tags: [programming, symfony, django, del.icio.us]
---
I've done some rewrites of code, and they usually are coupled with redesigns.

Redesigns and rewrites are tricky.  With web sites existing users tend to prefer incremental changes with each.  Changing a design element or a feature are pretty much equivalent when its done incrementally.

Usually small changes are like surgery.  You make a small change, you possibly announce it, and people look at it and usually say yes, this change is better.  But mostly a small change can go unnoticed.

Tiny atomic changes are nice and they improve the product.

A rewrite of code however is a discrete change.  They take forever.  Second system and all that.  They inevitably involve a redesign as well.  They tend to be received with mixed reviews.

Generally a design of a site is grafted onto code.  Sometimes by templating languages, sometimes in a tightly coupled system.  In either case there's usually two options:

1. Make a faithful port of the design.
2. Redesign

The latter is generally preferred since this saves a lot of time.  Generally there are bugs with a design, and there is a design backlog.   A faithful port of the design would mean porting every broken HTML code, every non user-friendly element, etc.

Unfortunately this leaves web developers with a scary situation: Launching a product which changes peoples functional and UI experience.

The good thing is redesigns usually mean evolutionary leaps.  Meaning, iterations can happen faster, both in design and functionality.  We can easily please new customers, and we can quickly bring current customers up to speed.

In my spare time, I've been rewriting code that I wrote in symfony (PHP) into django (python).  It's a tiresome long process that can easily kill a side project.
