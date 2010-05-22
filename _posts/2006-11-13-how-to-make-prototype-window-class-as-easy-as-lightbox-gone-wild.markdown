---
wordpress_id: 69
layout: post
title: How to make Prototype Window Class as easy as Lightbox Gone Wild
wordpress_url: http://spindrop.us/2006/11/13/how-to-make-prototype-window-class-as-easy-as-lightbox-gone-wild/
site: spindrop
tags: [programming, css, prototype, lightbox, javascript]
---
[l]: http://particletree.com/features/lightbox-gone-wild/ "Lightbox Gone Wild"
[p]: http://prototype-window.xilinus.com/ "Prototype Window Class"

I like the way that [Lightbox Gone Wild][l] will automatically pickup any links with the `class=lbOn`, but I wanted to use (at some point) [Prototype Window Class][p] instead.

Luckily [PWC][p] is built on Prototype which means we've already loaded a helpful library.

<!--more-->

In order to take all `class=lbOn` objects and run them through [PWC][p] we just write a simple loop and iterate.

So here's the low-down:

* Download [PWC][p]
* Copy window.js
* Use the included prototype & script.aculo.us if you don't already include it in your page
* copy any themes you wish to use.

In your page add this bit of JavaScript:

<div><textarea name="code" class="js">
	var mylb = Class.create();
	
	mylb.prototype = {
		initialize: function(ctrl) {
			this.content = ctrl.href;
			Event.observe(ctrl, 'click', this.activate.bindAsEventListener(this), false);
			ctrl.onclick = function(){return false;};
			},
	
			// Turn everything on - mainly the IE fixes
			activate: function(){
				var win = new Window('window_id', {className: "alphacube",title: "Tour", url: this.content, width:700, height:500});
				win.setDestroyOnClose();
				win.showCenter(true);
			}
		}

		lbox = document.getElementsByClassName('lbOn');
		for(i = 0; i < lbox.length; i++) {
			valid = new mylb(lbox[i]);
		}
</textarea></div>

So, this code simply looks for all the anchor tags with `class=lbOn` and then  creates a new `mylb` instance for each anchor.  The end.
