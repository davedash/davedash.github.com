---
layout: post
title: The Python textcluster Package
tags: [python, clustering, search, mozilla, moz10, firefox]
published: true
time: 7:49AM
---

[1]: http://davedash.com/2010/03/18/finding-the-most-common-firefox-issues/
[fi]: http://aakash.doesthings.com/2010/06/25/hi-my-name-is-firefox-input/
[g]: http://davedash.com/2010/07/08/the-python-textcluster-package/

Earlier I wrote about [finding the most common Firefox issues][1].  I had
wanted to automate that process and continually find these issues.
Unfortunately I never had time to do this.

When they announced [Firefox Input][fi], I thought about doing this again...
just with Firefox Input data but then I went on paternity leave and time kind
of crept away.  But I mentioned the idea this week and it piqued some interest.

So I found myself with a bit of time to work on it.  The first stage was
releasing a python library called [`textcluster`][g].

[`textcluster`][g] takes the [work I did earlier][1] and makes it a bit more
general purpose.  The idea is I can do something like this:

{% highlight python %}
docs = (
        'Every good boy does fine.',
        'Every good girl does well.',
        'Cats eat rats.',
        "Rats don't sleep.",
        )

c = Corpus()
for doc in docs:
    c.add(doc)

print c.cluster()
{% endhighlight %}

Which results in:

    [
        (
            "Rats don't sleep.",
            {'Cats eat rats.': 0.21353467285253394}
        ),
        (
            'Every good girl does well.',
            {'Every good boy does fine.': 0.32030200927880093}
        )
    ]


The number is the "similarity" between the strings relative to the entire
document corpus.

My next trick is to see if I can run this memory-intensive calculation over a
data-set of 25,000 opinions submitted.  If I can we can get some interesting
data about what people think of the new [Firefox beta][b].

[b]: http://www.mozilla.com/en-US/firefox/all-beta.html
