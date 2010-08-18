---
layout: post
title: "Trimming Whitespace in Django Forms"
tags: [amo, mozilla, django]
published: true
time: 9:21AM
---
[d]: http://delicious.com/
[1]: http://code.djangoproject.com/ticket/6362
[h]: http://github.com/mozilla/happyforms
[p]: http://www.peterbe.com/plog/automatically-strip-whitespace-in-django-forms

I've been using frameworks for a number of years.  So I expect a lot of things
to happen "for free" in Django.  One is whitespace removal.  In [Delicious][d]
we had a lot of data in our database with leading and trailing whitespace.  On
the frontend we moved to symfony (actually ysymfony) and that prevented a lot
of this.

So I was quite surprised that [this is not the case with Django][1].  So I
decided we could solve this at the form level, and released a
[ridiculously simple library][h].  After some googling, I found that I was
[not the first to do this][p].

Feel free to use this, fork it, submit pull requests, etc.  I suspect in the
future we'll handle other global form filtering - like stripping high order
Unicode since MySQL is often not a fan.
