--- 
wordpress_id: 208
layout: post
title: "PHPs strengths: array_count_values"
wordpress_url: http://spindrop.us/?p=208
---
I always like to think of what different interpreted programming languages bring to the table.

Perl is great with string manipulation.  I tend to use perl if I need to rewrite/reformat text.

Python makes it easy to write clean, organized code and has a lot of syntactical sugar like list comprehensions.

For PHP one of my coworkers suggested that maybe it's ease is what it brings to the table.  I've accepted that wryly at first, but after some thought it's actually a real strength.

PHP has positioned itself to be easily adoptable.  When I learned PHP/FI 2.0 it was because I had exhausted server-side includes and needed something better.  PHP/FI was a great solution because it was easy to install (my ISP had it) and documented easy things that I could do.  After all it was just some additional changes to my templates.

I never for once thought that I'd be paid at a company to code in it... but then the internet just got big.

The other way php positioned itself is the library of functions it has out of the box.  Today I found myself looking for a python equivalent to [`array_count_values`](http://www.php.net/array_count_values).

Its a function I wouldn't use every day, but there are rare instances where having a set of data aggregated by count would be very useful.  That's exactly what this function does.

Even python's lists, sets and dictionaries, which can do with simple operations what PHP needs an army of `array_` functions to do, didn't reveal anything useful.  So I will use the following:

<div>
<textarea name="code" class="python">
def list_count_values(l):
    d = {}
    
    for item in l:
        if item in d:
            d[item] += 1
        else:
            d[item] = 1
	
    return d
</textarea>
</div>
