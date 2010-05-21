--- 
wordpress_id: 141
layout: post
title: "python: relative paths"
wordpress_url: http://spindrop.us/2008/01/27/python-relative-paths/
---
So I started yesterday with Django, and I decided I didn't want to futz with creating another mysql database that I'd need to manage, etc.  Instead I'll just use `sqlite`.

I wanted to keep my `sqlite` database within my project regardless of where I might move my project later.  So I did this:

<div><textarea name="code" class="python">
	import os        
	DATABASE_NAME = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data/db.sqlite')        # Or path to database file if using sqlite3.
</textarea></div>

I confused a lot of people on IRC, but it's really quite easy:

* `__file__` is the filename of the current script, very similar to PHP's `__FILE__`
* `os.path.abspath` calculates the absolute path, hence the absolute path of the current file
* `os.path.join` does all the nasty business of joining paths together and figuring out what type of slashes are needed, etc.
* 'data/db.sqlite' is a string

So really all we were doing is creating a relative path, but setting it absolutely.
