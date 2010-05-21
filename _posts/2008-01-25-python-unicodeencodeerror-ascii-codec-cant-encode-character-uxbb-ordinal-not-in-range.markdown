--- 
wordpress_id: 138
layout: post
title: "python: UnicodeEncodeError: 'ascii' codec can't encode character u'\\xbb' ...: ordinal not in range..."
wordpress_url: http://spindrop.us/2008/01/25/python-unicodeencodeerror-ascii-codec-cant-encode-character-uxbb-ordinal-not-in-range/
---
[tags]error, python, utf-8[/tags]

I don't fully understand utf-8 errors, but I've been getting this error.

So here's a quick fix:

<div><textarea name="code" class="python">
import sys
sys.setdefaultencoding('utf-8')
</textarea></div>
