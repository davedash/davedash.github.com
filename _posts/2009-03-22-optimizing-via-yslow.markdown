---
wordpress_id: 252
layout: post
title: Optimizing via YSlow
wordpress_url: http://spindrop.us/?p=252
site: spindrop
---
[yslow]: http://developer.yahoo.com/yslow/
[ydn]: http://developer.yahoo.com/
[fake]: http://spindrop.us/2009/03/08/appengine-is-not-a-free-cdn/

I'm not a performance person per se.  I am a heuristics type of guy.  Meaning you tell me a bunch of things to look out for, I get an understanding for those things, and if I agree, I'll fix them.  I work off lists :)

[YSlow][] is therefore a boon to me.  If you aren't familiar with it, it is a plugin for Firefox (with a dependency on Firebug) that will grade the performance of a given site based on a set of rules determined by [YDN][].  This is my list, and YDN went into great detail to explain each of these items is important.

The following is my journey through optimization.  I went from a D- to a C in a single day.  While that might not seem like much, I could have nabbed an A if I used a CDN, like [CloudFront](http://aws.amazon.com/cloudfront/), or even a [fake CDN][fake] and dropped Google AdSense and Analytics.  Those tools are helpful for me, and worth keeping around, so I opted to take the grade penalty.

<!--more-->
[yui]: http://developer.yahoo.com/yui/

### Begin: D - 61

I began with a D.  It's actually not that bad.  In most dimensions I was getting an A.  Namely because I use a web framework (Django) that is optimized for being cached and served well. 

### YUI Combo-loading: Sneaking up to D - 62

My first goal was to reduce the HTTP requests.

I use the [YUI][] CSS and javascript framework as the foundation for my CSS and javascript.  One major benefit is that they offer to host this for you on a true <acronym title="Content Delivery Network">CDN</acronym>.  The javascript framework is very thorough and can do quite a lot.  Because it's so robust, it is split into several files.  Originally I had been doing this:

<div><textarea name="code" class="html">

<script type="text/javascript" src="http://yui.yahooapis.com/2.6.0/build/yahoo-dom-event/yahoo-dom-event.js"></script>
<script type="text/javascript" src="http://yui.yahooapis.com/2.6.0/build/connection/connection-min.js"></script>
<script type="text/javascript" src="http://yui.yahooapis.com/2.6.0/build/datasource/datasource-min.js"></script>
<script type="text/javascript" src="http://yui.yahooapis.com/2.6.0/build/autocomplete/autocomplete-min.js"></script>

</textarea></div>

That was 4 separate calls from the web browser to this server.  While they are all fast requests, it'd be better to make a single request that catches all of this.

Luckily, YUI has "combo-handling".  I was able to turn those four requests into the following:

<div><textarea name="code" class="html">
<script type="text/javascript" src="http://yui.yahooapis.com/combo?2.7.0/build/yahoo-dom-event/yahoo-dom-event.js&2.7.0/build/connection/connection-min.js&2.7.0/build/datasource/datasource-min.js&2.7.0/build/autocomplete/autocomplete-min.js"></script>
</textarea></div>

A very quick fix, that brought my overall grade up by a single point.

### Concatenation and Minification: Instant C- - 72

I still had a large number of HTTP requests.  Luckily [YUI][] has the [YUI Compressor](http://developer.yahoo.com/yui/compressor/).  It compresses javascript and CSS and even gives you tips on writing better code (or more compressible code).

This used to be scary and not something I'd want to deal with, but if I can run it from the commandline, then I can add it to [my deployment script](http://spindrop.us/2009/03/02/a-stitch-in-fabric-saves-time/).  Now on each deployment my CSS and javascript are concatenated and compressed and uploaded to my server.  When my app is in production mode, it seeks out minified code, versus more verbose human-readable code.

The javascript compression was great.  The output was at least compressed in half.  This skyrocketed the score to 72.  Less HTTP requests and Javascript minification were the individual rules in YSlow that were boosted.

### Google: They want you to fail

This is of course tongue-in-cheek.  Google has some wonderful tools like AdSense and Analytics that do hinder the score and ever so slightly the speed of your site.

As far as javascript is concerned, I am linking to:
* YUI
* My own JS 
* Google Analytics
* Google Adsense

Google Adsense is by far the worst offender.  You think you're calling just one solitary call to Google to fetch an ad, but it's actually 4 calls.  I'm sure this could be engineered better.  The good news is it's usually not too slow.

There's an option to self-serve `ga.js` the Analytics code.  While this might result in a higher score, there are a few issues.

* The process is more error prone, there's a chance that the file you download from Google might get corrupted and your unit tests might miss it.
* You are serving from your own servers - which could either be expensive or slower.
* Many sites include a call for `ga.js` and therefore there's a high likelihood that it's already browser-cached.
* The code could get out of date.

For this reason, it's better to lose about 5 points for not serving it.  This score is large because it effects a lot of YSlow's rulesets.  If you'd still like to self-serve here's [some discussion on that](http://www.askapache.com/javascript/google-analytics-speed-tips.html).

This will likely give you an "F" on the Expires Header ruleset as well.

### Content Delivery Network (CDN)

A lot of people freak that CDN is on YSlow and feel like not all sites need/require a CDN.  They are right that the don't need a CDN, but in my opinion they don't necessarily need to get an "A" either.  All this is an approximation of doing the best you can do to make your frontend code as fast and efficient as possible.

With that said, CDN's are becoming more and more in reach.  Amazon Cloud Files which [I mentioned][fake] is a pay as you go system, which is quite affordable (I estimated < $1/month for my needs).

I configured YSlow to list some of the standard Google and Yahoo API hosts as CDNs.  This didn't affect my score, and I didn't want to integrate S3/Cloudfiles at this stage, so I took the "F".  

### Gzip files (still at 72)

Adding Gzip to the Nginx configuration was easy, however my grade still stayed at 72, but it did up my score for that specific rule.  Gzip compression is supported in most modern browsers and is usually a config change away.

Again, note that `ga.js` is not served compressed.  

### Upgrading from `urchin.js` (up to 73)

In the process of tweaking my Gzip configuration, I noticed that I was still using the legacy `urchin.js` instead of the more modern `ga.js`.  Simply changing this boosted me to 73.

### Move Javascript to the bottom (still at 73)

Moving the javascript to the bottom is another trick.  This at least loads most of the HTML before the Javascript loads (and in many cases, waits).

Some refactoring of Django templates makes this a breeze.

### Conclusions

I was able to raise the score from a low D to a mid C, at some point I could make the score a high C, but it was inevitably not worth it.

From my perspective, Google could do a few things to help webmasters who use their widgets:

* Add a decent expires header to `ga.js` - this file is safe to cache for some degree of time.  Being at the latest and greatest `ga.js` is nice, but not necessary.
* Serve files Gzipped
* Use a single host for serving public APIs.  Yahoo can improve on this as well.  They can potentially do combo-hosting a la Yahoo Developer Network

Ultimately YSlow is a good guideline for speeding up your page render times.  It's not perfect, nor exact.  There's no realistic way to determine a users experience with page load times.  Slow network connectivity and bad browsers can make all your attempts in vain.  However, YSlow is an easy to follow set of heuristics which every site owner should attempt to implement as well as possible.

YSlow's [future incarnations][p] will yield some more flexibility.  Even in its default state it should yield better scores for people who are doing the right thing.

[p]: http://www.slideshare.net/stoyan/yslow-20-presentation
