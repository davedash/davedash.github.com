---
wordpress_id: 350
layout: post
title: Making our tests run thrice as fast
wordpress_url: http://spindrop.us/?p=350
site: spindrop
tags: [spindrop, mysql, django, mozilla, sphinx, testing]
---
[ttc]: http://github.com/jbalogh/test-utils/blob/c4c31905a95e59dcc8919c1030b23848ad7fbca6/test_utils/__init__.py#L57
[tu]: http://github.com/jbalogh/test-utils
[z]: http://github.com/jbalogh/zamboni/
[ian]: http://blog.ianbicking.org/

I've written a faster version of [TransactionTestCase][ttc] and packaged it with [test_utils][tu].  It's mysql specific since it relies on `SET FOREIGN_KEY_CHECKS=0` to flush the database.

The long story...

<!-- more-->

### Why speed matters

We're closing in on 300 tests for [Zamboni][z].  As of yesterday, to run our entire test suite it would have taken approximately 5 minutes.  If you run tests before code-reviews, during a code-review, and before you push to master - you've spent about 15 minutes doing tests for a single feature or bug-fix.  We have about 5 developers, so this cycle happens many times in a work day.  In that time many sandwiches can be made and consumed.

Even shortcuts, like running a subset of tests will only go so far, and ultimately we do want to validate that all our tests pass for any code-change.


### Testing Sphinx search with `TransactionTestCase`

Django recently sped up testing by running tests in a transaction.  However, this means that data never gets committed to the database and therefore external tools, like the Sphinx indexer, will never see any of that data.  So we resort to `TransactionTestCase` which *will* commit the data.

Unfortunately `TransactionTestCase` is painfully slow.  The accepted practice is to only use `TestCase` if you want your tests to be fast.  So, I decided to complain to [one of our new hires][ian] and he and I decided to tinker in mysql to figure out what was slow.  We discovered the following:

* `delete from [table] is slow`
* `truncate [table] is slow`
* ... unless you `SET FOREIGN_KEY_CHECKS=0`

So we decided we should do our own tear down.  After some tinkering with `cProfiler` I discovered that `TransactionTestCase` does a (slow) database `flush` on setup for a test case.  This wouldn't do.

### Making our own `TransactionTestCase`

I decided to make our own `TransactionTestCase` and it would just run `SET FOREIGN_KEY_CHECKS=0` and `TRUNCATE` on each table at tear down time.  It would also not do a `flush` on set up.

We write our tests with the idea that they clean up after themselves.  Rather than having them cleanup after the last test.  This is a requirement for us since `django-nose` doesn't reorder tests (nor should it) and a standard `django.test.TestCase` assumes a clean database.

Looking at a single test `test_sphinx_indexer`, using `django.test.TransactionTestCase` took ~30 seconds.  Using our new `TransactionTestCase` it takes ~4 seconds!

### Fast tests are good

We can now run our 275 tests in ~100 seconds versus the ~300 seconds it used to take.  Furthermore, skipping our sphinx tests (which are the only tests that use `TransactionTestCase`) only saves us ~10seconds.  That's not a lot of overhead for better coverage.

This took me the better part of a day, but solving this now, means we're going to more often than not run our sphinx tests all the time rather than skip them.  Our QA team will assure you that search is probably the most regression prone part of our site, so running these tests are vital to quality.

If you need to use `TransactionTestCase` in mysql, [give ours a try][tu].
