---
layout: post
title: "Pythonic string formatting in Javascript"
tags: [python, amo, javascript, mozilla, snippets]
published: true
time: 10:21AM
---
[a]: https://addons.mozilla.org/

We do a lot of string manipulation on the [Firefox Addons][a] site.  A lot of
it has to do with localization so one thing that comes up is being able to
format strings.  Here's a little snippet to give yourself python like string
formatting:

{% highlight javascript %}
    /* Python(ish) string formatting:
     * >>> format('{0}', ['zzz'])
     * "zzz"
     * >>> format('{x}', {x: 1})
     * "1"
     */
    function format(s, args) {
        var re = /\{([^}]+)\}/g;
        return s.replace(re, function(_, match){ return args[match]; });
    }
{% endhighlight %}
