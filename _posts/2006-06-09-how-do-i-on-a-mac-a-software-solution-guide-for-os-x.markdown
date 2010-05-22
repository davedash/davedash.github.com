---
wordpress_id: 39
layout: post
title: How do I... on a Mac?  A software solution guide for OS X
wordpress_url: http://spindrop.us/2006/06/09/how-do-i-on-a-mac-a-software-solution-guide-for-os-x
site: spindrop
tags: [reviewsby.us]
---
[ff]: http://www.econsultant.com/i-want-firefox-extension/index.html
[os x]: http://apple.com/macosx/

I've been doing web development as well as other "computer stuff" with Powerbooks for four years.  I'm currently in a happy place where I've got a nice set of tools with which I can use to accomplish many tasks.

This guide was inspired by [this Firefox Extension guide][ff].  This guide covers how I tackle tasks in [OS X] and how I've seen others tackle tasks.  I plan to regularly update this piece (software guides can get stale fast) and will incorporate suggestions left in the comments.

Hopefully people who are wondering about making the switch from Linux or whatever to [OS X] will find this guide as reassuring and helpful.  There's quite a bit more out there than what I have listed, but if I attempted to list every option, I'd never be able to finish this guide.

<!--more-->

* [Internet](#internet)
* [Programming](2/)
* [Multimedia](3)
* [Productivity](4)

<h3 id="internet">Internet: How do I...</h3>

*	#### Surf the web? ####

	*	##### [Camino]

		[Camino] combines the Mozilla Gecko browser with Apple User Interface.  If [Firefox]'s lack of <acronym title="User Interface">UI</acronym> integration bothers you (e.g. lack of services menu support), try [Camino].  Out of the box it blocks advertisements and popups.  It does lack the extensibility that [Firefox] has, but otherwise is a worthy browser.  It's fast and it gets the job done.

	*	##### [Firefox]

		I used to prefer [Firefox], despite its shortcomings.  There are [so many extensions][ff] available that no other browser comes close.  When I'm developing websites this **must** be open with [Firebug] and the [Web Developer Extension][wde]

	*	##### [Safari]

		This is a [Apple]'s very own browser based on [KHTML][] ([Konqueror], etc).  I don't use this myself, but I do use other [Apple WebKit][webkit] based applications.  It is elegant and integrates well with the rest of the OS.

[Camino]: http://www.caminobrowser.org/
[Firefox]: http://getfirefox.com/
[Firebug]: https://addons.mozilla.org/firefox/1843/
[wde]: http://chrispederick.com/work/webdeveloper/
[Safari]: http://www.apple.com/macosx/features/safari/
[Apple]: http://www.apple.com/
[KHTML]: http://www.konqueror.org/features/browser.php
[Konqueror]: http://www.konqueror.org/
[WebKit]: http://webkit.opendarwin.org/

*	#### Check my Email

	*	##### Gmail

		[Gmail] might be a web-app, but it works rather well as an email solution.  It can even integrate into [OS X] with the [GMail Notifier][gn].

[Gmail]: https://mail.google.com/mail
[gn]: http://mail.google.com/mail/help/notifier/

	*	##### Mail.app

		[Apple]'s built in Mail.app is a good choice if web-mail isn't an option.  It integrates well with the Address Book and even iChat.

*	#### Upload my Files

	[Transmit] does <acronym title="File Transfer Protocol">FTP</acronym> and <acronym title="Secure File Transfer Protocol">SFTP</acronym>.  It allows you to edit files "remotely."  This is a huge boon for all those tiny style sheet changes you might need to update. It is trial ware, but it is a great <acronym title="Graphical User Interface">GUI</acronym> for something I have to do everyday.  

[transmit]: http://www.panic.com/transmit/


*	#### Read blogs

	[NetNewsWire] lets you categorize and browse your feeds.  With the *Pro* version, you can specify a lot more details.  There's per-category and per-feed customization for period of downloads.  [NNW][NetNewsWire] also synchronizes with the [Bloglines] web based news reader.  This allows you to read your feeds using [NetNewsWire] go to work, or a friends house, and read them at [Bloglines].  All my feeds are added to [Bloglines] except for some testing ones and some private feeds from [LiveJournal].

	See *[Add to Bloglines from NetNewsWire][s2]*

[Bloglines]: http://bloglines.com/
[NetNewsWire]: http://www.newsgator.com/NGOLProduct.aspx?ProdID=NetNewsWire "An ASPX page for an Apple product"
[LiveJournal]: http://livejournal.com/
[s2]: /2006/06/08/add-to-bloglines-from-netnewswire

*	#### Update my [LiveJournal]

	[Xjournal] lets you edit entries, set privacy settings, edit your friends list and do a whole lot of whatever else you want to do on [LiveJournal].

[xjournal]: http://connectedflow.com/xjournal/

*	#### Chat

	*	##### [ichat AV][ichat]

		[ichat] will probably serve most peoples needs.  It supports <acronym title="AOL Instant Messenger">AIM</acronym> and Jabber (e.g. <abbr title="Google Talk">GTalk</abbr>).  It also does video and audio chat.

[ichat]: http://apple.com/ichat

	*	##### [Adium]

		Unfortunately, my friends and contacts can't agree on <strike>which <acronym title="Instant Messaage">IM</acronym> service to use</strike> <abbr title="Google Talk">GTalk</abbr>.  So I use [Gaim]-based [Adium].  [Adium] does pretty much all the major protocols, it's open-source and has a lot of plugins.  What's not to love?  It's even being included in the [Summer of Code 2006][soc] so that it can be more integrated with <abbr title="Google Talk">GTalk</abbr>.

[adium]: http://adiumx.com/
[gaim]: http://gaim.sf.net/
[soc]: http://trac.adiumx.com/wiki/SummerOfCode

	*	##### [Skype]

		<div class="photo screenshot_thumb right"><a href="http://www.flickr.com/photos/davedash/85269051/" title="Photo Sharing"><img src="http://static.flickr.com/37/85269051_1194096479_m.jpg" width="240" height="180" alt="Skype" /></a></div>

		[Skype] was a life saver when we had broadband in our Hotel in India this January (2006).  Free voice chat within the <acronym title="United States">US</acronym> and plenty of accessory phones to go along with it.

[skype]: [http://skype.net/]

*	#### Steal movies and music from starving artists and industry associations

	Trying to find that new [Jonathan Coulton][jc] song?  [Acquisition] might be able to help you or maybe even some of it's [free derivatives][acqlite].  [Acquisition] keeps getting better with each version and allows you to filter out what you aren't looking for.  This is a feature that is lacking from much of the software anywhere.

[jc]: http://www.jonathancoulton.com/
[acquisition]: http://acquisitionx.com/
[acqlite]: http://acqlite.sourceforge.net/


*	#### Collaboratively steal movies and TV shows

	[BitTorrent] offers a unique method of distribution.  There are a number of [BitTorrent] clients, including [Acquisition].  However, due to the sheer number of plugins (I suggest trying some of the <acronym title="Real Simple Syndication">RSS</acronym> plugins), your best bet might be [Azureus], a cross-platform client.

[BitTorrent]: http://www.bittorrent.com/
[azureus]: http://azureus.sourceforge.net/
<!--nextpage-->
<h3 id="programming">Programming: How do I...</h3>

*	#### Keep my files under version control

	[Subversion][svn] is my version control software of choice and I prefer using a combination of the command-line client, available via [Fink][] (see below) and [svnX].  [svnX] makes it easy to see at a glance just exactly what needs to be committed.  It also allows me to browse the repository and find just what I need.

[svn]: http://subversion.tigris.org/
[svnx]: http://www.lachoseinteractive.net/en/community/subversion/svnx/

*	#### Write code

	*	##### TextMate

		[TextMate] is an excellent editor for automating editing tasks.  With features like "snippets," cutting and pasting boilerplate code is a thing of the past.  If it doesn't support the language you want, it's *easy* to remedy that and write your own bundle.

[Textmate]: http://macromates.com/ "The Missing Editor for Mac OSX"

	*	##### Xcode

		[Xcode] is Apple's <acronym title="Integrated Development Environment">IDE</acronym>.  If you're writing Objective-C or Java, [Xcode] might prove useful.  For writing Cocoa applications, the bulk of your work involves dragging connections and defining relations between elements.  The "legwork" of writing actual code, is assuaged with an editor that features what you'd expect: folding, auto-completion and syntax highlighting.  

[xcode]: http://www.apple.com/macosx/features/xcode/

*	#### Get my fix of Unix goodness

	*	##### Fink
	
		Before I bought my Mac, the first thing I looked for was something like [Fink].  [Fink] uses debian packaging of Unix utilities for the Mac.  It's great.  There's an easy installer that puts the fink environment on your computer and then you've got debian style package management:

			sudo apt-get update
			sudo apt-get upgrade

	For that `svn` utility, you'll want `sudo apt-get install svn`.

[fink]: http://fink.sf.net/

	*	##### [iTerm]

		If you use the Unix shell **a lot**, you'll want [iterm] for it's tabbed interface.  It also has a handy feature of bouncing in the dock if something has changed in a background tab.

[iterm]: http://iterm.sf.net/

<!--nextpage-->
<h3 id="multimedia">Multimedia: How do I...</h3>

For the most part, Apple's [iLife] can take care of your multimedia needs.  Playing video is the exception (in this guide), since there are so many formats available, [Quicktime] only can support a small subset of these.  For the non-Apple user, this section a useful overview of just what can be done fairly easily with a Mac.

[quicktime]: http://apple.com/quicktime/
[ilife]: http://apple.com/ilife/

*	#### Listen to Music, Burn a <acronym title="Compact Disc">CD</acronym>, rip a <acronym title="Compact Disc">CD</acronym>

	[itunes] does a good job of putting all the things that you might need related to your music collection, in one place.  The [os x] version is a lot less frustrating than the Windows version, so don't let your past experiences taint your perception of [iTunes].

[itunes]: http://apple.com/itunes/

*	#### Organize my photos, burn them to a <acronym title="Digital Versatile Disc">DVD</acronym>, make slideshows

	[iphoto] is a giant beast, but it does do quite a bit.  It manages large collections of photos.  You can easily download them off your camera, and then categorize them as necessary.  Want to share them?  Burn it onto a <acronym title="Digital Versatile Disc">DVD</acronym> and give it to your family.  Want to make a slideshow set to music from your [iTunes]?  That's not a problem either.  
The entire [iLife] suite is fairly well integrated.  My family always wants us to bring our digital camera so we can put together a cheesy slideshow on <acronym title="Digital Versatile Disc">DVD</acronym>.  Good thing it's easy.  

	If you have a lot of photos there are some tools like [iPhoto Library Manager][ilm] that can make your life easier.

[iphoto]: http://apple.com/iphoto/
[ilm]: http://homepage.mac.com/bwebster/iphotolibrarymanager.html

*	#### Make a <acronym title="Digital Versatile Disc">DVD</acronym> of my Videos and Photos

	Create <acronym title="Digital Versatile Disc">DVD</acronym> menus, order photo slideshows and movies around, add music.  You can do all of this with [iDVD].  

[idvd]: http://apple.com/idvd

*	#### Edit movies

	If you want to actually edit home movies, [iMovie] can help.  You can pull in photos to make slide shows, synchronize it with audio tracks, add in video from other sources.  

[iMovie]: http://apple.com/imovie

*	#### Watch video files

	*	##### [Quicktime]
	
		The obvious choice on a Mac is [Quicktime].  [Quicktime] however lacks some of the codecs that are popularly circulating the internet.  These days you can find much of what you want on [YouTube] or [Google Video][gv] and not have to worry too much of compatability issues. 

[youtube]: http://www.youtube.com/
[gv]: http://video.google.com/

	*	##### [Flip4Mac]: Make Quicktime work

		[Flip4Mac] allows you to play Windows Media Files using Quicktime.  All but a handful of `<acronym title="Windows Media Video">WMV</acronym>` files play with this installed.

[flip4mac]: http://www.flip4mac.com/

	*	##### <acronym title="VideoLan Client">[VLC]</acronym>

		<acronym title="VideoLan Client">[VLC]</acronym> is a cross-platform video client that can play just about anything that [Quicktime] can't with the exception of a handful of certain `<acronym title="Windows Media Video">WMV</acronym>` files.  Chances are if you can't play it with either this or [Quicktime], it can't be played on the Mac.

[vlc]: http://videolan.org/vlc/

<!--nextpage-->
<h3 id="productivity">Productivity: How do I...</h3>

*	#### Do more from my keyboard/automate things/find things faster

	[Quicksilver][qs], [as discussed previously][s1], can speed mundane things up severely:

	> [Quicksilver][qs] is a the <acronym title="Graphical User Interface">GUI</acronym> equivalent to the command line.  You can launch applications or files or perform any number of operations on those files or applications.  With its powerful collection of plugins you can have it do much more, for example you can take a music file and play it in iTunes within the iTunes party shuffle.  Or take an image file and have it submit to [flickr] with a few simple keystrokes.  Initially, I couldn't get an idea of the application, other than a lot of people loved it.  Now, I'm barely using it to its potential and I love it.  Using a computer without it is quite a drag.

	If you need to launch things faster or do more things from the keyboard quickly, get this.  

[flickr]: http://flickr.com/
[qs]: http://quicksilver.blacktree.com/
[s1]: http://spindrop.us/2006/05/28/quicksilver-textmate-crazy-delicious-development-environment

*	#### Keep track of things to do and other lists

	I didn't at first use [OmniOutliner][oo] because I didn't understand the point of an outlining software.  It makes outlines, so what?  After reading enough of [43Folders][43F], however, I decided to check it out.  Now it's the *key to my productivity*.  I keep task lists for several projects in [OmniOutliner][oo] and I actually *get them done*.  Something about hierarchical groupings and the ability to add any number of columns to a task make this such a useful tool.  I've got todo lists with are checkboxes, descriptions, dates, notes, estimates, etc.  If I'm asked to bid on a project, it takes almost no time for me to drop it into [OmniOutliner][oo], split it up into smaller chunks, and throw together an estimate.

### Conclusion

There's a lot of software I'm sure I missed.  But my intent here was to cover a healthy slew of applications that I used myself to get various tasks completed.  I'd like to hear about your favorites and what you think works best on your Mac.

[oo]: http://www.omnigroup.com/applications/omnioutliner/
[43f]: http://43folders.com/
