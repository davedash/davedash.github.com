---
wordpress_id: 98
layout: post
title: Textmate Snippets for YUI em calculations
wordpress_url: http://spindrop.us/2007/05/08/textmate-snippets-for-yui-em-calculations/
site: spindrop
---
[tags]yui, yahoo, css, snippet, textmate, ems, px[/tags]

If you use [YUI grid layouts](http://developer.yahoo.com/yui/grids/) you'll notice that `ems` are the preferred units and for good reason.  But ems don't make sense to people like us who want to be super precise down to the pixel... pixels make sense.

So type in a number select it and run this `ruby` script as a TextMate command (that outputs as a snippet):


<div><textarea name="code" class="ruby" cols="100" rows="15">
#!/usr/bin/env ruby
#
# This script will do the necessary YUI calculations from px to ems
#
# The result is inserted as a snippet, so it's
# possible to tab through the place holders.

# validate input
input    = ENV['TM_SELECTED_TEXT'].to_i;
width    = input.to_f/13
ie_width = width * 0.9759

print "${1:width}:"+width.to_s+"em;*$1:"+ie_width.to_s+"em;$0"
</textarea></div>

You'll have the proper tab stops to change the newly calculated `ems` from `width` to `margin-left` or `margin-right` or whatever it is you desire.
