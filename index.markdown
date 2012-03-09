---
layout: default
title: dave dash
---

## About Me

My name is Dave Dash.
I am a [newbie dad][baby],
[someone][kt]'s husband
and a fromer web developer at
[Mozilla][m] for [Mozillians][mo],
[Firefox Input][i] and [Firefox Add-ons][a] sites.

You can contact me at `dd+stereolab` (at) `{this domain}`.

[mo]: http://mozillians.org
[i]: http://input.firefox.com/
[a]: http://addons.mozilla.org/en-US/firefox/
[baby]: /tag/baby
[m]: /tag/mozilla
[kt]: http://katiebonn.com

## Recent Blog Posts
<ol>
{% for post in site.posts limit:10 %}
    {% include item.html %}
{% endfor %}
</ol>


[Full archive](archive)


