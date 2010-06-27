---
layout: post
title: "python: UnicodeEncodeError: 'ascii' codec can't encode character u'\\xbb' ...: ordinal not in range..."
wordpress_url: http://spindrop.us/2008/01/25/python-unicodeencodeerror-ascii-codec-cant-encode-character-uxbb-ordinal-not-in-range/
ignore: _
site: spindrop
tags: [python, utf-8, error]
---
I don't fully understand utf-8 errors, but I've been getting this error.

So here's a quick fix:

{% highlight python %}
import sys
sys.setdefaultencoding('utf-8')
{% endhighlight %}
