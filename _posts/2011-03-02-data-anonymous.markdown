---
layout: post
title: "Data Anonymous"
tags: [mysql, security, mozilla]
published: true
time: 11:42AM
---
[s]: https://github.com/davedash/mysql-anonymous

I wrote a simple database [scrubber script][s].  It takes a `yaml` file that
describes what scrubbing needs doing and then outputs `sql` that you can send
to `mysql`.  It's dreadfully simple and I'd like to see if others can make use
of it.

At Mozilla we have a lot of contributors and would like them to have access to
realistic data since many of our bugs are based on certain states within the
data.
