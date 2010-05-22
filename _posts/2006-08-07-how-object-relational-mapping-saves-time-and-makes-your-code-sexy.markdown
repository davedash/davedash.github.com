---
wordpress_id: 61
layout: post
title: How Object-Relational Mapping saves time and makes your code sexy
wordpress_url: http://spindrop.us/2006/08/07/how-object-relational-mapping-saves-time-and-makes-your-code-sexy/
site: spindrop
---
[orm]: http://en.wikipedia.org/wiki/Object-relational_mapping "Object Relational Mapping on Wikipedia"
[symfony]: http://symfony-project.com/
[propel]:  http://propel.phpdb.org/
[Object Relational mapping][orm] is a way of transparently interacting with a relational database by using objects.  Each database table is a new class and each row in the table is a single object.  Relations between tables are now relations between classes.

It wasn't until I started using [symfony][] and [propel][] that I started appreciating [ORM][].  I started working on significant projects and the time it would take me to do things went down quite a bit.  Prior to [Propel][], I had a lot of library files that would store and retrieve information for me.

	class lib {
		function valid_user($username, $pw)
		{
			$q = "SELECT id FROM user WHERE username LIKE '$username' AND password LIKE '$pw'";
			return DB::do_query_select_one($q);
		}
	}

Not too bad, but a lot is buried in my hypothetical `do_query_select_one` function.  Let's compare this to the <acronym title="Object Relational Mapping">ORM</acronym> ([propel]) version:

	class myTools {
		public static valid_user($username, $pw)
		{
			$c = new Criteria();
			$c->add(UserPeer::USERNAME, $username);
			$c->add(UserPeer::PASSWORD, $pw);
			return UserPeer::doSelectOne($c);
		}
	}

That's a lot of extra writing, and as someone who's quite proficient in <acronym title="Structured Query Language">SQL</acronym>, you can see why I initially laughed it off.  <!--more--> Let's take it a step further.  Sure we have twice as many lines of code, but what would the calling functions do after they check to see a user is valid or not?

### Related Objects

In our non-<acronym title="Object Relational Mapping">ORM</acronym> world we would attempt to iterate through each row. find some corresponding <acronym title="Access Control List">ACL</acronym> table and add all these elements to a session variable.  This can get old fast.  Let's see how that would look:

	if ($user = valid_user($_POST['username'], $_POST['pw'])) {
		// $user we populated from our made-up 
		// DB::do_query_select_one function.  Let's pretend that's easy.
		$id = $user['id'];
		$sql = 'SELECT group FROM acl WHERE user_id = ?';
		$ps = prepare_statement($sql, $id);
		// ...
 	}

That's neat, but in the <acronym title="Object Relational Mapping">ORM</acronym> world we do it like this:

	if($user = valid_user($_POST['username'], $_POST['pw']))
	{
		$user->getACLs();
	}

All the extra database calls are safely encapsulated in our class.  No worries.  It's just a one-liner.

### Putting things into functions

Another neat trick is putting some redundant code into simple functions.  By using a criteria object, you can cleanly create some functions that take an input criteria and return one with specific parameters:

	function securify(Criteria $c)
	{
		// makes sure the user is still valid
		$c->add(User::EXPIRES, time(), CRITERIA::GREATER_EQUAL);
		$c->add(User::VALID, true);
	}

Now all we need to do every time we call a user is call `securify` on the `Criteria` object to make sure we have a valid user that hasn't expired.

### Deleting objects

Getting rid of data: `$user->delete()`.

### Customizations are saved

Let's say you want the `User` object to have some customizations.  Any of those customizations will persist even after you change the model, since `User` inherits from a `BaseUser` class which is dynamically generated from a defined schema.  This can save a *ton* of time when your model changes.  Instead of finding every instance of a call to see if a user is logged in, you can change your custom classes and not have to worry.  If this had been the case for me, I'd have saved myself and my client a few hours of coding.

### Conclusion

<acronym title="Object Relational Mapping">ORM</acronym> relegates the database to simply being a store for persistent objects.  What this means is you no longer need to rely on half-baked <acronym title="Structured Query Language">SQL</acronym> queries to save and load objects.  You can let the objects take care of that themselves, without worrying about the database back-end.  This allows you, the programmer, to do your job of manipulating objects to execute the goal of a web site.  Enjoy.

