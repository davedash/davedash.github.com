--- 
wordpress_id: 20
layout: post
title: reviewsby.us + Google Coop, ratings, updates
excerpt: |
  [Google]: http://google.com/
  [b]: http://googleblog.blogspot.com/2006/05/yes-we-are-still-all-about-search.html
  [c]: http://www.google.com/coop/
  [q1]: http://www.google.com/search?hl=en&lr=&q=cheesecake
  [s]: http://www.google.com/coop/profile?user=015173080624703800226
  [tcf]: http://reviewsby.us/restaurant/cheesecake-factory
  
  [Google][] [announced yesterday][b] [Google Coop][c], a way to subscribe to links from other sites.  So let's say you type in a word like ["cheesecake" into Google][q1].  If you are [subscribed][s] to results from [reviewsby.us][r] you will get a result for [The Cheesecake Factory][tcf].  Go ahead and [give it a try][s] (you must be logged in to your Google Account to subscribe).

---
[Google]: http://google.com/
[b]: http://googleblog.blogspot.com/2006/05/yes-we-are-still-all-about-search.html
[c]: http://www.google.com/coop/
[q1]: http://www.google.com/search?hl=en&lr=&q=cheesecake
[s]: http://www.google.com/coop/profile?user=015173080624703800226
[tcf]: http://reviewsby.us/restaurant/cheesecake-factory

[Google][] [announced yesterday][b] [Google Coop][c], a way to subscribe to links from other sites.  So let's say you type in a word like ["cheesecake" into Google][q1].  If you are [subscribed][s] to results from [reviewsby.us][r] you will get a result for [The Cheesecake Factory][tcf].  Go ahead and [give it a try][s] (you must be logged in to your Google Account to subscribe).

It took about an hour to push some changes live and get that search going.  Unfortunately there's more work to be done (it's rather hard to validate these feeds).  I intend to add descriptions, ratings, number of menu items, etc to the results.  

[ratings]: http://reviewsby.us/restaurant/pizza-nea
I also added [ratings] to the web site.  Anybody can let us (quickly) know what they think of any restaurant without taking the effort of writing a review.  

Logins should work slightly better.  I rewrote the code that redirects you after logging in so it takes you to where you were or where you were going.  I also fixed a bug with removing tags.
