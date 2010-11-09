---
layout: post
title: "Using git to borrow from the future"
tags: [mozilla, git]
published: true
time: 1:58PM
---

One of the great features of ``git`` is the ability to re-order commits, break
commits into parts, and merge commits together.

Assuming that my `master` branch is a pristine copy of the site and an ancestor
of `mybranch` we can re-order commits by running:

``git rebase -i master``

This will take all the commits in your current branch (``mybranch``) that are
built upon ``master`` and allow you to reorder or edit them individually,
remove them or squash them.

For example you might get:

    pick 123abcd New feature supreme
    pick 123abce Whitepsace fixes
    pick 2222222 Rename functions.
    pick 123abcf rebase me

The last commit listed is the latest commit and is where ``mybranch``'s `HEAD`
points to.

You can edit this like so:

    pick 123abce Whitepsace fixes
    pick 2222222 Rename functions.
    pick 123abcd New feature supreme
    f 123abcf rebase me

This will re-order history so the first three items happen and the "rebase me"
commit just gets rolled into the "New feature supreme".  Note since this is a
rebase the commit hashes will change.  Let's say history is now this (reverse
chronological):

    323abcd New feature supreme
    3222222 Rename functions.
    323abce Whitepsace fixes

Great?  Almost.

There's a likely hood that your apps' unit tests will not pass after the commit
"Rename functions".  Some functions may have been renamed somewhere later in
``mybranch`` possibly in "rebase me" which is now a part of "New feature
supreme."

This is a mess, but we can run ``git rebase -i master`` again and edit the
"Rename functions." commit.  If you run a test-suite and things fail you can
"borrow from the future".  You see at this point ``Rename functions`` is
something that happened in the past.  ``mybranch``'s head is now
``New feature supreme`` which is the future.  We can pick and choose little
changes with some ``git``-fu.

While rebasing in the ``Rename functions.`` we might notice that we forgot to
rename a call, but we remembered to rename this call at some point in
``mybranch``.  We can simply do this:

``git checkout -p mybranch [paths]``

This will let you interactively select chunks of code from the head of
``mybranch`` and put it into your specific commit ``Rename functions.``.

You can narrow this down by specifying some ``paths``.

Once we finish rebasing we'll have a commit history that is logically ordered
and have all tests passing tests.

