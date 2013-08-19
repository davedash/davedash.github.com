---
layout: post
title: "Deploying software at Pinterest"
tags: [python, pinterest, deploys]
published: false
time: 10:01PM
---
**tl;dr** Pinterest Engineering is [SOA][soa] and we utilize S3, Zookeeper and
Python to keep our services up to date.

I'm one of the early members of the technical Operations team at Pinterest.
We build tools, setup services and otherwise assist our fellow Engineers
so they can deliver the best experience to
pinners as efficiently as possible.

One of my earliest tasks was to fix bugs in our deploy scripts.  I transformed
this task into an opportunity to define release engineering at
Pinterest as well as to create some solid release tools.

## An evolution of architecture

Within the last year and a half, Pinterest has moved from being a multi-tiered
architecture to a service oriented architecture.  We went from housing all of our
code in a giant repository to having multiple repositories with any number of
small services written in either Java or Python.

All through these changes our deploy tools and release infrastructure have had
to keep up and accommodate.  While at times accommodating these changes have
been frustrating, it has forced
our team of two "Release Engineers" to document better and build more robust
software.

## The Tools of the Trade

We use a variety of tools that are for the most part fairly accessible to most
companies.

* **[Github Enterprise][g]** is our version-control overlay.  It
    manages code-reviews, facilitates code-merging and most importantly
    has a great API.  The API let's us interact with our repository in
    a very clean programatic way.
* **[Jenkins][j]** is our continuous integration system, we use
    it to package builds and run unit tests after each check in.
* **[Zookeeper][z]** manages our state.  It tells each node what version of
  code they should be running, it reports the status of what each node is
  actually running and it contains all our service configuration.
* **Amazon S3** is where we keep our builds.  It is a simple way to share data
  and scales with no intervention on our end.

All of these tools can be substituted and you'd still be able to achieve a
system similar to Pinterest's.  We chose these specific tools because we were
familiar with them.

## The build pipeline

In practice, Pinterest is a continuous delivery\* shop.

![Pipeline](http://cl.ly/image/3k3E3U2X2A0J/Screen%20Shot%202013-08-18%20at%203.52.13%20AM.png)

Here's our build pipeline from the inception of a change to being served in
production.

1. An engineer makes a git branch.
2. She pushes it to her fork in Github Enterprise and submits a Pull Request.
3. Jenkins runs automated tests against her pull request (for services in our
   main repository).
4. After the request is approved it is merged (by the original engineer).
5. The newly integrated master branch triggers a Jenkins job that runs the same
   automated tests in step 3.
6. Upon success of the aforementioned job we have a build task that creates
   a tarball of the files and pushes it into S3.  We also branch this build in
   git as `jenkins-stable`.
7. Some systems are automatically deployed to (e.g. an internal copy of the
   site).
8. A deploy is then manually initiated.  We usually choose the same build that
   is currently `jenkins-stable`, but we can choose anything that's available
   in S3.

## The Deploy

A build that is deployed has two defined
states: It is either canaried or it is deployed everywhere.  This state is
recorded in Zookeeper to either `enabled/canary` or `enabled` node respectively.

"Canaried" means that we wish to have only a small subset of our fleet serving
the new build.  This gives us time to validate that everything is working as
planned.  For the most part this involves looking at charts, error logs, error
aggregators, and clicking around on the site.  All very manual.

On each node sits a fairly robust Zookeeper client called `deployd`.  This
listens to either `enabled` or `enabled/canary` depending on it's role (which
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
traffic to a few instances while we restart it][1].  With most services we define a
restart concurrency that defines how many nodes will be restarted at any given
time.  In some cases we can restart almost all the nodes at once with no user
impact.

We can then monitor our deploy in our state-of-the-art deploy monitoring tool.

