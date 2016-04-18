---
layout: default
title: dave dash
---
{% capture about_content %}
* Father of two little boys
* [Someone][kt]'s husband
* A Web Operations Consultant
* Former Software and Operations Engineer at [Pinterest][p]
* Former web developer at [Mozilla][m] and [Delicious][d]

You can contact me at `dd+gardenisle` (at) `{this domain}`.

[d]: http://delicious.com/
[p]: http://pinterest.com/
[a]: http://addons.mozilla.org/en-US/firefox/
[m]: /tag/mozilla
[kt]: http://katiebonn.com/
{% endcapture %}

<div id="posts" class="container">
    <section class="col-md-12 wow fadeIn">
      <div class="post featured">
        <div class="row">
          <div class="col-md-6 media">
            <img src="/static/images/2016/holi_with_r.jpg" class="img-responsive" />
          </div>
          <div class="col-md-6 caption">
            <p class="post-title">I am Dave Dash</p>
            {{ about_content | markdownify }}
          </div>
        </div>
      </div>
    </section>
</div>
