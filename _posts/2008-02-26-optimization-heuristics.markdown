---
wordpress_id: 169
layout: post
title: Optimization heuristics
wordpress_url: http://spindrop.us/2008/02/26/optimization-heuristics/
site: spindrop
tags: [programming, symfony, php, del.icio.us, system calls]
---
I decided to play version control private-eye today when my coworker mentioned that we make a system call to check the time several times per request on a few specific pages.

My analysis was we didn't need to have the calls but it had me thinking...
<!--more-->

### The micro-caching heuristic

One way of optimizing code is by calculating expensive operations once and storing them in a specific location.  It's a micro-cache if you will of data.

One obvious example ends up being loops:

<div><textarea name="code" class="php">
// inefficient
for ($i = 0; $i < count($arr); $i++)
{
// magic
}

// efficient
$arr_size = count($arr);
for ($i = 0; $i < $arr_size; $i++)
{
// magic
}
</textarea></div>

The inefficient example computes `count($arr)` *n* times where *n* is the size of the array `$arr`.  The latter computes it once.

When we write and review code we should look out for loops and repeated code.  These elements can be pulled out.

With some data lookups like system calls or queries we can apply a request-wide caching.  In a symfony app, for example, we might need to calculate the time stamp in several locations throughout the code.  Rather than calling `time()` throughout the code, we can create a site wide accessible attribute that has the same value.

For example, we can subclass `sfContext` and add a method called `getTime()` which runs `time()` once and only once per request and stores it internally.  Whenever part of the app needs the time stamp, `myContext::getInstance()->getTime()` (or an equivalent shortcut) can be called.  Of course, I haven't tested this, and `myContext` might not be the best place for this, but a similar strategy will work.

-dd
