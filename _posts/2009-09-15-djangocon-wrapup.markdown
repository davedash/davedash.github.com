---
wordpress_id: 311
layout: post
title: DjangoCon wrapup
wordpress_url: http://spindrop.us/?p=311
site: spindrop
tags: [spindrop, django, mozilla, djangocon]
---
I went to [DjangoCon](http://djangocon.org/) this past week for work.  Django is one of my favorite frameworks.  I dropped PHP and the symfony framework to learn python and Django and I haven't looked back.  I think for Mozilla's webdev team it would be the framework of choice.  We have 100s of sites in many frameworks, but not a lot of resuability.  Django apps are built to built to be reusable.  If you build correctly you don't have to refactor, it's already done.<!--more-->

Here's a collection of notes I collected through the conference.

### Day one

#### Keynote - Avi Bryant
> Frameworks lock us into RDBMS = bad

This keynote mentioned the limits of modern frameworks and modern web development.  Essentially frameworks are great for getting started, but as a site grows, the framework gets replaced little by little.  Sometimes it can get in the way - such as with limitation of database choices.

#### UR doing it wrong - James Bennet

James outlined a few key problems that many Django developers run into:

* learning python as you go
     * doesn't work unless you know some programming upfront
     * do the python tutorial
     * read python in a nutshell or dive into python

* Things you should know:
	* subclasses
	* super()
	* slides went too fast... hopefully they'll be posted

All in all RTFM for python and Django :)

Learn about other py packages... like twisted.  If Twisted Matrix was implemented in Ruby it would be advertised as the second coming of Christ. 

Bennet's Django App review smoketests:

* installable via pip, easy_install or setup.py
	* read distutils-guide
	* stay away from setuptools
* have a README
* INSTALL file list deps
* Write DOCUMENTATION
	* use sphinx.pocoo.org
	* store it in your package *and* upload package docs
* LICENSE (most Django apps use BSD)
* Write unit tests
* django-lint - to look over code (like pep8.py)

pro-django is a decent book, but not written by Bennet.

#### Testing - Eric Holscher

* Django 1.1 encourages you to test by auto-creating tests.py.
* Support for:
	* Unittests
	* Doctest
	* Tests done in a db transacation
* Test Driven Documentation (TDD + DDD)
* Doctest
	* easy
	* can't use PDB
	* Hides certain failures
* Unittests via Django TestCase
	* XUnit
	* setup/Teardown
	* adds db fixtures
	* assertions
	* mail testing/inbox testing
	* url testing
* TestCase
	* Browserless Request/Response testing
	* Similar to sfBrowser in symfony
* Google Summer of Code (for Django 1.2)
	* Coverage reports!
* I need to learn PDB

#### Deploying Django - 

Run mod_wsgi in daemon mode.

### Day 2

#### [Keynote - Ian Bicking](http://blog.ianbicking.org/2009/09/10/a-new-self-definition-for-foss/)

GNU Manifest:
>  I consider that the golden rule requires that if I like a program I must share it with other people who like it. Software sellers want to divide the users and conquer them, making each user agree not to share with others. I refuse to break solidarity with other users in this way. I cannot in good conscience sign a nondisclosure agreement or a software license agreement. ...

> So that I can continue to use computers without dishonor, I have decided to put together a sufficient body of free software so that I will be able to get along without any software that is not free. 

* GNU manifesto was the idea of sharing software amongst friends
* GNU has purpose - BSD, etc is just a rule - free to share
* Free is not just the absense of copyright
* Free is not a reaction to existing rules, but a golden rule
* Not just a fight against MS
* Need to find morality (the why) within the practical (the law, or what you can do)
* Open sourcing closed source code isn't building open source
* This might apply to Mozilla... as webkit has taken off more than Gecko.
* Open source is person to person not company to company - despite sponsorship.

### Using Django in Non-standard ways - Eric Florenzano

* Django loosely coupled
* Replace templating with Jinja 2
* Copy Django methods into djangoext to easily customize Django behavior
* Not using django.contrib.auth
	* reasons: writing a fb app - no auth needed
	* no shoehorning needed - saves time - less overhead
* skip the orm?
	* legacy dbs
	* non standard or db (or non-relational database)
	* no database
* wsgi middleware has some cool shit
	* repose.bitblt: autoscales images
	* repose.squeeze: will concat js/css on the fly based on statistical analysis
* non standard Django based apps
	* YARDBird - IRCBot framework
	* djng micro framework
	* Jngo- singlefile cms
* using admin in a nonstandard way is hard/impossible coupled with ORM and auth

#### Real-time web and other Buzzwords - Chris Wanstrath

* more than just getting your rss feeds faster
* push vs. pull
* 1 persisting connection vs polling
* comet/flash-xml/or html5 web socket
* orbitted - open source python comet server
* zeddicus - does the business logic
* orbitted has its own js libs - its a simple port/socket thing for your server code to deal with - not request/response.
* all connections are persisting browser/orbitted orbitted/zeddicus
* You can even use orbitted to connect straight to IRC and write a client in JS
* Jetty also is good for comet

Also:
* see webhooks 
* see pubsubhubub


#### [Pluggable, Reusable Django Apps: A Use Case and Proposed Solution](http://www.slideshare.net/nowells/djangocon-09-presentation-pluggable-applications) - Shawn Rider and Nowell Strite

* PBS moved from perl to django - build a lot of reusable apps
* convincing your superiors
	* need a good story - 
	* existing base of python helped
	* With Django easy to do things right without doing things slow
	* be really good...
* built a lot of apps to be very reusable, and pluggable based on requirements PBS had

### Day 3

#### [Keynote](http://www.slideshare.net/twleung/djangocon-2009-keynote) - Ted Leung - Sun

* Django jobs are a growing market
* Preferred by startups
* Bespin/wave - cool
* APIs are big... still
* Physically impossible to create purely server-side interactions that are usable enough - rely on rest/comet/ajax/etc to bridge gap

#### [Scaling Django](http://immike.net/files/scaling_django_dc09.pdf) Mike Malone

* MM from Pownce (now sixapart)
* Slides started out as "Building Scalable Web Applications"
* Django didn't get in the way too much when it came to scaling
* Django had tons of caching support
* Cached objects by hand (memcached) and object ID lists
* Use memache for sessions too
* use signals to signal cache invalidation
* race conditions...
* Queue shit... gearman, rabbit mq, etc.
* Memecached incr/decr operators are awesome
* See gh/mmalone/django-caching
* See gh:.../django-multidb
* to combat slavelag use a memcache key to alternate between master or slave

#### [Gearman - working later](http://heisel.org/blog/2009/09/11/gearman/) - Chris Heisel

* Gearman - a work later alt to rabbit mq
* Makes the most sense for something like cesium, with a bazillion worker <strike>bees</strike> foxes feeding off a single queue

Also at the con, I talked to someone about rebuilding large apps... and they took a PHP app and used URL rewriting to and a lot of PHP/Python glue code to build a seamless transitory app.  The rule is, all new functionality was done up in python while the old app was in maintenance mode.


More talks [here](http://djangocon.pbworks.com/Slides)!

