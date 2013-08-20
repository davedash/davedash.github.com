---
layout: tutorial
title: An Introduction to Python Virtualenvs
---
When you are developing python you'll end up using third party libraries.  The preferred way to acquire these is by using `pip`.

`pip` out of the box will install things as system packages.  While this is helpful there are two problems with this:

* Not every library you'll download should be installed as a system package
    * You might need specific versions of specific libraries
    * You might have bad packages that don't uninstall cleanly
* You will need to install every package using `sudo` which can be annoying and cumbersome.

Luckily there's an easy way around this.  `virtualenv` creates virtual python environments with their own isolated set of packages.

If you are on a Mac, I suggest the following for your environment:

* [`Homebrew`][b]
* `virtualenv_wrapper`

**Note**: If you are not on a Mac you can omit the `Homebrew` step.  Unfortunately if you are on Windows, I'm not sure what good options are other than to use something like [VirtualBox][v].

## Installing Homebrew

[Homebrew][b] is a commandline package manager for OS X.  It's more often than not what you want to use to install any system level packages and tools like, python, ruby or wget.

The installations is fairly simple:

```
ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"
```

More details are available on the [Homebrew homepage][b].

Once this is installed you'll want to brew a python installation (in favor over the default python that ships with OS X):

```
brew install python
```


## Installing `virtualenv_wrapper`

`virtualenv` has a nice companion package called `virtualenv_wrapper`.  Installing it will give you a rich set of tools to switch between virtual `python` environments.

To install this tool:

```
sudo pip install virtualenvwrapper
```

**Note:** This is the one time where you want to install something with `pip` while using `sudo`.  The reason being is that `virtualenvwrapper` is something that you *do* want as part of your system packages.

You'll want to add the following to your `.profile` (or `.bashrc` or `.zshrc`):

    export WORKON_HOME=$HOME/.virtualenvs
    export PROJECT_HOME=$HOME/Devel
    source /usr/local/bin/virtualenvwrapper.sh

More details are found [here][vw].

You'll want to log out and log back in, or run a command like:
`source ~/.bashrc`.  This will give you all the special features of
`virtualenv_wrapper` into your shell.

## Working on projects

Most of this is covered in [the introduction][i] to virtualenv.  Let's say you have a project called `ponies` and that project lives in
`~/Projects/ponies` you can now create a `virtualenv` just for ponies:

    mkvirtualenv ponies -a ~/Projects/ponies

Now, whenever you need to work on ponies you can do the following:

    workon ponies

This will automatically use a special `ponies`-only version of `python`, any packages that you `pip` install will only be available to `ponies` and you won't need to use `sudo`.

Furthermore if things go south you can always do the following:

    deactivate  # This takes you out of the ponies virtualenv
    rmvirtualenv ponies
    mkvirtualenv ponies -a ~/Projects/ponies

Good as new.

## Final Thoughts.

This may seem like a lot of work at first.  After all you just want to write code.  That's fine, you can probably skip this.  As you work with more python code, and with multiple projects, you may then see the need for something like `virtualenv`.  You can more than likely retroactively `virtualenv`-ize your development environment.

This tutorial is something I recommend for all new python engineers as it generally will cause hardships at inconvenient times.  May as well take care of this stuff now.

The world is your oyster.



[b]: http://brew.sh/
[v]: http://www.virtualenv.org/en/latest/#installation
[vw]: http://virtualenvwrapper.readthedocs.org/en/latest/install.html#basic-installation
[i]: http://virtualenvwrapper.readthedocs.org/en/latest/#introduction
