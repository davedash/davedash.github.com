---
wordpress_id: 107
layout: post
title: doctine and getState()
wordpress_url: http://spindrop.us/2007/07/10/doctine-and-getstate/
site: spindrop
tags: [spindrop, symfony, php, doctrine, database, errors, sfDoctrine]
---
[tags]doctrine, php, symfony, sfDoctrine, database,errors[/tags]


I tend to have models with a field called `state`.  Doctrine offers a few ways of getting to the `state` field:

	$obj->get('state');
	$obj['state'];

`$obj->getState()` however conflicts with `Doctrine_Record::getState()` from which all objects inherit.  Use one of the above alternatives.
