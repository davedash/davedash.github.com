---
layout: default
title: dave dash
---

## About Me

My name is Dave Dash.
I am a [newbie dad][baby],
[someone][kt]'s husband,
an engineer at [Pinterest][p]
and a former web developer at
[Mozilla][m] and [Delicious][d].

You can contact me at `dd+wordproblems` (at) `{this domain}`.

[d]: http://delicious.com/
[p]: http://pinterest.com/
[a]: http://addons.mozilla.org/en-US/firefox/
[baby]: /tag/baby
[m]: /tag/mozilla
[kt]: http://katiebonn.com/

## A Tutorial

I work with a lot of developers both seasoned and new who are new to python.
Here is a [tutorial on virtualenv][v] which I believe is a cornerstone of
healthy python development.

[v]: /tutorial/virtualenv

## Recent Blog Posts
<ol>
{% for post in site.posts limit:10 %}
    {% include item.html %}
{% endfor %}
</ol>


[Full archive](archive)