![deploy tool](http://cl.ly/image/250111163r0C/Screen%20Shot%202013-05-17%20at%203.30.18%20PM.png)

I'd like to point out that I'm no expert at [`curses`][c], but had the help of Erik
Rose's [blessings](https://pypi.python.org/pypi/blessings/) module which makes
light work of the terminal.

[c]: http://docs.python.org/2/library/curses.html
[1]: http://owencoutts.com/blog/2012/12/02/A-better-deploy-strategy.html

## Design principles

Early on with my intern at the time, Owen, we setup some design principles.  We
were both [opinionated developers][2] so setting up some ground rules made
sense.

[2]: http://owencoutts.com/blog/2012/04/26/Code-Quality-and-Why-You-Care.html

### Don't touch the code directly.

Initially our deploy scripts lived in the same repository as the code we were
deploying.  This was painful.  I would update the deploy scripts, do a deploy
and lose my changes because part of the deploy meant doing some git
operations on the
repository I was working on.  Most of what we needed to do was simple tagging,
sometimes we needed to do compilation work.

Even after we moved our tools to their own repository, we still did repository
manipulations.  This was gross.  If someone wanted to deploy we could ruin
their working copy because we decied to muck with it.  Furthermore it was slow.
If we wanted to avoid issues, we'd have to do a clean `git clone`.

We moved all the git operations into Github API calls.  Any pull request that
removed a `subprocess.call(['git', ...])` and replaced it with a call to the
API was a winner in my book.  As a result our deploys sped up and we had less
requirements about from where we could deploy.

### Keep a consistent interface

For a while our release engineering team of two (me and my intern) handled the
majority of deploys.  Despite that other engineers would occasionally still
need to deploy.  We wanted the experience to be consistent regardless of ant
underlying
changes we
made.

Eventually my intern left and our team gained Nuo Yan who took over a lot of
the day-to-day build out of the tool.  We, then, started to transition deploys
from our team to other engineering teams who owned those services.  It was even
more
important that we kept some of the promise to these other teams.

We would have some services use a combination of SSH and `git` to do deploys,
while others used the S3/Zookeeper based approach we use now.  When we made a
service switch, we made sure that it was as minimally noticeable as possible.

The difficult thing about building tools is teaching people how to use them.
If you don't think ahead of time of how you want things to work, it can be a
chore to keep teaching people: "Oh now you do *X* instead of *Y*."

We also made services conform to *our* requirements.  Every service follows
roughly the same flow.  Whether it's in our main repository or not, or whether
it's python or Java is irrelevant to the tool.  Everything operates exactly the
same.  This helps our team not have to context switch when debugging issues.

### Design to make things easy for the deployer

Our plan has never been to keep things manual.  At every step of the game we
think, how can we make the deploy easier for the deployer.  After all, for some
time it was just us doing the deploys.  Doing 3-6 deploys a day was long and
arduous.  It did, however, force us to automate as much as we could.

We would write manual scripts which would validate if a deploy worked.  We would
then teach people how to run them.  We would then figure out a way for them to
get run automatically.  Eventually it would find itself as part of the main
deploy command.

Our plan is to continue to automate validations and any other manual steps.
Our eventual goal is that we can automate any decision making to the point
where we can remove the human element altogether.

### Crash early... Crash often

Our deploy daemon attempts to catch all exceptions inside eventlets and the
main thread and exit as
quickly as possible.  Rather than try to write complicated code that tries to
fix the state of things, we write code that crashes early.  We rely on a tool
called supervisor to restart our daemons.  This usually has a side effect of
fixing everything.

The last thing we wanted our code to do was to get to a point where it was in a
for-loop and needed to be `kill`ed.  Thanks to health checks that close this
loop, we can verify very quickly when a node is never coming up correctly and
bug fix then.  But this is rarely necessary.

&nbsp;

We probably have more design decisions than these listed, but these are some of
the main ones.  We never really wrote these down before the fact, but we would
discuss
them, and they would definitely come out in
code-reviews.  These don't need to be set in stone, but it helps to have some
idea of what things you are willing to do and what things you'd like to avoid
when building a tool.


## Our biggest challenges

We had a few challenges that we had to push through.  Some were necessary, and
some taught us some valuable lessons.

### Provisioning

We use puppet as part of our provisioning process.  A lot of our classes were
coupled in such a way that almost everybox had `rsync`'d a git checkout of our
code base.  Going forward we did not want to do that anymore.  So we spent a
lot of time refactoring our puppet code, decoupling where we could and having a
two provider system for providing our software:

1. The classic way of rsync'ing a git repository.
2. The modern way of using our `deployd` clients to pull the right version from
   S3.

To this day we have a lot of checks in place that determine whether we'll use
`rsync` or let `deployd` do it's thing.  As our puppet code base matures we
decouple this more and more, but we'll be happy when we have very clear
manifest files that don't try to stomp over each other.

### Configuration

Initially configuration was bundled with the tools.
This was cumbersome to update so we moved
service configuration into a configuration file.  To
update it we'd have to change the file and run puppet.  Some boxes might not
get the file, because of puppet failures, some boxes would get updates before
others.

Nuo rewrote the configuration to store everything in Zookeeper.  This meant
that if we had to change the number of hosts restarting at once to 200 from
100, we could do it instantly and not have to worry
if puppet ran successfully.

A design decision of our operations team in general is to have as few moving
parts for a given system as possible.  Taking puppet out of the equation made a
lot of sense.

### Python Packaging

Python packaging was only tangentially related to our deploy process.  Once upon
a time puppet used to run `pip install -r requirements.txt` ever few hours.
Unfortunately this was never right after a deploy, so we trained our engineers
that if they wanted to use a new package that they would have to deploy a
`requirements.txt` change, and then later deploy the code that used it.

This was horribly inefficient.  We later just had the deploy tools handle
python
package installation.  We learned a lot of things about the `pip` tool.  The
most important was that pip did not work great with system packages.  We also
found
an edge case where [sometimes the cached copies of files were bad][bad-cache].
We found many of these problems went away with `pip` 1.4 and have since changed
our entire fleet to use that version (rather than a mix of `pip`'s from 0.8-1.3.x).

We also were building a lot of system tools that had their own dependencies.
We now have the option to use `virtualenv` for our python services.  So they
don't conflict with our tools.

[bad-cache]: https://github.com/pypa/pip/pull/968

### New services

Pinterest engineering was moving to SOA fast, and new services would be
created while we were scrambling to fix bugs with our Zookeeper system and
to transition older services to Zookeeper.

One of our earlier new services forced us to document how to create a
Pinterest service and integrate it into the deploy tool.  This documentation
made it very clear to us how fragile our frameworks were.

Later on some of our services were being written in Java.  I naively assumed
this would just work, but when it came time to integrate I realized we had so
many assumptions about the code that we'd deploy:

* It would be from the same repository
* It would have the same monitoring tools.
* It would always be python

This forced us to write service configuration.  While it wasn't the code we
wanted to write, it was the code that we needed.  The service level
configuration made it easier for other teams to use our tools.  Eventually the
configuration made its way to Zookeeper, making the barrier to deployability
even lower.

More recently we deployed a new service that was in a different repository than
all our other python services.  This forced us to revisit all our assumptions
we made about deploying python.

Now we have a tool that's a bit more robust and useful for other teams.

## Current Issues

Despite all our valiant efforts we have some remaining issues.

Jenkins is slow for our main repository that houses most of our services..
Which is to say that we have a lot of tests, and many of them are slow.  While
this doesn't effect our deploys it does effect how fast we can
respond to problems.  Our strategy has been to find pieces of our code that can
be factored into libraries.  This means we move unit tests for those pieces of
code with the libraries which results in speedier builds.  Often we can find
slow tests through Jenkins' test profiling.  We will also
experiment with parallelizing builds across multiple executors.

Another issue we're having is some services after restart perform poorly after
the first few requests.  We are continually investigating ways to warm up our
services so our deploys can be more stealthy.

The other major issue is S3 and our build sizes.  Our largest build is nearly 200MB
and can take quite some time to download.  A download can take 30 seconds when
S3 is behaving, or sometimes several minutes.  We've recently instrumented our
tools, and will focus on cutting this number down.

## Other directions

As I mentioned earlier, there were a lot of options that we could have chosen.
In fact, we never really discount any options.  We went with python because
that's what the scripts originally were written in.  If we started over, we
might consider something like Go.

For downloads we might look to a tool like
[Herd](https://github.com/russss/Herd) which uses BitTorrent to distribute
code rather than S3.

We might even decide that changing machines in place isn't serving us well, but
perhaps adding baked AMIs into our deploy infrastructure is something that we
want.

We have a lot of options for these tools going forward.  We'll continue to
collect data, optimize and repeat.

## Final thoughts

While some of this process suffers from NIH, existing tools for deploying
didn't seem to meet our needs.  We'd love to one day pull the
Pinterest-specific bits out of our tools and open source them.  In the meantime
if you have questions feel free to contact us.

Of course, if you like solving problems like these, join our team that helps
give Pinners the best experiences as quickly as possible.

\* Continuous delivery means that your master branch of code is always deployable.

[soa]: http://en.wikipedia.org/wiki/Service-oriented_architecture
[g]: http://enterprise.github.com/
[j]: http://jenkins-ci.org/
[z]: http://zookeeper.apache.org/
