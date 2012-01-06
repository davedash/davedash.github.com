---
layout: post
title: "Naming things and a recursion"
tags: [django, mozilla, webdev, python]
published: true
time: 5:23PM
---

Most Mozilla webdev projects have an awful project structure, and it's
partially my fault.  I'm [attemtping to fix that][1], but I
cringe every time someone creates a new [playdoh][2]
(Mozilla's Django template)
based project.

### The typical python project

Your typical python project looks like this:

    /my_project
        someotherstuff/
        docs/
        theactualthingicareabout/
        setup.py
        LICENSE

### MOZtrosity

We didn't have a good guide when we first started writing Django projects, so
we opted for something like this:

    theactualthingicareabout/
        apps/
            foo/
            bar/
        __init__.py
        urls.py
        settings.py
        LICENSE

In otherwords, the Django Project, which is a python module, is immediately
checked out.  If you check this out to an invalid directory, e.g. you do something like:

    git clone github.com/davedash/myawesomeproject.git will.not.work\!

Bad things will happen.

### So?

To some people this seems like an easy thing to work-a-round, but when it takes
three of my excellent coworkers a week to diagnose an issue, where this ended
up being the root cause...  well it becomes a higher priority issue.

So here's what happened this week, when we tried to deploy
[the new careers site][3] to a VM hardware.

Our ops team sensibly checked out the project like so:

    git clone https://github.com/mozilla/lumbergh.git careers

They did everything right.  Sure, they were creative and chose `careers` over
the default `lumbergh`, but they knew the shortcomings of our system and picked
a name that would resolve as a valid python package.

Unfortunately we'd hit some *recursion error* anytime we tried to hit a URL.
So we knew there was an issue with the URL resolver, but we couldn't figure it
out.

Here's what the project layout looked like:

    careers/ # I could be called anything, but they chose careers
        __init__.py
        apps/
            careers/  # I'm going to cause problems,
                      # but neither devs nor ops will suspect a thing! mwahaha
                __init__.py
                models.py
                urls.py
                views.py
        settings.py
        urls.py


other files.

We configure our `apps/` directory to be part of our `PYTHON_PATH` so we can
do things like `from careers import views`... you can probably see where this
is going.

Here's the main `urls.py` [1][4]:

    ...
    urlpatterns = patterns('',
        (r'', include('careers.urls')),
    )
    ...

The main `urls.py` includes `careers.urls` which if you look at the above
project layout, resolves to two different python packages:

* `careers/urls.py`
* `careers/apps/careers/urls.py`

Python chose the first, and therefore `urls.py` kept calling upon itself.

### So what did we learn?

Do better.

First of all, we need a better project layout. This will continue to cause
problems for even the brightest developers.

Secondly, if you don't do this at least name apps carefully.
Django's app model can be a bit much for
non third party apps.  Sometimes there's one app which spans the entire
project, and it's tempting to call it the same name as the project
(e.g. `careers`), but sometimes a lamer more generic name like `common` is
better.

But really, the second point is moot if we just clean up.

[1]: https://github.com/mozilla/playdoh/pull/67
[2]: http://playdoh.rtfd.org/
[3]: https://github.com/mozilla/lumbergh/
[4]: https://github.com/mozilla/lumbergh/blob/master/urls.py
