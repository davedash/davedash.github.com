--- 
wordpress_id: 21
layout: post
title: Internet Explorer bug fixes
excerpt: |
  [katie]: http://katiebonn.com/
  [ubuntu]: http://ubuntu.com/
  [wine]: http://winehq.com/
  [rbu]: http://reviewsby.us/
  <div class="photo" style="float: right">
  <a href="http://www.flickr.com/photos/davedash/146603141/" title="Photo Sharing"><img src="http://static.flickr.com/56/146603141_fe6dcb20b4_m.jpg" width="240" height="164" alt="IE Fix" /></a>
  </div>
  
  My web development shortcomings for my personal sites, including [reviewsby.us][rbu] (one-man army, no QA testers) is being blind to <acronym title="Internet Explorer">IE</acronym>.  [Katie] and I both work using Powerbooks and our backup computer is a [Ubuntu] desktop.  At work [Katie] uses <acronym title="Internet Explorer">IE</acronym> and noticed an error with how I display menu items.  Friday I took that [Ubuntu] machine and installed Internet Explorer via [Wine][] (details to follow).

---
[katie]: http://katiebonn.com/
[ubuntu]: http://ubuntu.com/
[wine]: http://winehq.com/
[rbu]: http://reviewsby.us/
<div class="photo" style="float: right">
<a href="http://www.flickr.com/photos/davedash/146603141/" title="Photo Sharing"><img src="http://static.flickr.com/56/146603141_fe6dcb20b4_m.jpg" width="240" height="164" alt="IE Fix" /></a>
</div>

My web development shortcomings for my personal sites, including [reviewsby.us][rbu] (one-man army, no QA testers) is being blind to <acronym title="Internet Explorer">IE</acronym>.  [Katie] and I both work using Powerbooks and our backup computer is a [Ubuntu] desktop.  At work [Katie] uses <acronym title="Internet Explorer">IE</acronym> and noticed an error with how I display menu items.  Friday I took that [Ubuntu] machine and installed Internet Explorer via [Wine][] (details to follow).

I didn't delve into this as much as I should have, as I really wanted it to just work in <acronym title="Internet Explorer">IE</acronym>.  The menu items are list items (`li`) that float left.  In the container (a `ul`) is set with `overflow: auto` which is supposed to give enough overflow to show the entire containing element including all floats.  For some reason it didn't work for <acronym title="Internet Explorer">IE</acronym> so as a quick fix I added a few clearing `<br/>`s.

[Enjoy the site][rbu].
