---
layout: post
title: "Filter Queries using pyes"
tags: [pyes, elasticsearch, mozilla, input.mozilla.com]
published: true
time: 8:23PM
---
I've been having a tough time navigating the Elastic Search docs, but some
sleuthing in the test suite for `pyes` has proved helpful.

If I have documents that I'd like filtered by let's say `product`, `version`
and `platform`, I can construct a query like so:

{% highlight python %}
    filters = [TermFilter("platform", "all"),
               TermFilter("product", "firefox"),
               TermFilter("version", "4.0")]
    filter = ANDFilter(filters)
    q = FilteredQuery(MatchAllQuery(), filter)
    results = es.search(q)
{% endhighlight %}

There is perhaps a more succinct way of doing this, but this serves my
purposes.

Let's say you need facets as well:

{% highlight python %}
    filters = [TermFilter("platform", "all"),
               TermFilter("product", "firefox"),
               TermFilter("version", "4.0")]
    filter = ANDFilter(filters)
    q = FilteredQuery(MatchAllQuery(), filter).search()
    q.facet.add_term_facet('type')
    results = es.search(q)
{% endhighlight python %}
