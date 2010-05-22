---
wordpress_id: 130
layout: post
title: "Python, Named arguments: Pure Genius"
wordpress_url: http://spindrop.us/2007/12/21/python-named-arguments-pure-genius/
site: spindrop
---

I decided I want to learn python, if only to learn Django and to "get" what all the python hub-bub is about.

Python's named arguments in function calls is pure genius.  Let me explain.  

In PHP, and many other languages you can define a function as such:

	function foo($a = 2, $b = 2)
	{
		return pow($a,$b);
	}

If you follow, `foo()` will give you `4`.  `foo(3)` is `9` and `foo(99,0)` is `1`.  In python we can do the same thing, but it'll pay to use some better variable names:

	def foo(base=2, exponent=2):
		return base**exponent

Similarly `foo()` will give you `4`.  `foo(3)` is `9` and `foo(99,0)` is `1`.  But what if we forgot what the order was?  Did base come first or was it exponent?  We can do this:

	foo(exponent=99, base=2)

Since `base` and `exponent` both have default values, we can even omit `base` and let it use the default:

	foo(exponent=10)

This means rather than passing an `$options` array to my functions and checking whether an option was set or not, I can just specify which options I want in my function call.  Or instead of remembering the order of the arguments, I can use whatever order suits me.  Or instead of calling a function like `bar(null, null, null, 2)` I can just skip those first three arguments all together.

A side effect of this, is now there's a real use, even for simple functions, to give your variables easy to remember names.
