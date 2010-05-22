---
wordpress_id: 92
layout: post
title: Tips for symfony and Subversion
wordpress_url: http://spindrop.us/2007/04/17/tips-for-symfony-and-subversion/
site: spindrop
tags: [programming, symfony, symfony, subversion]
---
[tags]symfony, subversion[/tags]

[a1]: http://www.symfony-project.com/askeet/1
[erepo]: http://www.ericsink.com/scm/scm_repositories.html
[esc]: http://www.ericsink.com/scm/source_control.html
[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/


There's some tricks you can do to running a symfony project with subversion:

### Ignoring files in `cache/` and `log/`

The first thing you can do (and this is well documented in the [askeet tutorial][a1]) is ignore files in `cache/` and `log/`.  These files are specific to each instance of your app and don't contain anything that needs to be in version control.  

Run the following:

	cd $SF_ROOT
	rm -rf log/* cache/*
    svn propedit svn:ignore log
    svn propedit svn:ignore cache

`svn propedit` will bring up a text editor, in both instances you want to save the following:

	*

### Ignore other auto-generated files

Eric Sink wrote an excellent [tutorial on source control][esc].  In his chapter on [repositories][erepo] he recommends checking in *only* hand edited source code.  If a property file generates another file, check in the property file, not the auto-generated result.  This not only keeps your repository clean, it prevents a lot of unnecessary check-ins. 

If you use propel for your <acronym title="Object Relational Mapping">ORM</acronym> layer there are a few files you can ignore using `svn propedit svn:ignore {dirname}`.

In `$SF_ROOT/config` we can ignore:

	*schema-transformed.xml

These are `xml` files that propel generates from `schema.xml` (or `schema.yml`).

In `$SF_ROOT/data/sql` we can ignore:

	lib.model.schema.sql
	plugins.*.sql
	sqldb.map

These are created from `schema.xml` (or `schema.yml`) as well.

The real savings will come with your model.  The propel model creates customizable php classes in `lib/model` which inherit from auto-generated files in `lib/om` there are also auto-generated map files in `lib/map'

We can run from `$SF_ROOT`:

	svn propedit svn:ignore lib/model/om
	svn propedit svn:ignore lib/model/map

and enter

	*

for both properties.

If you've mistakenly checked in some of these files you will need to remove them from your repository via `svn delete`.

### Linking the symfony Library

I prefer to embed the symfony library into each of my symfony apps rather than relying on a shared PEAR library.  This lets me run multiple versions of symfony without much fuss.  With subversion we can use the `svn:externals` property to directly link our app with the symfony subversion repository.

At first this sounds like danger, but externals can be linked to specific revisions.  However, the [symfony][] team tags their repository with version numbers.  To get this to work we need to do 3 things.  (**UPDATE:** See Fabien's comment about using the lib/vendor directory)

1. Modify `config/config.php` to look for symfony internally.  Just open it up and change it so it says this:
	<div><textarea name="code" class="php">
	<?php
	$sf_symfony_lib_dir  = dirname(__FILE__).'/../lib/symfony';
	$sf_symfony_data_dir = dirname(__FILE__).'/../data/symfony';
	</textarea></div>

2. Run `svn propedit svn:externals lib` from `$SF_ROOT` and enter:

		symfony http://svn.symfony-project.com/tags/RELEASE_1_0_2/lib/
or whatever version of symfony you want to link to, at the time of this post, `RELEASE_1_0_2` is fairly fresh.

3. Run `svn propedit svn:externals data` from `$SF_ROOT` and enter:

		symfony http://svn.symfony-project.com/tags/RELEASE_1_0_2/data/
or whatever version of symfony you want to link to, at the time of this post.

Now when you do `svn update` you'll have the [symfony][] library all linked up.  Furthermore this keeps all the developers on the same version of `symfony`.

Also you may want to start running symfony using `./symfony` versus `symfony`.  The former looks at your configuration settings to determine which `symfony` command to use, the latter is generally linked to your system wide command (which is generally the PEAR installed command).

### Linking to symfony Plugins

I have my hands in a number of symfony plugins because I work on a lot of projects which tend to share a lot of similar functionality.  Many of the plugins are in early stages of development, so I find it helpful to have them linked from svn as well.  This way I can get the benefits of any new functionality and if the occasion should arise, I can contribute any useful changes I make.

To link to the plugins you run `svn propedit svn:externals plugins` and enter one plugin per line in the following format:

	{plugin_name} -r{REVISION} {URL}

For one of my projects I use:

	sfPrototypeTooltipPlugin http://svn.symfony-project.com/plugins/sfPrototypeTooltipPlugin
	sfGuardPlugin http://svn.symfony-project.com/plugins/sfGuardPlugin
	sfZendPlugin http://svn.symfony-project.com/plugins/sfZendPlugin

I've omitted the revision, because I live dangerously and want to use the latest `$HEAD`.
