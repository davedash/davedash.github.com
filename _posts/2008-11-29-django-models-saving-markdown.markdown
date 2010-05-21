--- 
wordpress_id: 202
layout: post
title: "Django models: saving markdown"
wordpress_url: http://spindrop.us/?p=202
---
I love markdown.  I write my blogs in markdown.  For most user text areas in my web apps I support markdown and save both the markdown and the formatted text into my data store.

To do this I had to install [markdown for python](http://www.freewisdom.org/projects/python-markdown/Installation).  For my Django projects I prefer downloading (or externally linking) to source code versus `easy_install`.

Then you override your save model like so:

	from markdown import markdown

	class MyNote(models.Model):
		def save(self, force_insert=False, force_update=False):
	     	self.html_note = markdown(self.note)
     		super(MyNote, self).save(force_insert, force_update)

Easy.
