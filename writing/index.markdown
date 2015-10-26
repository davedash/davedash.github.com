---
title: writing | dave dash
---
<section id="medium">
  <h1>Much of my writing is now on Medium</h1>

  {% include medium.html %}

  [More posts on Medium.](https://medium.com/@davedash/)
</section>
<section id="other-writing">
{% capture content %}

# Other Writing
<ol class="post-list">
{% for post in site.posts limit:20 %}
{% include item.html %}
{% endfor %}
</ol>

[Full archive](/archive)
{% endcapture %}
{{ content | markdownify }}
</section>
