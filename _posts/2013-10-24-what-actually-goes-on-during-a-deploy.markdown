---
layout: post2
title: "What actually goes on during a deploy"
tags: [deploys, pinterest]
published: true
time: 8:33AM
---
Previously [I covered, at a high level, how our builds work][1] and [what tools
we used][2]. I wanted to
explain what exactly we are doing a during a deploy especially when it comes to
tracking state.  It's the one area where there aren't a lot of good off the
shelf tools that can just "do it for you."

A build can be deployed to a set of canary hosts, or to our entire fleet.  We
record this state in Zookeeper.

"Canarying" to a few hosts gives us time to validate that everything is working
as planned.  For the most part this involves looking at charts, error logs,
error aggregators, and clicking around on the site.  All very manual.

On each server sits a fairly robust Zookeeper client called `deployd`.  This
listens to either the `enabled` or `enabled/canary` Zookeeper node
depending on it's role (which
is also defined in Zookeeper).  If there is any change to these nodes a few
checks are performed:

* The node checks that it's serving the correct build.
* If it's not, it downloads the correct build and extracts it.
* It atomically flips a symlink on the node to point at the new build.
* It does any post-install steps, like installing dependencies.  For example we
  use pip to manage our python requirements so we do something like
  `pip install -r requirements.txt` after we've installed a new build.
* The service is restarted in the most graceful way.
* Current status of the node is reported back to Zookeeper.

Graceful restarts are somewhat complicated.  We employ different strategies for
different services.  In the most advanced form, multiple copies of the same
service are running on a machine.  Through `iptables` we are able to [turn off
traffic to a few instances while we restart them][o].  With most services we define a
restart concurrency that defines how many nodes will be restarted at any given
time.  In some cases we can restart almost all the nodes at once with no user
impact.

We can then monitor our deploy in our state-of-the-art deploy monitoring tool.

![deploy tool](http://cl.ly/image/250111163r0C/Screen%20Shot%202013-05-17%20at%203.30.18%20PM.png)

I'd like to point out that I'm no expert at [`curses`][c], but had the help of Erik
Rose's [blessings](https://pypi.python.org/pypi/blessings/) module which makes
light work of the terminal.

Ping me on twitter (@davedash) if you want to talk about the strategies you've
developed to deploy software at your organization.

[c]: http://docs.python.org/2/library/curses.html
[o]: http://owencoutts.com/blog/2012/12/02/A-better-deploy-strategy.html

[1]: /2013/10/12/how-we-deliver-features-to-pinners/
[2]: /2013/10/06/tools-we-use-to-release-pinterest/
