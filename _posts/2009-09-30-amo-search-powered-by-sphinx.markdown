---
wordpress_id: 319
layout: post
title: "AMO Search: Powered by Sphinx"
wordpress_url: http://spindrop.us/?p=319
site: spindrop
tags: [spindrop, search, mozilla, amo, addons.mozilla.org, sphinx, amochi09, chicago]
---
[g]: http://spindrop.us/2009/09/19/mysql-and-the-grand-regexp-retardedness-with-lettercasing/
[v]: http://spindrop.us/2009/08/07/v-is-for-version-hell/
[b]: http://spindrop.us/2009/06/18/question-building-a-better-search-engine/
[m]: https://wiki.mozilla.org/AddonMeetups:2009:Chicago
[a]: http://addons.mozilla.org/

Last night, I gave a talk at the [Addons Meetup][m] at Threadless HQ in Chicago on the new search engine powering [addons.mozilla.org][a].  I'll recap the technical portion of the talk and give a bit more details.

First, I'd like to thank Harper and Threadless.  It was a great location in the greatest city in the universe.  Before and after the meetup, Harper was just an all-around great guy to hang with and the threadless headquarters was a nice hangout place for meeting people interested in addons.

Shortly after my talk, our Engineering Ops team deployed the new AMO 5.1 complete with a new Sphinx powered search engine.

So let's talk about search.  Note: parts of this are a rehash of my talk, so feel free to skip around.

<!--more-->


### A bit about addons 

Addons is a huge growing space.  Arguably it's Mozilla's best kept secret.  Sure readers of this blog probably know what Addons are, but ask people who aren't as web-savvy.  Most people don't know what a browser is - and it's hard to explain it to people without getting technical.

We can just skip that step.  Because Addons are small things that people can easily "get".

"It's an easy way to customize the internet when your surfing." 

While perhaps not technically correct, its one way of explaining it to people.  Maybe a better way is just showing people what they can do with addons.

On my flight out to Chicago, I talked to a person on the plane who didn't know what a browser was, but after showing her [AMO][a] she was really intrigued.

If everyday non-technical people can realize the potential of addons, it's only a matter of time before they start knocking down the doors to AMO.

So we better be prepared to handle them, and get them what they want.

### The technical details of addons.mozilla.org

Everytime you open Firefox, it pings [AMO][a] to see if there's any updates to any of the addons that happen to be installed.  Over a third of the people using Firefox have at least one addon, and Firefox is roughly 22% of the browser market.  That means roughly 7% of people opening their browsers are pinging our servers for updates.

Needless to say it's a lot of traffic, and to support it we need a fair amount of hardware.  AMO is clearly the largest site in the Mozilla universe in both respects.

Some stats:

* 1 mySQL master
* 4 mySQL slaves
* 2 memached servers
* 2 Sphinx indexer/search daemons
* 24 Web Frontend
* Multiple Zeus ZXTM clusters all

Most of this is standard, we'll talk about Sphinx later, but Zeus is amazing.  I didn't know what Zeus was until earlier this year when I interviewed with Mozilla's VP of Engineering Operations.  All our requests get cached so much of our hits actually hit our Zeus cluster and not our web servers.

To see just how amazing they are read our [mrz's ops blog](http://blog.mozilla.com/mrz/).

### Why search matters

If you have any kind of custom content and unique meta data a custom search solution is a must.  Browsing through a site isn't going to cut it.  Browsing is dead.  Search is how you find things on a web site.  On [AMO][a] you may see an addon that's featured somewhere, or you might want to see what's out there, but the right search query will find you the right addon in two clicks.

### Improve Search

So my first job on AMO was to [improve addons search](https://bugzilla.mozilla.org/show_bug.cgi?id=498999).  It was a vague request and born out of frustration with what we had.  It wasn't a problem that certain things were indexed, or unicode didn't work, or results weren't sorted.  We may have had all those problems, but as a product search needed to be replaced.

To me it meant that we needed some framework that would allow developers to quickly debug and fix any future search calamities at a moments notice.

So here were the goals I made for myself:

* Do something that sucks less than what we’ve got
* Do something that makes it easier to suck less in the future
* Do something that’s easy to use for our operations team, web developers and most importantly, end-users
* Reduce strain on our databases, developers and operations teams

### Complex Data

Our data set is small (we have 5,000 addons), but there's a lot of secondary meta data about the addons that we track:

* Addons work in 1 or more locales (e.g. en-US, fr, de, etc)
* Addons are optionally platform specific (Linux, OS X, etc)
* Addons work with one or more products (Firefox, Thunderbird, Seamonkey, Sunbird or Fennec)
* Addons come in multiple flavors (extensions, themes, dictionaries and more)

We want to index all this data.  Unfortunately to get at much of this data it involves either numerous queries, or numerous joins which put a strain on mysql.  How much strain?

At peak we get about 10 search queries per second.  If we do something smarter this won't have to cause a lot of strain.

### Using Sphinx

Sphinx is an open source search indexer and daemon.  It's used by Craigslist, the Pirate Bay and [Mozilla Support](http://support.mozilla.com).  It was very easy to use and despite a complicated set of data and business logic, Sphinx was up to the task.

### The challenges

We needed to search for addons in several languages.  So indexing just addons wouldn't work, we need to make sure we have every translation of every addon indexed.  For those counting, we have 5,000 addons, but 18,000 translations of addons.

All the joining and filtering that needed to be done for our old search still needs to be done, but we can do this all in one shot by using a mysql view.  This view is a flat list of each translated addon as well as all meta data associated with it.  This then gets fed into the sphinx indexer.

Along the way we ran into some issues which used to be dealt with outside of mysql, such as comparing versions.  It was gross and quite a hack, so we turned the variety of [acceptable version strings into integers][v].  

We also learned that stemming wasn't a good idea as we assumed it would be.  Stemming was great for searching through lots of text, but a great deal of addon searches were really just searches for product names, so we opted for substring searches.  We'll see how that fares.  There is probably room for improvement.

Much of this, however involved knowing our data, and knowing how it will be used by our users.  Once we got that down, we could hammer it all out using Sphinx.

### Wins

So Sphinx gains us a bit architecturally.  We have a complicated query, but it only gets run once every 5 minutes versus the 180,000 times it was run "on demand."

Indexing happens rather quickly, just over a minute.

The API was a breeze to work with, and was easy to drop into our own codebase.

Because of our relatively small data set, and quick indexing, we're able to scale this simply by cloning and load balancing.  Meaning, we just need to scale for traffic, but addon growth (which is slower than traffic growth) we can safely not worry about for a while.

Our ops team can monitor the sphinx clusters and just deploy additional nodes as needed.

### Building a platform

What we've done is built a foundation for search.  Not all the problems are gone, but a lot of the problems that our QA team finds are able to be resolved quickly.  We have a nice pile of unit tests as well that help us keep our results in check when we start tweaking dials.

We even have the groundwork for some nifty advanced search syntax, that hopefully we can inject into future releases of AMO.

Enjoy.  And if you find anything, [let me know](http://bit.ly/search-bugs).
