---
title: DRY with Jinja Macros
layout: tutorial
redirect_to: https://blog.dadops.co/2013/08/18/dry-with-jinja-templates/
---
[Jinja][j] is a great templating language that's used with python.  One of the easiest ways to not repeat yourself in Jinja is to use macros.

Let's say you want to build a blog.  You might have something like this

{% highlight html %}
<h1>My Blog</h1>
<h2>Featured Post</h2>
<h3>Why Ponies are Awesome</h3>
<p>
    Ponies are awesome because...
</p>
<h2>Other Posts</h2>
<h3>Where Is My Kitten</h3>
<p>
    Here he is!
</p>
<h3>All the cupcakes</h3>
<p>
    I ate all the cupcakes at Pinterest today.
</p>
{% endhighlight %}

You might try to use for loops and variables in Jinja:

{% highlight jinja %}
{% raw %}
<h1>My Blog</h1>
<h2>Featured Post</h2>
<h3>{{ featured_post.title }}</h3>
{{ featured_post.body }}

{% for post in posts %}
    <h3>{{ post.title }}</h3>
    {{ post.body }}
{% endfor %}
{% endraw %}
{% endhighlight %}

A little bit of repetition, which can get annoying if you want to add a date:

{% highlight jinja %}{% raw %}
<h1>My Blog</h1>
<h2>Featured Post</h2>
<h3>{{ featured_post.title }}</h3>
<span class="date">{{ featured_post.date }}</span>
{{ featured_post.body }}

{% for post in posts %}
    <h3>{{ post.title }}</h3>
    <span class="date">{{ post.date }}</span>
    {{ post.body }}
{% endfor %}
{% endraw %}
{% endhighlight %}

At this point even I'm getting tired of contriving these examples.  Enter the
macro.  Macros can appear anywhere in your template.  They don't render unless
they are called so I usually stick them at the veryt top of a page:

{% highlight jinja %}{% raw %}
{% macro show_post(post) %}
    <h3>{{ post.title }}</h3>
    <span class="date">{{ post.date }}</span>
    {{ post.body }}
{% endmacro %}

<h1>My Blog</h1>
<h2>Featured Post</h2>
{{ show_post(featured_post) }}
{% for post in posts %}
    {{ show_post(post) }}
{% endfor %}
{% endraw %}
{% endhighlight %}

That's a lot easier.  You can think of macros in templates the way you think of functions elsewhere.

For a real world example, you can look at a commit to [Amy Lam's Hackbright project][1].

[j]: http://jinja.pocoo.org/
[1]: https://github.com/amyrlam/earthmd/commit/b71defc10191e4bff0a5d57a7dc61c10d43d4216
