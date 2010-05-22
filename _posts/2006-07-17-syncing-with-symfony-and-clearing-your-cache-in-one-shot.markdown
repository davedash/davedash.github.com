---
wordpress_id: 51
layout: post
title: Syncing with symfony and clearing your cache in one shot
wordpress_url: http://spindrop.us/2006/07/17/syncing-with-symfony-and-clearing-your-cache-in-one-shot/
site: spindrop
---
If you're using `symfony`'s `sync` command to synchronize files across environments (e.g. moving your development files to a staging server), it helps usually to clear the cache of the receiving server.

The following line will help:

	symfony sync production go ; ssh user@production "cd /var/www; symfony cc"   

Assuming you have <acronym title="Secure SHell">SSH</acronym> keys defined and that you change `user@production` to your username and server host as well as `/var/www` switched to your website path.  Also the `symfony` command needs to work on your "production" server (or whatever environment).

There may be a cleaner way to take care of this by changing the `symfony` command, but this works sufficiently well.
<!--next page-->
One of the more frustrating elements of web development is synchronizing multiple sites: usually a development site, a staging site and a production site.  <acronym title="SubVersioN">SVN</acronym> helps with keeping your code versioned, but usually you don't want to check out a copy of your web site onto your live server.

Usually we use <acronym title="Secure File Transfer Protocol">SFTP</acronym> or `rsync`.  The former has lots of problems, because a lot of manual work is usually involved to make sure you don't over-write important files.

`rsync`, however, is a champ and [symfony] takes advantage of this.  The key files you'll have to deal with are `$PROJECT_HOME/config/properties.ini` and `$PROJECT_HOME/config/rsync_exclude.txt`.

Your `properties.ini` should look roughly like:

	[symfony]
	  name=reviewsby.us
	[staging]
	  host=staging.reviewsby.us
	  port=22
	  user=root
	  dir=/var/www/staging/
	[staging2]
	  host=staging2.reviewsby.us
	  port=22
	  user=root
	  dir=/var/www/staging

Each heading other than "`[symfony]`" is a different environment.  In our example, we have two staging environments.  The values under each heading should be self-explanatory.  We can now run the following commands:

	symfony sync staging
	symfony sync staging go
	symfony sync staging2
	symfony sync staging2 go

The commands that lack `go` are "dry-runs" which just show you what files will be transfered.  The other commands will run `rsync` and transfer all the files not specified in the exclude file, `rsync_exclude.txt`.

See [askeet] or the [symfony documentation][s2] for more details.

[symfony]: http://symfony-project.com/ "The symfony Project"
[askeet]: http://www.symfony-project.com/askeet/22
[s2]: http://www.symfony-project.com/content/book/page/deployment.html
