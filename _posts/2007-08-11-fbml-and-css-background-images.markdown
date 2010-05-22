---
wordpress_id: 114
layout: post
title: FBML and CSS background images
wordpress_url: http://spindrop.us/2007/08/11/fbml-and-css-background-images/
site: spindrop
tags: [spindrop, css, openid, symfony, reviewsby.us, sfFacebookPlatformPlugin, fbml, partials, background, hacks]
---

[fbdev]: http://www.facebook.com/topic.php?uid=2205007948&topic=5140&post=50818&pwstdfy=0434dec4ce75745f05b7396611234b7c#post50818
[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/

I've been tediously building out the new [reviewsby.us][rbu] app for Facebook and I ran into some problem when I tried to embed this CSS:

<div><textarea name="code" class="css">
input.openid_login {
            background: url("http://openid.net/login-bg.gif") no-repeat #fff;
   background-position: 0 50%;
          padding-left: 18px;
}
</textarea></div>

The CSS worked fine, just now background image.  The fix is mentioned in [this post][fbdev] which is to repeat the `background` statement:


<div><textarea name="code" class="css">
input.openid_login {
            background: url("http://openid.net/login-bg.gif") no-repeat #fff;
            background: url("http://openid.net/login-bg.gif") no-repeat #fff;
   background-position: 0 50%;
          padding-left: 18px;
}
</textarea></div>

Voila, it works.  Hopefully this hack won't be necessary in later versions of the Platform.
