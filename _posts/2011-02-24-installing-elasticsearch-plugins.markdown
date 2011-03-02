---
layout: post
title: "Installing ElasticSearch plugins"
tags: [seo, search, elasticsearch, mozilla, python, pyes]
published: true
time: 1:36PM
---
[p]: http://elasticsearch.googlecode.com/svn/plugins/
I'm slowly trying to familiarize myself with ElasticSearch and the `pyes`
python interface.  ElasticSearch uses a lot of plugins, and while the plugin
system is easy to use, it's not obvious where to find the plugins.

They are [here][p].

If you want to install the attachments plugin, you can do:

    bin/plugin install mapper-attachments

And voilà it's installed.
