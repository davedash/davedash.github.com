---
layout: post2
title: "How We Deliver Features to Pinners"
tags: [python, pinterest, deploys]
published: true
time: 10:01PM
---
Previously we discussed [what tools Pinterest uses for deploys][2].  This
article shows how we connect them to one another in order to create a
"pipeline."

In practice, Pinterest is a continuous delivery shop.  That means at any given
time we are able to serve the latest code our engineers have deemed ready.  In
practical terms that means we can create features and fix bugs and deliver them
to pinners in the same day if not within the same hour.

![Pipeline](http://cl.ly/image/3k3E3U2X2A0J/Screen%20Shot%202013-08-18%20at%203.52.13%20AM.png)

Here's our build pipeline from the inception of a change to being served in
production.

1. An engineer makes a `git` branch.
2. She pushes it to her fork in Github Enterprise and submits a
   [Pull Request][1].
3. Jenkins runs automated tests against her pull request (for services in our
   main repository).  To facilitate this we use a lightweight webapp called
   [Leeroy][l].
4. After the request is approved it is merged (by the original engineer).
5. The newly integrated master branch triggers a Jenkins job that runs the same
   automated tests in step 3.
6. Upon success of the aforementioned job we have a build task that concats and
   minifies assets, pulls in translations and creates a tarball of the files
   and pushes it into S3.  We also branch this build in git as
   `jenkins-stable`.
7. Some systems are automatically deployed to (e.g. an internal "bleeding edge"
   version of the site).
8. For other services, a deploy is then manually initiated.  We usually choose
   the same build that is currently `jenkins-stable`, but we can choose
   anything that's available in S3.

There is a potential for redundancy in step 5.  It is entirely possible that
the branch of an engineers' code we test will be cleanly merged onto "master"
thus avoiding the need for testing of integrated code.

Currently in this pipeline running our automated tests is the slowest step.

[1]: https://help.github.com/articles/using-pull-requests
[l]: https://github.com/litl/leeroy
[2]: /2013/10/06/tools-we-use-to-release-pinterest/
