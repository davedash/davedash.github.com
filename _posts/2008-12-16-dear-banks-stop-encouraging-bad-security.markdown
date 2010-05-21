--- 
wordpress_id: 212
layout: post
title: Dear Banks, Stop Encouraging Bad Security
wordpress_url: http://spindrop.us/?p=212
---
[m]: http://mint.com/
[g]: http://geezeo.com/

I use an online personal finance site that connects to all my financial accounts and aggregates my transaction history.  I love it, it's very useful, and it keeps me financially organized.

The part that annoys me is that most of these personal finance sites require you to supply your username and password for all your bank accounts.  For some banks it also requires your social security number, the last five people you've slept with, your home town, your favorite color, etc, etc.  Basically all the pesky sign in questions your bank might ask you when you log in.

This is a cruel necessity for companies like [Geezeo][g], [Mint][m], Ameriprise and Quicken Online in order to provide this aggregation service and a scary proposition for people like us who use these services.  You're giving full unfettered access to companies you may not have ever heard of to all your finances.

**Security questions, and personalized security questions are the wrong way to fix bank security.**

<!--more-->
People want online personal finance sites.  They want all their data in a single place without having to jump through a bazillion hoops for each and every 401K, savings account, checking account, online stock trading system and mortgage account.  They will gladly sacrifice security for a chance to better their financial management capabilities.

Banks need to create APIs so third-party software can access transaction data.  The authentication for this should be secure, limited and revokable.  Meaning, I may authorize [Mint][m] to see my Bank of America account, but at any time I can log on to BoA and deny Mint's ability to see my transaction data.  OAuth may be one mechanism to achieve this.

This will achieve a few things:
* People won't give out their passwords online to anybody but their bank.
* Getting data into these aggregating sites will be reliable and secure.
* At any time you can see who has access to your transaction data and revoke it.

Please banks, do your part to keep the internet secure.  [Mint][m], [Geezeo][g] and anybody else, please do your part of turning up the pressure on financial institutions and when the time comes... please start using these APIs.
