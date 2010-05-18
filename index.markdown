---
layout: default
title: dave dash
---

## About

My name is Dave Dash.  I am a soon-to-be dad and a Senior Web Developer at
Mozilla for the Firefox Add-ons site.


## Recent Blog Posts
<ol>
{% for post in site.posts limit:10 %}
    {% include item.html %}
{% endfor %}
</ol>

[Full Archive](archive)

## Tags

<p class="tags">
{% include tags.html %}
</p>
