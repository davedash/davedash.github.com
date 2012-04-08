---
layout: post
title: "Plus Addressing"
tags: [django, webdev, pinterest, email]
published: true
time: 10:36PM
---

One of my biggest pet peeves is registration forms that don't accept "plus"
addresses, e.g. `myname+whatever@mysite.com`.

I've been using plus addressing for years, and before that,
["minus" addressing][1].  Since GMail handles my `@davedash.com` email
addresses I am forced to use the "plus" style if I want to easily create
multiple addresses on a whim.

I use this style of addressing to keep track of who might be spamming me
(JC Penny for example).  I might sign up with `myname+facebook@mysite.com` for
Facebook, `myname+pinterest@mysite.com` for Pinterest, etc.  Unfortunately this
wasn't working when I signed up for Pinterest.  My wife and a few of my friends
were quick to tell me about this:

![pinterest registration screenshot][2]

So when I joined Pinterest, I immediately filed a bug, and then after talking
to a few people, decided to fix it.  The fix was remarkably simple.

There's usually two causes for this problem.  1. People use the wrong
validation for their emails.  Namely one that says `+` is bad.  Luckily most
web frameworks, like Django, get this right.  2. They use the email address as
some sort of parameter in a URL.  For example:
`http://mysite.com/newsletter/unsubscribe?email=myname+whatever@mysite.com`.

## The wrong validation

If you're using the wrong validation, fix it.  There's no excuse for anybody
seeing "sorry please use a valid" email address when their email is perfectly
valid.  Django has a [regular expression which you can use][3].

## The URL issue

The URL issue is an issue of URL encoding.  In our example
(`http://mysite.com/newsletter/unsubscribe?email=myname+whatever@mysite.com`):

The email variable gets decoded as:

    myname whatever@mysite.com

Clearly that *is* invalid.  On a URL bar, the `+` is interpreted as a space.
The solution is to encode your email address.  For Pinterest, this is all we
needed to do.  JavaScript has a handy `encodeURIComponent` to change this.  If
you are using an `ajax` call from jQuery, you can simply pass the data an
object:

    {'email': 'myname whatever@mysite.com'}

This will get encoded properly.

## Call to Action

Plus addressing a minimal use case, but please... make sure that people aren't
hitting validation errors in your registration.  Each input on a registration
form is a reason to not register.  Each validation error, is a reason to give
up prematurely.  Do your users and your product a favor and don't invalidate
them unnecessarily.

![pinterest registration screenshot post-fix][4]


[1]: /2008/10/12/google-apps-in-search-of-a-worthy-email-system/
[2]: /static/images/2012/04/07/pin-screenshot.jpg
[3]: https://github.com/django/django/blob/master/django/core/validators.py#L88
[4]: /static/images/2012/04/07/pin-screenshot-fix.jpg
