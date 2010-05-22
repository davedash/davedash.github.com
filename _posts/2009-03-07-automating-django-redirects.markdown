---
wordpress_id: 242
layout: post
title: Automating Django Redirects
wordpress_url: http://spindrop.us/?p=242
site: spindrop
tags: [spindrop, django, redirects, slugs]
---
[r]: http://docs.djangoproject.com/en/dev/ref/contrib/redirects/

Django has a very [simple redirects system][r].  Simple as in it's easy to understand.  If someone encounters a 404, Django Redirects catches this and does a final lookup to see if there's an entry to a new URL in the redirects table.

The real win, is when your `slug` fields change (and thus the `get_absolute_url()` of your objects), you can simply automate the creation of a redirect:

<div><textarea name="code" class="python">
        if self.pk:
            old_version = MyObjectClass.objects.get(pk=self.pk)
            if old_version.stripped_title != self.stripped_title:
                Redirect(site_id=1, old_path=old_version.get_absolute_url(), new_path=self.get_absolute_url()).save()


</textarea></div>

Note you must have enabled the [redirects app][r] before trying this.  You also need a `get_absolute_url()` function defined for  your `MyObjectClass`.  This is the true value of Django Middleware.  Let those truly repetitive site-wide tasks get done in one spot.
