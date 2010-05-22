---
wordpress_id: 148
layout: post
title: Why Django Templating is awesome and why I get smarty again
wordpress_url: http://spindrop.us/2008/02/01/why-django-templating-is-awesome-and-why-i-get-smarty-again/
site: spindrop
tags: [spindrop, symfony, php, django, smarty]
---
I get Smarty thanks to django... yeah, it's weird.

Back to my [original comment about templating](http://spindrop.us/2008/01/28/templating/), smarty really is trying to limit the scope of PHP in a good way.  Too often I see a lot of heavy-lifting in the templates.  It's so bad it makes my MVC'd brain explode.

Django templates are very limited, based on a philosophy of keeping view logic and only view logic in the templates.

This is what smart tries to do and it's a reasonable solution to the fact that PHP is a templating language with a kitchen sink.  It's saying, okay... well let's treat PHP as a programming language, and keep Smarty as the template.

symfony of course says (well not really, or in any official capacity, but would you believe... frameworks talk to me), some PHP is view and some is model/controller.  We'll suggest which ones are which, but really we're not getting in the way of making your life a living hell by sticking complicated business logic inline.
