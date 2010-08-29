---
layout: default
title: dave dash
---

## About Me

My name is Dave Dash.  I am a [newbie dad][baby] and a web developer at
[Mozilla][m] for [Firefox Input][i] and [Firefox Add-ons][a] sites.

You can contact me at `dd+onion` (at) `{this domain}`.

[i]: http://input.firefox.com/
[a]: http://addons.mozilla.org/en-US/firefox/
[baby]: /tag/baby
[m]: /tag/mozilla

## Recent Blog Posts
<ol>
{% for post in site.posts limit:10 %}
    {% include item.html %}
{% endfor %}
</ol>


[Full archive](archive)


