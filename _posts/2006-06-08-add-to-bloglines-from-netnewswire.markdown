---
wordpress_id: 38
layout: post
title: Add to Bloglines from NetNewsWire
wordpress_url: http://spindrop.us/2006/06/08/add-to-bloglines-from-netnewswire
site: spindrop
---
I use [NetNewsWire][] in conjunction with [Bloglines][] and often come across new feeds from within [NetNewsWire][] that I'd like to add to my [Bloglines][] (versus adding it directly to [NetNewsWire][]).  

[Bloglines][] is my sandbox for new feeds until I deem them worthy enough to read in [NetNewsWire][].  So here's an AppleScript to feed (no pun intended) my <acronym title="Real Simple Syndication">RSS</acronym> addiction:

<div><textarea name="code" class="Applescript">
	-- NetNewsWire to Bloglines
	tell application "NetNewsWire"
		set u to (URL of selectedHeadline)
	end tell
	tell application "NetNewsWire"
		activate
		open location "http://bloglines.com/sub?submiturl=Subscribe&url=" & u
	end tell
</textarea></div>

or save [this apple script][script] to `~/Library/Application\ Support/NetNewsWire/Scripts/`.

[NetNewsWire]: http://www.newsgator.com/NGOLProduct.aspx?ProdID=NetNewsWire 
[Bloglines]: http://bloglines.com/
[script]: applescript://com.apple.scripteditor?action=append&script=%2D%2D%20NetNewsWire%20to%20Bloglines%0D%0Dtell%20application%20%22NetNewsWire%22%0D%09set%20u%20to%20%28URL%20of%20selectedHeadline%29%0Dend%20tell%0D%0Dtell%20application%20%22NetNewsWire%22%0D%09activate%0D%09open%20location%20%22http%3A%2F%2Fbloglines%2Ecom%2Fsub%3Fsubmiturl%3DSubscribe%26url%3D%22%20%26%20u%0Dend%20tell%0D
