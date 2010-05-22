---
wordpress_id: 52
layout: post
title: Inverting color codes in Textmate
wordpress_url: http://spindrop.us/2006/07/19/inverting-color-codes-in-textmate/
site: spindrop
---
[textmate]: http://macromates.com/
[g1]: http://www.google.com/search?q=inverse+colors+hex

I deal a lot with <abbr title="hexadecimal">hex</abbr> color codes in <acronym title="Cascading Style Sheets">CSS</acronym>.  One thing I occasionally need to do is invert color codes.  Normally this is something I could [Google][g1] for, but I wanted a solution that didn't requiring constant reference.

My favorite text editor, [Textmate], has a powerful automation system.  I can write mini scripts in whatever language suitable and take advantage of the power of Unix shell scripting to execute them.  [From Googling][g1], I learned enough ruby to learn that this:

	printf("#%06X", 0xFFFFFF - STDIN.gets.gsub(/^#/,"").hex )

Will invert a hex color from standard input.  What it's doing is fairly simple.  It's using `printf` to print a formatted string.  `%06X` means it should zero-fill the resulting string with up to six zeros, the same way a hex color string is (e.g. we write 0000FF and not FF to mean 'blue').  The rest is simple subtraction.  We take `FFFFFF`, the hex code for white, and subtract the input from `STDIN` and arrive at the inverse of what we started.
<!--next page-->
Now to add this to [TextMate] we open `Automation|Run Command|Edit Commands...` and create a new command:

	echo $TM_SELECTED_TEXT |ruby -e 'printf("#%06X", 0xFFFFFF - STDIN.gets.gsub(/^#/,"").hex )' 

This echo's whatever is selected and pipes it to the `ruby` script.  We set the command to input selected text and replace the selected text on output.  Furthermore we can bind it to a keystroke.  I chose `Control-Alt-I`, as it is unused on my system.

Voila, I can highlight any hex code and instantly invert it.

To keep this on one line, I neglected a few friendly features.  One is interpreting 3-digit <abbr title="hexadecimal">hex</abbr> colors (e.g. #ccc), and the other is knowing whether or not to place the `#` in the result.  If you can come up with an elegant solution, please post it below.  Otherwise I hope this helps.

