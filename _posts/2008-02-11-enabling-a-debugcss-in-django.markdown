---
wordpress_id: 159
layout: post
title: Enabling a debug.css in django
wordpress_url: http://spindrop.us/2008/02/11/enabling-a-debugcss-in-django/
site: spindrop
---
I like for extra magical stuff to occur when I am in development/debug mode.  One of those magical things is a a magic `debug.css` style sheet.

Django sets a `debug` variable when the following conditions are met:

`django.core.context_processors.debug` is listed under `TEMPLATE_CONTEXT_PROCESSORS` and your IP address (127.0.0.1 if your using the standard development server) is listed under `INTERNAL_IPS`.

Then in your `base.html` just add something like this:

<div><textarea name="code" class="html">
  {% if debug %}
  <link rel="stylesheet" type="text/css" media="screen" href="/static/css/debug.css" />
  {% endif %}
</textarea></div>

For my CSS I like to use the following:

<div><textarea name="code" class="css">
.incomplete { background:#c0c !important}
.incomplete .incomplete{background:#d0d !important}
.incomplete .incomplete .incomplete{background:#e0e !important}
.incomplete .incomplete .incomplete .incomplete{background:#f0f !important}
</textarea></div>

As I am developing my site, if I feel that a block of content isn't fully finished for whatever reason, I mark it with a class of `incomplete`.  This results in a purple color (which I don't use on my site), the purpler it is... the more incomplete the content.

It's like eating that stuff that makes your teeth red if you haven't brushed them enough.  Once all the purple's gone the site is ready for production.

Eventually we can use all these hooks into the template to implement a symfony-style debug bar... later.
