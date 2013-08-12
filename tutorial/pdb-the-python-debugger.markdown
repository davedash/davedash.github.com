---
layout: tutorial
title: pdb, the Python Debugger
---

Sometimes it's nice to get down and dirty with your code and just figure out
exactly what it's trying to do.  Luckily `python` provides us with `pdb` the
`python` debugger.  This tutorial will get you started with it.

## tl;dr

Add `import pdb; pdb.set_trace()` to your code at points where you want to
debug.  In the debugger you can `step` into code and you can execute arbitrary
statements by prefixing them with `!`.

For details, continue reading.

## Naive debugging

Let's assume for a moment that you have a new `virtualenv`.  If you've
completed the [`virtualenv` tutorial][v] you can create a temporary one like
so:

    mktmpenv

Let's make a python script called `foo.py`:

    def sum_of_squares(a, b):
        c_squared = a^2 + b^2
        return c_squared


    if __name__ == "__main__":
        print sum_of_squares(3, 4)

**Note**: The mistakes above are for demonstration purposes.

Our expectation is that we'd get the number 25, but instead we get 7 when we
run this program.

A naive debugging strategy is to litter the code with `print` statements:

    def sum_of_squares(a, b):
        a_squared = a^2
        b_squared = b^2
        print a^2
        print b^2

        c_squared = a^2 + b^2
        print c_squared
        return c_squared


    if __name__ == "__main__":
        print sum_of_squares(3, 4)

This certainly works, but it has it's limitations.  For one, if your script
produces a lot of output, you might miss those printed items.  Secondly you
might forget what variable is what so you may add more `print` statements.
Eventually you'll be overwhelmed with `print` statements, figure out your bug,
and then carefully undo all the `print`s that you used for debug.

For our contrived example that might not be a problem, but hopefully you are
writing complex and challenging code that could benefit from more.

## Enter `pdb`

`pdb` lets us debug items interactively and step into functions to follow what
our code is doing.  We can take our original example and augment it by doing
the following:

    def sum_of_squares(a, b):
        c_squared = a^2 + b^2
        return c_squared


    if __name__ == "__main__":
        import pdb; pdb.set_trace()
        print sum_of_squares(3, 4)


Now I get the following:

    » python foo.py
    > /private/tmp/foo.py(10)<module>()
    -> print sum_of_squares(3, 4)
    (Pdb)

You can use `?` to get help, but the arrow indicates the line that's about to
be executed.  At this point it's helpful to hit `s` to step into that line.

    (Pdb) s
    --Call--
    > /private/tmp/bar.py(2)sum_of_squares()
    -> def sum_of_squares(a, b):

This is a call to a function.  If you want an overview of where you are in your
code, try `l`:

    (Pdb) l
      1
      2  -> def sum_of_squares(a, b):
      3
      4             c_squared = a^2 + b^2
      5             return c_squared
      6
      7
      8     if __name__ == "__main__":
      9         import pdb; pdb.set_trace()
     10         print sum_of_squares(3, 4)
    [EOF]
    (Pdb)

You can hit `n` to advance to the next line.  At this point you are inside the
`sum_of_squares` method and you have access to the variables in it's scope,
namely `a` and `b`.  You can view those by doing `!a` or `!b`.  Here's some a
snippet of debugging:

    (Pdb) n
    > /private/tmp/bar.py(4)sum_of_squares()
    -> c_squared = a^2 + b^2
    (Pdb) !a
    3
    (Pdb) !b
    4
    (Pdb) !a^2
    1
    (Pdb) !b^2
    6

We can see that the `^` operator is not what it seems.  We might even recall
that in many computer languages what we want is the `**` operator to do
squares:

    (Pdb) !a**2, b**2
    (9, 16)

Voila!  We were able to step in and around the execution paths of our code and
successfully debug our software.


[v]: /tutorial/virtualenv

## Final thoughts

Get familiar with the `python` debugger.  It'll let you be able to interact
with your code immediately instead of waiting for you to re-run your code and
add new `print` statements.
