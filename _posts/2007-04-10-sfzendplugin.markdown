---
wordpress_id: 90
layout: post
title: sfZendPlugin
wordpress_url: http://spindrop.us/2007/04/10/sfzendplugin/
site: spindrop
---
[tags]Zend, Zend Search Lucene, Search, Lucene, php, symfony, zsl, plugins[/tags]

[s1]: http://spindrop.us/2006/08/25/using-zend-search-lucene-in-a-symfony-app/
[p]: http://archivemati.ca/2007/03/08/zend-search-lucene-symfony-and-the-ica-atom-application/
[l]: http://lyro.com/
[zsl]: http://framework.zend.com/manual/en/zend.search.html
[symfony]: http://symfony-project.com/
[szp]: http://www.symfony-project.com/trac/browser/plugins/sfZendPlugin
[zf]: http://framework.zend.com/
[zfb]: http://www.symfony-project.com/book/trunk/17-Extending-Symfony#Bridges%20to%20Other%20Framework%20Components

I originally intended to rewrite [my Zend Search Lucene tutorial][s1], but [Peter Van Garderen][p] covered the bulk of what's changed and I was too busy developing search functionality for [lyro.com][l] (not to mention finding inconsistencies with the Zend Search Lucene port and Lucene) to finish the tutorial.  So I broke it up into smaller pieces.

I packaged [Zend Framework][zf] into a [symfony plugin][szp].  [symfony][] is easily extended using plugins.  

You can obtain this from subversion with the following command (from your `/plugins` directory):

    svn export http://svn.symfony-project.com/plugins/sfZendPlugin

[symfony][] has a [Zend Framework Bridge][zfb] which let's us autoload the framework by adding the following to `settings.yml`:

    .settings:
      zend_lib_dir:   %SF_ROOT_DIR%/plugins/sfZendPlugin/lib
      autoloading_functions:
        - [sfZendFrameworkBridge, autoload]

First we define `sf_zend_lib_dir` to be in our plugin's `lib` directory.  Then we autoload the bridge framework.

After setting this up, all the Zend classes will be available and auto-loaded from elsewhere in your code.
