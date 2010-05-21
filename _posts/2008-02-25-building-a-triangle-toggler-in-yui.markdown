--- 
wordpress_id: 168
layout: post
title: Building a triangle toggler in YUI
wordpress_url: http://spindrop.us/2008/02/25/building-a-triangle-toggler-in-yui/
---
If someone knows the more common name for triangle-toggle menu's similar to [this](http://developer.yahoo.com/yui/examples/treeview/menu_style.html).  Let me know.

There is a widget where an element toggles the display of a secondary set of elements.  The toggle shows an arrow pointing down or right depending on the visibility of the elements.  I wanted to build that in YUI.

<!--more-->
The problem is two-fold:

1. Build a triangle that toggles from right to down.
2. Show and hide content.

However, with some clever CSS we can do this all in a single class change on an element.

### Build that triangle

There's a number of ways to show or hide this triangle.  Because it is flexible, I'm going to opt for using a background image.  Also to save on HTTP requests, I'll use a sprite-d image.  This may get merged with other icons on the system.

The particular site I'm working on uses a black background with white text, therefore a white triangle toggle seems appropriate.  

<div style="background:black;text-align:center; padding:1em">
<img src="http://spindrop.us/wp-content/uploads/2008/02/sprite.png" alt="sprite.png" border="0" width="11" height="29" />
</div>

This is what I use.  I leave a little space, because the background will only clip horizontally based on the size of the element.

### Add the HTML/CSS

The following HTML:

<div><textarea name="code" class="html">
<div id="area" class="off">
  <h3><span class="toggle">Toggle Me</span></h3>
  <ul class="hide_me">
  </ul>
</div>
</textarea></div>

and the following CSS:

<div><textarea name="code" class="css">

.toggle {
    background: url(../images/icons/sprite.png) no-repeat 0px -14px;
    padding: 0 0 0 18px;
}

.off .hide_me {
    display: none;
}

.on .toggle {
    background-position: 0 9px;
}

</textarea></div>

Provide the two states we require for the triangle.  If you are new to sprites, rather than changing the background image entirely we just shift the background image up or down appropriately to show a new background.

### The Javascript

The javascript is rather simple, but we put in some magical tricks here and there.

<div><textarea name="code" class="js">
var MA = {}
MA.toggler = function()
{
    var e = YAHOO.util.Event; 
    var d = YAHOO.util.Dom;
    
    return {
        init: function() {
            e.onDOMReady(this.setup,this, true)
        },
        
        setup: function() {
            e.on(d.get('doc4'),'click',this.handleClick,this,true);
        },
        
        handleClick: function(ev) {
            var target = e.getTarget(ev);
            if (d.hasClass(target, 'toggle')) {
                var toggle = target.parentNode.parentNode;
                this.toggle(toggle);
            }
        },
        toggle: function(element) {
            var on  = "on";
            var off = "off";
            if (d.hasClass(element, on)){
                d.removeClass(element, on);
                d.addClass(element, off);
            } else {
                d.removeClass(element, off);
                d.addClass(element, on);
            }
        }
    }
}();

MA.toggler.init();
</textarea></div>

If you're unfamiliar with this style of Javascript, here's what's going on.  Everything is done in the `MA` namespace as to not conflict with other javascript.

The toggler is fairly generic and expects a similar HTML structure for *any* toggle-able element.  That means this code only needs to be written once, and anytime we use the `toggle` class, toggling in this fashion will occur.

We only run the `init` function.  `init` says when the `DOM` is available then run the `setup` function.  `setup` adds an event handler to `doc4`.  `doc4` just happens to be the id we use on our `body` tag.

Note that we're listening for clicks everywhere.  This means we have to define only one event handler, regardless of how many toggle-able items there are.  The event handler checks to make sure we clicked on a relevant element and then applies the `toggle` function to the grandparent element (switching the class from `off` to `on` as appropriate).

Note that this style of event handling means you need to carefully apply your class names.  Also note, that this code could be optimized a little bit more, I haven't put this code into production, and therefore haven't optimized it for the YUI compressor.

Try this out if you want, I'm sure it can be trimmed down overtime.  If you have trouble with it, let me know.

-d
