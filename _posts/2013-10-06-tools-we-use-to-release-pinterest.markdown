---
layout: post
title: "Tools We Use To Release Pinterest"
tags: [deploys, pinterest]
published: true
time: 6:55PM
comments: false
---
We have a fairly flexible Continuous Delivery system at Pinterest.  The tools
we use are fairly accessible, so you can build your own Continuous Delivery
system too.

* **[Github Enterprise][g]** is our version-control overlay.  It
  manages code-reviews, facilitates code-merging and most importantly
  has a great API.  The API let's us interact with our repository in
  a very clean programatic way.  For example we tag each deploy in git and
  are able to query it using Github's Repo API.
* **[Jenkins][j]** is our continuous integration system, we use
  it to package builds and run unit tests after each check in.
* **[Zookeeper][z]** manages our state.  It tells each node what version of
  code they should be running, it reports the status of what each node is
  actually running and it contains all our service configuration.
* **Amazon S3** is where we keep our builds.  It is a simple way to share data
  and scales with no intervention on our end.  It integrates fairly well with
  Jenkins.

All of these tools can be substituted and you'd still be able to achieve a
system similar to Pinterest's.  We chose these specific tools because we were
familiar with them.

These are the tools we use to create the release, the artifact we upload to S3.
To facilitate a deploy we have a series of deploy tools including a commandline
controller as well as a series of Zookeeper clients that live on each box that
needs updates.

If you are building a Continuous Delivery system let us know how you are
building it.

[g]: http://enterprise.github.com/
[j]: http://jenkins-ci.org/
[z]: http://zookeeper.apache.org/

