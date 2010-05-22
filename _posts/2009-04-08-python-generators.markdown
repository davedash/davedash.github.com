---
wordpress_id: 258
layout: post
title: Python Generators
wordpress_url: http://spindrop.us/?p=258
site: spindrop
---
Someone had mentioned "generators" in python to me, so I decided to figure out what it was... and I figured it out.  I think a simple example would help explain it:

<div><textarea name="code" class="python">
>>> def fib():
...  i1 = 0
...  i2 = 1
...  while True:
...    yield i2
...    i3 = i2 + i1
...    i1 = i2
...    i2 = i3
... 
>>> a = fib()
>>> a
<generator object at 0x319468>
>>> a.next()
1
>>> a.next()
1
>>> a.next()
2
>>> a.next()
3
>>> a.next()
5
</textarea></div>

Basically you can iterate over this "generator" which is a special function that "yield"s more than one value if you keep pinging it.

Adding this to the toolkit in my brain.  I'm thinking one potential use is taking a resultset from a datastore (e.g. mysql) and converting it into an object.  
