---
layout: default
title: dave dash
---
<div class="jumbotron">
{% capture about_content %}
# I am Dave Dash.

* Father of two little boys
* [Someone][kt]'s husband
* A Web Operations Consultant
* Former Engineer at [Pinterest][p]
* Former web developer at [Mozilla][m] and [Delicious][d]

You can contact me at `dd+pogostick` (at) `{this domain}`.

[d]: http://delicious.com/
[p]: http://pinterest.com/
[a]: http://addons.mozilla.org/en-US/firefox/
[m]: /tag/mozilla
[kt]: http://katiebonn.com/
{% endcapture %}
{{ about_content | markdownify }}
</div>
