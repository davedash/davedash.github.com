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
  <li>
    <span class="date">{{ post.date | date: "%Y.%m.%d"}}</span> &raquo;
    <a href="{{ post.url }}">{{ post.title }}</a>
  </li>
{% endfor %}
</ol>

[Full Archive](archive)

Site Tag:  {{ site.tags.keys }}

{% for tag, post in site.tags %}
a
{% endfor %}
