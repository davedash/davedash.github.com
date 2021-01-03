---
layout: post
title: Database versus files for Images
redirect_to: https://blog.dadops.co/2009/02/18/database-versus-files-for-images/
tags: [database, django]
---
This is a dead topic for sure, but one of the bad web development habits I had picked up was that storing everything in a database made things easier.

I actually put some effort into thinking this through.  For me it was a case of management.  I didn't want to have to worry about two data stores for application-generated data.  In otherwords, the data in the database was all generated via my web application (either by myself or others who worked on the product, or by end users).  Having to also remember that there were select files as well seemed like a disaster.

Most frameworks, correctly assume you'll upload files to a filesystem.  I never fully understood this until I thought about how I'd speed things up when the time comes to speed things up.  Django forces you to think that way.

Almost from the start Django encourages you to:

1. Upload any binary content to the filesystem with pointers in a database
2. Have a separate server, or even machine serve static content.

Furthermore in a cached environment or even an environment that utilizes a CDN, putting static content in one spot, including user-generated content, was a big win.

I've been porting an app from symfony to django for some time, and I had been serving images via the database.  Immediately when I switched to the filesystem I saw a huge benefit.  Not just a drop in database connections, but overall "zippiness" in the site.

We'll see how well this performs in the real world, but I am quite sure that I learned my lesson.
