---
wordpress_id: 299
layout: post
title: git svn rebase... forever?
wordpress_url: http://spindrop.us/?p=299
site: spindrop
tags: [spindrop, svn, mozilla, git, git-svn]
---
While working on [addons.mozilla.org](http://addons.mozilla.org/) I ran into an issue of `git svn rebase` continually asking me to merge a file, over and over.

I had a branch open for a bug.  In that branch I wrote a library.  While that bug was under review, I had to use that library in a new branch for another bug - and had to develop on it a bit.

	$ git co -b bug1 master
	$ vi libs/mylib.php # make the lib
	$ git add .
	$ git commit -m "my new lib"
	$ git checkout -b bug2 master
	$ git checkout bug1 libs/mylib.php # copies this file from one branch to the next
	$ git commit -m "lib copied over"
	$ vi libs/mylib.php # hack on the lib 
	$ git commit -m "awesomized lib"
	$ git svn dcommit # push it up
	$ git checkout bug1
	$ git svn rebase #... oh shit

So the rebase was happening.  This is git trying to merge your changes in bug1 and bug2 and play them together in realtime nicely, asking you each step of the way to merge things manually.  I thought something weird was happening since "libs/mylib.php" kept needing manual merging.  Then I noticed that git is applying a series of patches, and that eventually this will resolve and your site will be rebased.

Don't lose hope, `git svn rebase` will finish.
