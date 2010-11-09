---
layout: post
title: "Faceted Search on Input"
tags: [sphinx, input, mozilla, django, amo]
published: true
time: 1:25PM
---
[sphinx]: http://sphinxsearch.com/
[i]: http://input.mozilla.com/
[f]: http://en.wikipedia.org/wiki/Faceted_search
[amo]: http://addons.mozilla.org/
[s]: http://www.sittercity.com/search-sitters.html?ct=101&zip=95126
[e]: http://ebay.com/

So one trick with [Sphinx search][sphinx] is [faceted search][f].  It's somewhat
crudely implemented, by batching queries together, but does the job well.  In
the case of [Firefox Input][i] it can reduce quite a bit of queries (our
search result pages take one batched sphinx query, and one database query now
instead of 5 database queries).

<div class="side">
<a href="http://www.flickr.com/photos/davedash/5126379671/"
   title="Add-on Search Results for shopping :: Add-ons for Firefox">
   <img src="http://farm5.static.flickr.com/4041/5126379671_33b3e472d5_m.jpg"
    width="240" height="172" alt="Add-on Search Results for shopping" /></a>
</div>

Faceted search is search with filters to help narrow down a result set.  I'll
give you three examples.  [Firefox Add-ons][amo] which I wrote,
[Sitter City][s] which gives you a lot of ways on narrowing down on the perfect
baby sitter and [ebay][e] which lets your narrow down on auction items.

For [Input][i] we ask for the following when we do a search:

* How many opinions match the term for which we are searching taking into
  account any preferences we have already specified (feeling, locale, operating
  system, date range, etc).
* How many opinions show a positive sentiment, and how many show a negative
  sentiment?
* What is the breakdown of languages for the opinion results.  (I.e. how many
  are en-US, de, fr, etc).
* How many people are on Mac, Linux or Windows.

We can batch these four queries into a single Sphinx request.

Here's [our implementation](http://github.com/davedash/reporter/commit/348018).

Having done this twice, I do recognize that there is a lot of room for making
the code a bit more reusable.  But overall it runs fairly well.
