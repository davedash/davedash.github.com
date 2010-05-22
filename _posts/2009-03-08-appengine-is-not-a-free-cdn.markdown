---
wordpress_id: 244
layout: post
title: AppEngine is not a free CDN
wordpress_url: http://spindrop.us/?p=244
site: spindrop
tags: [spindrop, cdn, misconceptions]
---
[c]: http://24ways.org/2008/using-google-app-engine-as-your-own-cdn

I've been doing some personal research with YSlow and looking into CDNs and reading comments on various blogs about CDN solutions.

I think people make a lot of assumptions as to what is a CDN.  Even people who correctly [define what a CDN is][c], will later make this mistake.

To quickly summarize in layman's terms:  A CDN is a system which sends data to a user using nearby servers, rather than a central server.  So your web site might have dynamic content hosted in one location, but a user requesting static assets (images, stylesheets, videos, etc) will have it served from a server that is physically close to them.  So I might have my logo ultimately served from San Jose, whereas someone in New Jersey might have it served from a server in New York.

This is not the service that Google is offering with AppEngine.  It is not the service you get for hosting with Yahoo's unlimited small business hosting, and it's not even the service you get with Amazon's S3.

These are all very specific services that don't have any guarantee that the data will be served from a location that is close to the end user.  It's just specialized hosting.

With that said, all these services are worthwhile if you want to stop serving static content and rely on someone else to do it.  Chances are they can do a better job than you at hosting these static assets, and allow you to focus on serving dynamic content.  The one thing to remember is be sure you are using the right tool for the right job.  AppEngine is great for writing apps on the Google Infrastructure, but it doesn't necessarily offer the same SLA for serving content as S3, or Yahoo! Small Business might.

Also note, that if you are using S3, and really need a CDN, Amazon offers [CloudFront](http://aws.amazon.com/cloudfront/).
