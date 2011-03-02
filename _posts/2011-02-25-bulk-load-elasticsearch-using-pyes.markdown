---
layout: post
title: "Bulk load ElasticSearch using pyes"
tags: [elasticsearch, pyes, search, mozilla, python]
published: true
time: 2:27PM
---

When indexing a lot of data, you can save time by bulk loading data.

With `pyes` you can do the following:

{% highlight python %}
from pyes import ES


es = ES()
es.index(data, 'my-index', 'my-type', 1)
es.index(data, 'my-index', 'my-type', 2)
es.index(data, 'my-index', 'my-type', 3)
es.index(data, 'my-index', 'my-type', 4)
{% endhighlight %}

This will make 4 independent network calls.

{% highlight python %}
from pyes import ES


es = ES()
es.index(data, 'my-index', 'my-type', 1, bulk=True)
es.index(data, 'my-index', 'my-type', 2, bulk=True)
es.index(data, 'my-index', 'my-type', 3, bulk=True)
es.index(data, 'my-index', 'my-type', 4, bulk=True)
es.refresh()
{% endhighlight %}

Will do this in one call.  This is handy for those "reindex all the items we
can" weekends.
