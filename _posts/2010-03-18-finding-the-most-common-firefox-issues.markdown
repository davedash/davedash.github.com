--- 
wordpress_id: 354
layout: post
title: Finding the most common Firefox issues
wordpress_url: http://spindrop.us/?p=354
---
[f]: http://support.mozilla.com/en-US/kb/
[g]: http://github.com/davedash/SUMO-issues

Cheng Wang of the Mozilla Support team, a few months back, decided to present on some design ideas for [Firefox Support][f].  One of the issues he noted was that there are a lot of repeated issues and that it would be useful to group them.  Grouping them lets you see how often something occurs, and secondly let's you see how urgent it might be.

Luckily grouping and clustering text is something computers can do.  So I wrote [this utility][g] that does just that.

I ran this script over a sampling of data from the last week:

* Firefox won't start after update. (65 related issues)
   *  5.6:  Firefox updated, Gmail not delivering mails
   *  5.6:  How to change My Profile when Firefox won't load?
   *  7.5:  Once I close firefox, cannot start firefox again except system restart
   *  5.6:  When intalling updates Firefox uninstalls itself
   *  16.8:  firefox won't start after update 3.6
   *  11.2:  Upgraded to Firefox 3.6 and now it won't start
   *  14.9:  Firefox won't start with most extensions
* How do I add a bookmark to more than one folder? (64 related issues)
   *  8.9:  How do I get my bookmarks on the bookmarks toolbar to show up as an icon only with no text?
   *  7.5:  Bookmarks lost after upgrade and cannot save new bookmarks
   *  7.5:  why do i have to add the .com now to addy's?
   *  8.7:  When I open sidebar to edit bookmarks, I only see the folder for Bookmarks Toolbar. I do not see a folder just called Bookmarks nor do I see my list of bookmarks, that separately appear under bookmarks menu at top of screen
   *  7.5:  All my impoted bookmarks go to the same webpage
* How do I remove the \ask toolbar\"?" (50 related issues)
   *  14.9:  How do I remove an unwanted toolbar?
   *  5.6:  how to remove temporary video files from computer
   *  7.5:  I have no Toolbars or searchbar and i cant bring them back
   *  7.5:  nowhere says how to REMOVE a toolbar - only how to add or modify one
* not able to open youtube videos (45 related issues)
   *  5.6:  Cannot open bookmark/history sidebar
   *  5.6:  After working well for years Firefox will now not open
   *  6.7:  opening bookmarks do not open in new tab
   *  5.6:  I can't watch videos on youtube with firefox, but on internet explorer i can
* I cannot download Firefox 3.6.  I've tried erasing the download file.  I cannot get beyond logging out of Firefox. (44 related issues)
   *  8.4:  when downloading files firefox download manager will freeze and i will have to start over the file download
   *  5.6:  Firefox will not let me download anything! Can someone help?
   *  6.3:  cannot download epixHD.com: not compatible with firefox 3.6
   *  5.0:  Several tabs are coming up when i try to downloads things
   *  5.0:  Firefox wont open since I downloaded the 3.6 update.

The number on the right of the related issue is a score of how strongly it relates to the main issue.

The full sample is 352 clusters from an original 3000+ issues.  That's a lot less stuff to go through.  We can tune this to have either less clusters, and more related issues in a cluster, or we can make more clusters of issues and that might result in more accuracy.

Despite the inaccuracy of clustering we can make some general observations:

* Firefox not starting is a big issue.
* Bookmarks are either confusing or broken.
* People don't like toolbars
* Opening things is hard
* Downloading things or Firefox is hard

Hopefully we can fine tune these reports and have them run regularly... maybe automatically posting to Tumblr?
