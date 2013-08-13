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

## Tutorials

I work with a lot of developers both seasoned and new who are new to python.
Here are some tutorials on things that I hope can be helpful:

* [Virtualenv][v] which I believe is a cornerstone of healthy python
  development.
* [pdb: the python debugger][pdb] which is an incredible tool for debugging
  even the toughest of applications.

[v]: /tutorial/virtualenv
[pdb]: /tutorial/pdb-the-python-debugger

## Recent Blog Posts
<ol>
{% for post in site.posts limit:10 %}
    {% include item.html %}
{% endfor %}
</ol>


[Full archive](archive)


