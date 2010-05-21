--- 
wordpress_id: 233
layout: post
title: A stitch in Fabric saves time
wordpress_url: http://spindrop.us/?p=233
---
[f]: http://www.nongnu.org/fab/

Each day as I grow as a developer I pick up better habits.  One is automating anything that I'll have to do more than once.

Therefore, deploying important projects has evolved:

1. Edit files live on the site.
2. FTP files from my local machine onto the live site and do tweaking as needed.
3. Develop using a cross-platform capable framework and deploy live via rsync.
4. One step deployment.

I looked at a few methods for performing one-step deployment.  Shell scripts seemed to basic, and things like Puppet seemed to large a scale.  So I looked into Capistrano and [Fabric][f], and settled on [Fabric][f], because it was barebones and python.

I'm at a stage with my project where I need to test it on an external server, so rather than uploading it and winging it I actually thought about a few things.

<!--more-->

### The task

I was thinking the ideal situation is a single command line that I can type that will upload my files to the server.  Furthermore it should upload first to a new directory and then symlink and restart the server to do the cutover.  I can easily write another script to rollback.

The way I setup my Nginx and Apache servers was they would look for the symlinks: staging, test, production to serve up the respective environments (I'm using a single host for this example).


### Directory Structure

I use a very particular directory structure:

* `$WWW_APPS/mysite.com/` - is my root app deployment directory.
	* `releases/` - each code push is stored in a unique directory
		* `1/`
		* `2/`
		* ...
		* `100/` - the directory name is the `svn` revision, but is a series of precise `svn` exports, not a checkout.
	* `staging` - this symbolic link links to a specific revision directory that has been designated for staging purposes.  This might be the last directory in `releases/`, e.g. `$WWW_APPS/mysite.com/releases/100/`
		* `config/` - any config files go here (e.g. nginx or apache)
		* `mysite.com/` - the actual Django project
		* `scripts/` - any utility scripts, mostly database model changes
		* `site-packages/` - any related libraries that I need, this isn't the best approach I need to investigate `virtualenv`
		* `static/` - all my static assets go here
	* `staging.rollback` - the former `staging` symlink is demoted to `staging.rollback`
* `$WWW/mysite.com/`  
	* `staging` - This is where the static assets get served from according to nginx.  It's a symbolic link to `$WWW_APPS/staging/static`.  This link does not change during deployment.
	* `uploads_staging/` - This directory contains uploads (user data).  It requires manual adjustment when there are data changes (deletes, adds, updates).  For the most part it can stay unchanged from one deployment to the next.


### Subversion

I'm currently using subversion to maintain my code.  If you are starting a project anew, I suggest using `git` as it is designed with branching in mind.  The script below should be adaptable for `git` instead of `svn`.

That being said, when I deploy code, I use the revision number as the directory name for that deployment (e.g. `$WWW_APPS/mysite.com/releases/100/` for `r100`) .  

This forces me to commit my changes and not deploy code that is not checked in.

Other viable alternatives would be time-stamped directories.  Anything that is unique between deployments will be sufficient.

### The `fabfile.py`

Here's the `fabfile.py` I constructed.  It's by no means final


<div><textarea name="code" class="python">
def staging():
    "Pushes current code to staging, hups Apache"
    # get the build number    
    local('svn up mysite.com')
    
    config.svn_version   = svn_get_version()
    
    if not config.svn_version:
        abort()
    
    config.static_path   = '/var/www/static.mysite.com'
    config.svn_path      = 'http://svn.mysite.com/trunk'
    config.svn_export    = 'svn export -q -r %(svn_version)s'
    
    run('mkdir %(path)s', fail='abort')
    
    # svn export mysite.com to path 
    run('%(svn_export)s %(svn_path)s/mysite.com %(path)s/mysite.com', fail='abort')
    
    # svn export site-packages to site-packages
    run('%(svn_export)s %(svn_path)s/site-packages %(path)s/site-packages', fail='abort')
    
    # svn export mysite.com to path 
    run('%(svn_export)s %(svn_path)s/scripts %(path)s/scripts', fail='warn')
    
    # svn export configs
    run('%(svn_export)s %(svn_path)s/config %(path)s/config', fail='abort')
    
    # export /var/www/static.mysite.com/releases/%(svn_version) 
    run('%(svn_export)s %(svn_path)s/static %(path)s/static', fail='abort')
    
    # symlink to images from /var/www/static.mysite.com/staging/images/menuitems/* new release dir
    run("rm -r %(path)s/static/images/menuitems", fail=abort)
    run("ln -s %(static_path)s/menuitems_staging %(path)s/static/images/menuitems", fail=abort)

    # rotate "staging" symlinks
    run('rm %(releases_path)s/staging.rollback', fail='warn')
    run('mv %(releases_path)s/staging  %(releases_path)s/staging.rollback', fail='warn')

    # staging sym to new destination
    run('ln -s %(path)s %(releases_path)s/staging', fail='abort')
    
    # server is hup'd
    invoke(hup)

def rm_cur_rev():
    config.svn_version   = svn_get_version()
    run('rm -rf %(path)s', fail='abort')

def hup():
    sudo('/etc/init.d/apache2 restart')
    sudo('/etc/init.d/nginx restart')
    
    
def svn_get_version():
    from subprocess import Popen, PIPE
    output = Popen(["svn", "info", "mysite.com"], stdout=PIPE).communicate()[0]
    return output.partition('Revision: ')[2].partition('\n')[0]



config.fab_hosts = ['mysite.com']
config.fab_user = 'builder'
config.releases_path = '/var/www_apps/mysite.com'
config.path          = '%(releases_path)s/releases/$(svn_version)'


</textarea></div>

### Final Thoughts

There's room for improvement, but this is a start.  `virtualenv` looks like another avenue I might want to explore (especially when it comes time to upgrade Django, python, MysqlDB or PIL).  This also doesn't take care of priming the server with necessary packages - again, something `virtualenv` could make easier for me.

However, this file was not too difficult to create.  I sat down, thought about the ideal solution, implemented the steps and iterated on that until the script worked.  I have pushed 19 revisions of code so far, mostly to test this process, but also to make necessary adjustments.  I've probably saved countless hours of logging in and doing things manually.

How do you deploy your apps?
