---
layout: default
title: dave dash
---

## About

My name is Dave Dash.  I am a soon-to-be dad and a Senior Web Developer at
Mozilla for the Firefox Add-ons site.

You can contact me at `dd+onion` (at) `{this domain}`.

## Recent Blog Posts
<ol>
{% for post in site.posts limit:10 %}
    {% include item.html %}
{% endfor %}
</ol>

[Full archive](archive)

## Tags

<ul class="tags">
{% include tags.html %}
</ul>
