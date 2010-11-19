---
layout: post
title: "Counting Sphinx groupBy Queries"
tags: [sphinx, search, input.mozilla.com, mozilla]
published: true
time: 11:46AM
---
[i]: http://input.mozilla.com/

I quickly implemented Sphinx on Input, while revisiting it, I saw that we try
to answer this type of question:

> Of the results displayed:
>
> * How many are happy and how many are sad?
> * How many are for Windows, Linux or Mac?
> * How many are for English, French or Japanese

Finding these involve using faceted search.  Unfortunately this is a bit
awkward to do using Sphinx.  For the first example, happy or sad you would have
to run the query like such:

1. Take the query, remove any filters on *happiness* and do a group by on
   happy opinions
2. Restore any filters on happiness and run the query as normal.
3. Return both the results, and the aggregate data from step 1.

Doing the group by is easy, but you only get to know how many feelings there
are and what they were.  In our case: happy and sad.  What we really want is
how many of our original search were happy and how many were sad?

I assumed something like this would work:

    sphinx.SetSelect('feeling, @count')

`@count` is one of those magic variables that Sphinx uses.  Unfortunately this
doesn't work.  `COUNT(*)` doesn't work either.  Here's what did:

    sphinx.SetSelect('feeling, SUM(1) AS count')

Not the straight forward mysqlish syntax I've come to expect from Sphinx, but
it works.
