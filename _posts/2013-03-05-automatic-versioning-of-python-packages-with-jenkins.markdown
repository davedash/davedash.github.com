---
layout: post
title: "Automatic versioning of python packages with Jenkins"
tags: [python, jenkins]
published: true
time: 8:40AM
---
# Automatic versioning of python packages with Jenkins

I maintain a few internal python libraries at Pinterest, and for some of them, we try to maintain properly versioned pip packages.  There's no real method to my madness of versioning things, I start with `0.1` and if I need to make changes that require me to reinstall the package somewhere we'll soon see a `0.1.1`.


Occasionally there'll be a big change, maybe a new script, and we'll see ``0.2.0``.

The small changes, however got obnoxious.  My workflow would be like this:

1. Run my package.
2. Find a bug.
3. Fix the bug.
4. Increment the version.
5. Build a package.
6. Reinstall package.

Repeat if necessary.

At least step 5 was automatic, Jenkins happily will run ``python setup.py sdist`` and upload those bits to S3.  Step 4 was a bit annoying, since it was often editing ``setup.py`` to change the version number.

So I changed some things around.  Jenkins uses nice monotonically increasing numbers.  Part of my build step involves doing this:

```
echo $BUILD_NUMBER > build.info
```

``build.info`` gets packaged with my library by adding it to the ``MANIFEST.in`` file.

In ``setup.py`` I do the following:


{% highlight python %}

def __path(filename):
    return os.path.join(os.path.dirname(__file__),
                        filename)

build = 0

if os.path.exists(__path('build.info')):
    build = open(__path('build.info')).read().strip()

version= '0.6.{}'.format(build)

{% endhighlight %}

I can then pass ``version`` to the ``setup()`` method.

Now my version numbers are ``0.1.$JENKINS_BUILD`` which eliminates step 4 in my bug fix cycle.  The one downside is this number will never reach "0", so if I do a major change I'll jump from ``0.1.12`` to ``0.2.13``.  That functionally works for me, but I'd love to improve this.
