---
wordpress_id: 313
layout: post
title: Getting started with pipe viewer
wordpress_url: http://spindrop.us/?p=313
site: spindrop
tags: [spindrop, mozilla, pv]
---
Despite working on slimming the `addons.mozilla.org` database through dieting and exercise - I still have to occasionally do long running database tasks.  So I finally tried out [pipe viewer](http://www.ivarch.com/programs/pv.shtml).  As someone who's impatient this has been awesome.  Here's some quick examples:

	[root@ml-db10 sun]# pv -cN source < addons_remora.2009.09.15.sql.gz | gunzip|pv -cN gunzip > addons_remora.2009.09.15.sql
	   gunzip: 10.1GB 0:06:48 [25.5MB/s] [   <=>                                  ]
	   source: 3.47GB 0:06:48 [8.72MB/s] [======================>] 100%

Here we are calling pipe viewer with an argument that says to title this progress meter as `source`, and feeding it the gzip'd file.  Pipe viewer will output two things the progress, and the actual file.  We pipe that file into `gunzip` to unzip it, and back into another instance of pipe viewer (again with a title, of `gunzip`) and the standard output gets redirected to our destination file.

Now a simpler example is checking the progress of loading a large sql file into mysql:

	[root@ml-db10 sun]# pv -cN sql < addons_remora.2009.09.15.sql | mysql -uroot addons_remora -p$PWD
	      sql: 2.55GB 0:18:19 [5.68MB/s] [=====>                  ] 25% ETA 0:54:30

We could have probably combined all this, however:

	[root@ml-db10 sun]# pv -cN source < addons_remora.2009.09.15.sql.gz | gunzip|pv -cN gunzip | mysql -u root addons_remora -p$PWD

Armed with this knowledge you can determine whether to grab a soda, a sandwich or a 2-hour lunch.
