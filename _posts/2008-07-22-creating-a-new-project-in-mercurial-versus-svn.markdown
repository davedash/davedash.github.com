---
wordpress_id: 186
layout: post
title: Creating a new project in Mercurial versus SVN
wordpress_url: http://spindrop.us/?p=186
site: spindrop
---
One of the most annoying things about creating new SVN projects is the new project dance:

	$ svnadmin create $SVNREP_DIR/newproject
	$ svn mkdir -m "layout creation" file:///$SVNREP_DIR/newproject/trunk file:///$SVNREP_DIR/newproject/tags file:///$SVNREP_DIR/newproject/branches
	$ mkdir newproject
	$ cd newproject
	$ svn import -m "initial import" . file:///$SVNREP_DIR/newproject/trunk

Oh... yeah, no this isn't that bad.

It's this part that's bad:

	$ cd ..
	$ mv newproject newproject.tmp
	$ svn co file:///$SVNREP_DIR/newproject/trunk newproject
	$ # do sanity check here...
	$ rm -rf newproject.tmp

That's a lot of work, and it's actually hard to remember unless you do it a lot.

Here's the mercurial equivalent:

	$ mkdir -p newproject/trunk
	$ cd newproject
	$ mkdir branches tags
	$ hg init

That's it.  It's not apples to apples of course.  Mercurial keeps its repository locally, and does very simple push/pull commands for synchronization.  But the dreaded dance of removing a project after it's been imported and then checking out the project is really a peeve of mine.
