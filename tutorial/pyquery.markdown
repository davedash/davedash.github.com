---
layout: tutorial
title: Scraping the web with pyquery
---

## tl;dr

    pip install pyquery
    python
    >>> from pyquery import PyQuery as pq
    >>> doc = pq('<html><body><p>Hello World</p></body></html>')
    >>> print doc('p').text()
    'Hello World'

## Details

At Mozilla Web we developed a pattern that liked for
testing templates.  We would make a fake request to a URL, get the content from the response object (we used Django) and then search for elements using `pyquery`.  `pyquery` used a syntax similar to jQuery so it wasn't very difficult for us (who used jQuery) to carefully write selectors that would find the exact piece of text we are looking for.

Let's do a more complicated example.  Currently this is my home page:

![screenshot](http://cl.ly/image/2v0R212d2g3M/28565fccbba59b5824979ae4d32da714-1.png)

Let's try to grab the text in question.
Let's install `pyquery` and [`requests`][r].  Requests is a library that makes light work of fetching web pages:

    pip install pyquery requests

Now let's explore:

{% highlight python %}

import requests
response = requests.get('http://davedash.com/')
response.content[:40]
'<!DOCTYPE html>\n<html xmlns="http://www...".. />

{% endhighlight %}


Great looks like we were able to fetch some HTML, and hopefully it's my web page.

Let's see if we can load that into pyquery:

{% highlight python %}
from pyquery import PyQuery as pq
doc = pq(response.content)
{% endhighlight %}

We can use jQuery style selectors to get HTML elements out of my homepage.  Let's take a wild guess and assume I put this in a paragraph tag:

{% highlight python %}
doc('p')
>>> [<p>, <p>, <p>, <p>]
{% endhighlight %}

It appears there are 4 paragraph tags.  No problems.  This is python:

{% highlight python %}
[p.text for p in doc('p')]
>>> ['My name is Dave Dash.\nI am a ',
     'You can contact me at ',
     'I work with a lot of developers both seasoned and new who...',
     None]
{% endhighlight %}

Oh brilliant we just need the third paragraph tag:

{% highlight python %}
doc('p')[2].text
>>> 'I work with a lot of developers both seasoned and new who...'
{% endhighlight %}

This is simple stuff.  Let's do something a bit more advanced.  Let's try to get the dates of each post that I've listed in "Recent Posts":

{% highlight python %}
[e.text for e in doc('span.date')]
>>> ['2013.03.05',
     '2012.07.06',
     '2012.06.04',
     '2012.04.07',
     '2012.03.19',
     '2012.03.07',
     '2012.03.01',
     '2012.02.22',
     '2012.02.16',
     '2012.01.05']
{% endhighlight %}

Clearly I don't blog nearly enough. Note the parameter in `doc` is
`'span.date'`.  If you don't speak CSS it means I'm looking for a `<span>`
element with a class of `date`.  Similarly the `doc` object we created can take
any valid CSS selector as a string argument.

Happy scraping.


[i]: /tutorial/ipython
[r]: http://docs.python-requests.org/en/latest/
