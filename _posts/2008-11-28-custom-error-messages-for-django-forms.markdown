---
wordpress_id: 200
layout: post
title: Custom error messages for Django forms
wordpress_url: http://spindrop.us/?p=200
site: spindrop
tags: [spindrop, django, forms]
---
For some reason, it was difficult for me to find the documentation for this.  If your Django form field is required you'll by default get an error stating that 'This field is required.'  You can easily replace that when defining your form like so:


	class ReviewForm(forms.Form):
	    rating = forms.ChoiceField(choices=STARS, error_messages={'required': 'Please choose a star rating'})
	    note   = forms.CharField(widget=forms.Textarea(),)
    
`error_messages` is just a simple dictionary of validation messages that override the default.

While this is properly documented it was not quickly searchable.  But the [django form fields reference page](http://docs.djangoproject.com/en/dev/ref/forms/fields/) documents this well.
