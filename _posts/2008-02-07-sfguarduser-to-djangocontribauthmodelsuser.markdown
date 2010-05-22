---
wordpress_id: 157
layout: post
title: sfGuardUser to django.contrib.auth.models.User
wordpress_url: http://spindrop.us/2008/02/07/sfguarduser-to-djangocontribauthmodelsuser/
site: spindrop
---
Let's pretend that your assignment was to convert a symfony app that used sfGuardAuth to a django-based system.  Wouldn't it be great if someone just gave you a bunch of SQL that you could use to convert the [symfony][] `sf_guard_user` table to a [django][] `auth_user` table?

<!--more-->

Here you go:


    REPLACE INTO 
      auth_user

    SELECT 
      p.id AS id, 
      replace(username, 'http://', '') AS username,
      null AS first_name,
      null AS last_name,
      email,
      concat(algorithm,'$',salt,'$',password),
      0 as is_staff,
      1 as is_active,
      0 as is_superuser, 
      last_login,
      u.created_at as date_joined


    FROM 
      `sf_guard_user` u, profile p 

    WHERE
      p.userid = u.id


[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/
[django]: http://djangoproject.com/
