---
wordpress_id: 293
layout: post
title: V is for Version Hell
wordpress_url: http://spindrop.us/?p=293
site: spindrop
tags: [spindrop, search, versioning, mozilla, addons.mozilla.org, sphinx]
---
[t]: https://developer.mozilla.org/en/Toolkit_version_format

Versioning is quite difficult to deal with.  Versions are nearly-numbers, but you can't quite sort them using standard numerical algorithms.

While the following is true:

	1.1	< 1.2

The following is also true:

	1.2	< 1.18 < 1.20

The "." is not a decimal point but a separator.

Mozilla uses a modestly complicated [versioning system][t] that involves stars, plusses, and sometimes "x".

I found a very convoluted way to translate these versions into large integers.  The versions for applications in the AMO database have four parts at most, they are potentially alpha or beta and potentially a pre-release.  In some cases we have multiple versions represented with `.*`, `.x` or `+` at the end.
<!--more-->
The [Toolkit docs][t] let us translate "+" to mean "pre-release of the next version".  E.g. 1.0+ is 1.1pre0.  Since my primary purpose of all this is for sorting, `.*` and `.+` may as well just be a very large "version part."  Since all the version parts I deal with are a maximum of 2-digits, I turned `.*` and `.+` into `.99`.

For example:  
	3.5+ => '03'+'05'+'99' => 030599

We also need to deal with versions that may be alpha, beta or not.  If everything else is equal:

	3.5a < 3.5a5 < 3.5b < 3.5b2 < 3.5 < 3.5+

We assign a single integer to represent a version's "non-alphaness":

	a => 0
	b => 1
	non alpha/beta => 2

We assume that `3.5a = 3.5a1`.  Therefore:

	'3.5a => 3.5.0a1 => '03'+'05'+'00'+'0'+'01' => 030500001

Similarly if it's a pre-release we assign a 0 or 1 to represent "non-pre-releaseness":

	'3.5a pre2 => 3.5.0a1pre2 
	=> '03'+'05'+'00'+'0'+'01'+'0'+'02 
	=> 030500001002

So what does this get us?  Integers which we can use for comparison, sorting, etc.  It's a one time calculation for each version and we can do some nice SQL statements in AMO like:

	mysql> SELECT version,version_int FROM appversions WHERE application_id = 1 ORDER BY version_int LIMIT 15;
	+---------+--------------+
	| version | version_int  |
	+---------+--------------+
	| 0.3     |  30000200100 | 
	| 0.6     |  60000200100 | 
	| 0.7     |  70000200100 | 
	| 0.7+    |  80000200000 | 
	| 0.8     |  80000200100 | 
	| 0.8+    |  90000200000 | 
	| 0.9     |  90000200100 | 
	| 0.9.0+  |  90100200000 | 
	| 0.9.1+  |  90200200000 | 
	| 0.9.2+  |  90300200000 | 
	| 0.9.3   |  90300200100 | 
	| 0.9.3+  |  90400200000 | 
	| 0.9.x   |  99900200100 | 
	| 0.9+    | 100000200000 | 
	| 0.10    | 100000200100 | 
	+---------+--------------+
	15 rows in set (0.00 sec)

I can now index these integers using Sphinx and do some very easy searches for addons based on version number.
