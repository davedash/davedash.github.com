---
layout: post
title: "DjangoCon Testing Tutorial"
tags: [mozilla, djangocon, django, testing]
published: true
time: 1:36PM
---
<div class="side">
   <img src="/static/images/2011/08/10/djangocon.png"
        width="287" height="184"
        alt="DjangoCon 2011" />
</div>

If you want to learn all you can about testing anything in your Django App, see
[my tutorial][t] at [DjangoCon][d].
It's on September 5th, it'll be 3 hours
long and so far with seven sign ups it will be very hands-on.

Here's what I think I will cover, but I may change this depending on what the
audience wants:

* Testing issues
    * ask people to fill out etherpad with issues they've run into
    * ask someone to rank them in order of complexity
* List an outline of topics
    * post them on etherpad
    * have people + them if they are interested
* Testing overview
    * We started in late 2009 early 2010
    * Our largest project has 2500 tests
    * Our next largest has 1100
    * We have pretty good coverage
* How testing works    in Django
    * I'm not 100% sure on this
    * Test runner setups up a new database
    * Test runner finds and runs tests
    * Tests run class setup
    * Test runs each test in a test case
        * Load fixtures
        * Tests run setup
        * Tests runs the test
        * Tests runs teardown
    * Tests run class Teardown
    * You get an F if you're bad and a . if your not.
    * Now that you know it, you can hack it.
* How we've hacked testing
    * 2500 tests is a lot
    * We no longer recreate the database when you run the test suite
    * In each test case we just load the fixtures once.
    * We rearrange the tests so things with the same fixture set run together
* Testing tools that we use at Mozilla
    * nose/django_nose
    * nose plugins
        * nicedots
        * progressive
    * coverage
        * git + whatchangedpy
* Testing everything, no excuses
    * 100% Coverage isn't important
    * 80% is nice
    * Good coverage on tricky things is important
    * Some coverage on everything is important
    * External
    * If you start depending on APIs, Search or different tools you need to be able to test for them.
    * Writing these test cases will take less time than this tutorial
    * It will save you so much headache in the future.
    * The same headaches you save yourself by writing "normal" tests
    * Mock easy things
        * use a decorator on any test/view that might use redis
        * if redis isn't setup, use the mock client
        * mock client doesn't support everything,
            * just what I need to get my tests running -
            * feel free to extend it if you use it
        * Testing Redis
    * Setup/Teardown for complicated tools
        * Good for search and APIs
        * Raise SkipTest (nose) if the developer doesn't want to run these tests
        * Non realtime tools
            * Testing Sphinx search
            * SetupClass
                * load fixtures
                * run indexer
                * run server
            * Sphinx server now available for all tests in your test case
            * Teardown
                * stop server
        * Real time tools
            * Nicer, data can be added in post_save signals or elsewhere in your app
            * Testing LDAP
                * Setup
                    * Remove LDAP files
                    * Load an ldif
                    * Start slapd
                * Your code can now touch LDAP
            * Testing ElasticSearch
                * We leave ES running all the time.
                * Setup
                    * Checks for ES support or SkipTest
                    * Deletes index
                    * Creates index
                * You can now read/write to ES
                * Teardown
                    * Delete's index
    * Fixtures
        * Fixture Magic
        * Model Maker
    * pitfalls
        * dates
        * using PDB


[t]: http://djangocon.us/schedule/presentations/30/
[d]: http://djangocon.us/
