---
wordpress_id: 126
layout: post
title: Table based layouts?  In this day in age?  Really?  How about grids?
wordpress_url: http://spindrop.us/2007/10/05/table-based-layouts-in-this-day-in-age-really-how-about-grids/
site: spindrop
---
[tags]css, yui, grids, table, layout[/tags]


[YUI]: http://developer.yahoo.com/yui/
[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/
[grids]: http://developer.yahoo.com/yui/grids/

I think there are three kinds of people:

1. People who learned tables for layouts and went to CSS+`div`s.
2. People who learned tables for layouts and never needed to learn CSS+`div`s (or insisted that this was way too complicated)
3. People who never learned tables.

I would argue in some ways the second class of people are right, tables are a lot easier.  Until you run into issues... and until you need to maintain your template code.

Luckily there's grids.  Grids are easier than tables and easy to maintain and look at.  You can achieve just about anything with [grids][].

<!--next page-->
<!--more-->

Personally I like using [Yahoo's YUI][YUI] to get grid support.  It's a CSS framework in the same way that [jQuery](http://jquery.com) is a javascript framework or that [symfony][] is a PHP5 framework.

[YUI][] will normalize all your elements and give you a standard way to change the size of text and elements and give you [grids][].

So it helps to think of your layout in terms of grids... or columns.  [YUI grids][grids] supports some common combinations:

* `.yui-g` - 2 equal size containers (nest to get 4).
* `.yui-gb` - 3 equal size containers
* `.yui-gc` - 2/3 - 1/3
* `.yui-gd` - 1/3 - 2/3
* `.yui-ge` - 3/4 - 1/4
* `.yui-gf` - 1/4 - 3/4

Granted, this doesn't cover every scenario, but it's a start, and it's easy to build off of to create your own special sizes.

So to create some magical columns you do the following:

<div><textarea name="code" class="html">
<div class="yui-g">
  <div class="yui-u first"></div>
  <div class="yui-u"></div>
</div>
</textarea></div>

`yui-g` can be substituted for any of the above classes.  `yui-u` is your columns or grid cells.  `first` indicates the first column since `:first` isn't understood by some popular browsers.

Now you know grids.  It's less complicated than the tabular equivalent:

<div><textarea name="code" class="html">
<table class="layout">
  <tr class="first_row">
    <td class="col1"></td>
    <td class="col2"></td>
  </tr>
</table>
</textarea></div>

With the framework in place, it's a lot easier to quickly adjust your layouts, and the readability is huge especially as your layouts grow.
