---
wordpress_id: 323
layout: post
title: "Django: Model Inheritance or Related Tables wrt AMO"
wordpress_url: http://spindrop.us/?p=323
site: spindrop
tags: [spindrop, django, mozilla, amo, addons.mozilla.org]
---
[amo]: http://addons.mozilla.org
[z]: http://github.com/jbalogh/zamboni
[1]: http://scottbarnham.com/blog/2008/08/21/extending-the-django-user-model-with-inheritance/
[2]: http://www.b-list.org/weblog/2007/feb/20/about-model-subclassing/

When I attended DjangoCon this year, I lamented that our flagship web property was difficult to test, and not fun to develop.  I figured DjangoCon was a way to placate me, and Django might mean something for some of the smaller projects at Mozilla.  However, Wil Clouser, our lead web developer, [announced development changes](http://micropipes.com/blog/2009/11/17/amo-development-changes-in-2010/) for [addons.mozilla.org][amo] (AMO) that says we'll be moving to Django.  

Wil was open to Django and knew that's what we in the dev team wanted.  Jeff spawned our foray into a new AMO with [Zamboni][z].  I've been working on some grunt-work tasks inside and outside of Django.

One of those tasks is building a transparent layer in Django to keep users logged in from our PHP-based site.  That kind of problem almost immediately forces you to ask one of the most fundamental questions you ask when using any framework:

> How much do I change my app, in order to accommodate the framework?

<!--more-->

More specifically:

> Should I use the `django.contrib.auth` User module, and to what extent?

The more we looked into what features of Django we might want to use, `django.contrib.auth` was heavily tied into other things we wanted, so it made sense for us to use it.  The next question is whether we try the [inheritance approach][1] or do we treat our legacy users table as a sort of User Profile and utilize the User module using the [related table approach][2]?

Using model-inheritance seems real nice, because we can pretend that our legacy user is the same thing as a `djaango.contrib.auth` User - but this isn't true:

Looking at our `users` table more closely:

	mysql> explain users;
	+-------------------------+---------------------+------+-----+---------------------+----------------+
	| Field                   | Type                | Null | Key | Default             | Extra          |
	+-------------------------+---------------------+------+-----+---------------------+----------------+
	| id                      | int(11) unsigned    | NO   | PRI | NULL                | auto_increment |
	| email                   | varchar(255)        | YES  | UNI | NULL                |                |
	| password                | varchar(255)        | NO   |     |                     |                |
	| firstname               | varchar(255)        | NO   |     |                     |                |
	| lastname                | varchar(255)        | NO   |     |                     |                |
	| nickname                | varchar(255)        | YES  | MUL | NULL                |                |
	| bio                     | int(11) unsigned    | YES  | MUL | NULL                |                |
	| emailhidden             | tinyint(1) unsigned | NO   |     | 0                   |                |
	| sandboxshown            | tinyint(1) unsigned | NO   |     | 0                   |                |
	| homepage                | varchar(255)        | YES  |     | NULL                |                |
	| display_collections     | tinyint(1) unsigned | NO   |     | 0                   |                |
	| display_collections_fav | tinyint(1) unsigned | NO   |     | 0                   |                |
	| confirmationcode        | varchar(255)        | NO   |     |                     |                |
	| resetcode               | varchar(255)        | NO   |     |                     |                |
	| resetcode_expires       | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
	| notifycompat            | tinyint(1) unsigned | NO   | MUL | 1                   |                |
	| notifyevents            | tinyint(1) unsigned | NO   | MUL | 1                   |                |
	| deleted                 | tinyint(1)          | YES  |     | 0                   |                |
	| created                 | datetime            | NO   | MUL | 0000-00-00 00:00:00 |                |
	| modified                | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
	| notes                   | text                | YES  |     | NULL                |                |
	| location                | varchar(255)        | NO   |     |                     |                |
	| occupation              | varchar(255)        | NO   |     |                     |                |
	| picture_type            | varchar(25)         | NO   |     |                     |                |
	| averagerating           | varchar(255)        | YES  |     | NULL                |                |
	+-------------------------+---------------------+------+-----+---------------------+----------------+

You can very easily argue that this is a profile table, which happens to have credential information thrown in.

I can see overtime, I'll just struggle to keep our legacy User to act like a Django User, whereas a UserProfile is fairly standard.

Had I been writing this app from scratch, I would have chosen the UserProfile route.  This is extra data which takes up a lot of space, and changes far more often than user credentials.  Changing 4M+ rows sucks, by making users our UserProfile table, any changes to that table, don't tie up the table used for sign-ins.

I'm curious what other people who port their apps to Django have done.
