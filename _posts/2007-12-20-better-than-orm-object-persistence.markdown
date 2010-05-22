---
wordpress_id: 129
layout: post
title: Better than ORM Object Persistence
wordpress_url: http://spindrop.us/2007/12/20/better-than-orm-object-persistence/
site: spindrop
---
 After talking to people about the benefits and disadvantages of various ORMs... and reading up a little on non RDMBSs like [Amazon SimpleDB](http://www.amazon.com/gp/browse.html?node=342335011) I came to the realization that ORM is really a hack to get RDBMSs to work as a storage for objects.

I'm being liberal with the term hack.  It really does work for a lot of situations, but it's not very elegant.  The workflow is more or less this:

* You create a database.
* You create some objects
* You define tables to store attributes of objects
* You establish a mapping

There's a lot that goes into database definition.  It would be nice to breakout from this line of thinking and do things a bit differently:

* Create database
* Save named (e.g. Person, Place, Log, Restaurant, Rating, Review) serialized objects to the database.

Let the database learn from the saving of the object how to define the type.  In fact, it should be flexible and let us have mixmatched types, etc.

Let the database index everything, and keep the indexes up to date, but prioritize it based on usage.  In other words if we usually query a database of Persons in order by a field called lastname, then make sure that index on lastname is always at hand.  We should be able to query this data back out of storage based on how we stored it.

We should also be able to reach other objects in the database in a similar manner.

The key here is letting the database layer do the heavy-thinking about what to do with serialized data, versus having some middle layer take care of it.

...

so I might just be naive about data and databases.  But if this idea is worthwhile and some database people can validate me, I'd be willing to work on it.
