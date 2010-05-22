---
wordpress_id: 188
layout: post
title: postgresql and python in osx
wordpress_url: http://spindrop.us/?p=188
site: spindrop
tags: [programming, python, osx, postgresql]
---
I want to start dabbling with postgreSQL on OS X.  After several SVN checkouts, binary packages, etc, I've realize the easiest path to success is just installing from fink unstable.

Running:

	fink install psycopg2-py2.5

will get you everything you need, `python`, the `pyscopg2` driver and even `postgresql`.  

Unfortunately I had MacPython binary and a postgres binary which I couldn't easily install (and if anybody knows how to uninstall at least the former, I'm all ears).  I decided to just merge the site-packages for both the fink installed python2.5 and the MacPython:

	$ rm -rf /Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/site-packages/
	$ ln -s /sw/lib/python2.5/site-packages /Library/Frameworks/Python.framework/Versions/2.5/lib/python2.5/

Now if I installed more python packages via fink they will work in MacPython.
