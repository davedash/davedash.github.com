---
layout: post
title: "Better querying for ElasticSearch"
tags: [mozilla, elasticsearch, python]
published: true
time: 2:55PM
---
I wrote [about how to write filter queries using `pyes`][t].
Unfortunately after using ElasticSearch in [the Add-ons Builder][f], I realized
that our code would become unwieldy and hard to read if we kept using straight
up `pyes`.

I prefer to write APIs so that are natural and conform to how I think, not one
that simply mirrors another system.

So rather than this:

{% highlight python %}
    filters = [TermFilter("platform", "all"),
               TermFilter("product", "firefox"),
               TermFilter("version", "4.0")]
    filter = ANDFilter(filters)
    q = FilteredQuery(MatchAllQuery(), filter).search()
    q.facet.add_term_facet('type')
    results = es.search(q)
{% endhighlight %}

I made [something simpler][s]:

{% highlight python %}
    from elasticutils import S
    results = (S(platform='all', product='firefox', version='4.0')
               .facet('type').get_results)
{% endhighlight %}

Here were the design thoughts:

* I wanted something easy to remember, ``S`` for search.
* I wanted smart defaults, by default ``S()`` matches all documents, unless you
  give it a query term.
* I didn't want to write python that looked like Java, or JSON or even a
  ``dict``.
* I wanted to write something that felt like the Django-ORM
* Ultimately I want code that I enjoy writing.

So here it is, I expect it to power Firefox Add-ons, the Add-ons Builder and
Firefox Input shortly.

This is all part of [ElasticUtils][s].
Let me know if you are using it, and pull requests are welcome!

[t]: /2011/03/25/filter-queries-using-pyes/
[f]: http://builder.addons.mozilla.org
[s]: https://github.com/davedash/elasticutils/
