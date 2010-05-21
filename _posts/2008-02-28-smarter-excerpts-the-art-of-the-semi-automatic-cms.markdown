--- 
wordpress_id: 171
layout: post
title: "Smarter excerpts: the art of the semi-automatic CMS"
wordpress_url: http://spindrop.us/2008/02/28/smarter-excerpts-the-art-of-the-semi-automatic-cms/
---
I was browsing the [TED](http://ted.com/) site, since it's all up in my blogospheres and ran across this:

<img src="http://spindrop.us/wp-content/uploads/2008/02/picture-1.png" alt="Picture 1.png" border="0" width="689" height="340" />

If you look at the excerpts, they are piss poor descriptions:

	Frans Lanting is one of the greatest nature p...





<!--more-->




Nature p-what?  Nature painter?  Nature preserver?  If you click around enough... the answer is nature photographer.  Many of the excerpts failed at giving me any indication of who these people are or even enticing me to find out.  I am a web 2.0 person, if I have to click on a link and load a new page, then it better be good.  When I'm doing an information binge, I am not going to have that level of patience.

One day at del.icio.us I decided to test the limits of every profile field... and I learned that every now and then you *do* need to truncate user generated content.

This page however, is trusted users who have edited structured content (to borrow [a term from the Django Book](http://www.djangobook.com/en/1.0/chapter17/)).  That means, that someone had to enter in a description for this person.  Someone who is trusted at TED.  Chances are the page was rendered to trim the excerpt at 46 characters.

There's two easy solutions to this:

1. DHTML

    This remaining excerpt could have been hidden away, and a button that said "show all" or "expand" (or whatever is the usable phrase/icon) could show the full except.  This prevents me from having to jump around.

2. Use Semi-Automatic excerpts

	We are talking about "trusted users" meaning, we can trust them to do things that humans do better than machines (there's my del.icio.us humans-do-some-things-better mentality).  When they enter the description for a person, their administration interface should be able to suggest an excerpt and they, the "trusted user" should be able to make adjustments or tweaks.

The former solution is far easier, but if you're scanning a site, especially one as extensive as [TED's speakers listing](http://www.ted.com/index.php/speakers), the last thing you want to do is click "expand" buttons everywhere to read everything.  The latter solution is smarter.  Of course, the problem could also be solved by upping the 46 character limit, but not everything should be fully automated.
