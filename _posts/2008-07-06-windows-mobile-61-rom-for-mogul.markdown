--- 
wordpress_id: 185
layout: post
title: Windows Mobile 6.1 ROM for Mogul
wordpress_url: http://spindrop.us/?p=185
---
[nextrom]: http://www.phonenews.com/phones/index.php/HTC_PPC-6800_/_XV6800_/_Mogul_/_P4000_/_Titan

A [leaked ROM for the Sprint Mogul][nextrom] featuring Windows Mobile 6.1 was circulating the internet and many of my issues with Windows Mobile were pushing me to upgrading.  For me it fixes a few things with the GPS and improves the usability of texting.

### GPS

The biggest issue I was having with the Sprint Mogul was the GPS would crash continuously... forcing me to restart my device.  Restarting any phone tends to take forever, so I was eager to have this problem minimized.  The issue was that if an app still had the GPS open, and the machine went to sleep, upon waking the GPS driver would crash.

Something similar still happens in 6.1, but its way more resilient.  Instead of restarting every day, I find myself restarting once or twice every several weeks - and that's after heavy GPS usage.

### SMS Notifications

The Mogul used to vibrate and alert that your SMS message has sent.  There was a registry hack to disable this for versions prior to 6.1, but that's no longer necessary.

The downside to the hack was you wouldn't have any sort of feedback that a message was sent.  However, Pocket Outlook has adopted a chat style interface for displaying text messages.  So now texts look like conversations - which make it very easy to have tiny conversations with people.

### Do it...

Flashing the ROM is easy since Sprint (apparently) gives you a Rom Update Utility (Windows executable unfortunately) that does all the dirty work.  I backed up my data using Missing Sync and then started the update process in a virtual machine.

Restoring my default settings and apps was a bit of a pain, but overall it's a decent upgrade and fixes my biggest gripes.
