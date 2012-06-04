---
layout: post
title: "Pinternationalization"
tags: [mozilla, pinterest, i18n, spanish]
published: true
time: 10:54AM
---

We [translated our site to **Spanish**][pin] and will **continue to translate it into other languages** in the future.

One day, I came into work and they said, "You are in charge of Internationalization now."  I won't lie, it wasn't the most exciting news--for most developers, *localization is a daunting task*.  I brought this upon myself after emailing my fellow engineers about [how to do localization][0].  At [Mozilla WebDev][1] localization is a core-competency.  You work closely with a team of volunteer translators and you appropriately extract a variety of messages.  Mozilla even built some useful tools to help with this.

I adapted this process for Pinterest and I've come to *enjoy* localization.

## How localization works.

In general localizing a web site involves a few steps steps:

* **Message marking:** Any message on the site (e.g. "Hello Dave", "Login", "Repin") has to be "marked" as localizable.
* **Message extraction:** We have a tool that extracts any messages found in our codebase and builds a translation template.
* **Translation:** This involves taking a file filled with English messages and adding a translation for each one in multiple languages.
* **Compilation:** Each message is compiled into a binary format that allows for fast translation lookups.

It seems deceptively simple, but it can get very complicated as you'll see.

## How it worked at Mozilla

At Mozilla any text we wrote *had* to be localized.  It's very much a global organization.  For example a message like this:

    {% highlight jinja %}
        Hello Dave
    {% endhighlight %}

Would probably look like this before we localize it:

    {% highlight jinja %}
        {% raw %}
            Hello {{ firstname }}
        {% endraw %}
    {% endhighlight %}

To localize it we would wrap it using some special 'tags' or 'functions':

    {% highlight jinja %}
        {% raw %}
            {{ trans }}
                Hello {{ firstname }}
            {{ endtrans }}
        {% endraw %}
    {% endhighlight %}

These special tags served two purposes:

1. They will look up in a message database what the translation is.
2. They let our [internal tools][tower] find these messages, so our translators can translate them.

Step 2 is what we call extraction.  Some teams at Mozilla would automate this process and automatically email the localizers that the messages are ready for translation.

We had [a tool][3] that allowed volunteers to begin translating.  These translators had leaders and the leaders worked with people at Mozilla to make sure the process was working.

The translated strings would automatically saved to our code repository and we'd then compile that before we deployed a web site.

## How it works (for now) at Pinterest

The Mozilla process worked well, but there was a lot of [awkward steps][4] that I didn't want to replicate.  Unfortunately we still had to markup strings.  It's a lot more difficult to do this with a social networking site (versus the Mozilla web sites) because you get messages like this:

    Bob and 6 others liked your pin.

This involved writing a uniquely translatable messages for:

* Bob liked your pin.
* Bob and 1 other liked your pin.
* Bob and `n` others liked your pin.

The hardest part was Pinterest was built without translation in mind--therefore assumptions were made about how we could dynamically construct sentences.  For example (pseudo-code):

    message = "Bob"
    if others:
        message += "and n other"
        if n != 1:
            message += "s"
    message += "liked your pin"

Localizing those four fragments ("Bob", "and n other", "s" and "liked your pin") wouldn't work as different languages have different rules for plurality, ordering of subjects and general sentence construction.

I spent a lot of time correcting these types of messages as well as doing in person code reviews in order to help other developers construct their own sentences.  This is an on-going process and probably the most difficult part of translating .

For a lot of these strings, it was a real simple change, I employed a lot of [vim macros][vim] to assist me (``set paste`` is your friend).

A tool that could find unmarked messages in our codebase would have been immensely useful.  Instead I [wrote a script][6] to build a "!!!YELLING!!!" translation which uppercases everything and adds exclamations.  This is a similar strategy that many teams use, including the [Firefox Add-ons][fa] team, for finding untranslated text.

### Translation

My colleague, Sarah, has been building a translation team.  Together we figured out how we wanted to start.  We decided to hire native translators who are familiar with our site.  The feedback and discussion we've received for Latin American Spanish has been great.  From them we're able to identify things that are difficult to translate, and help build better message strings and context so that a translator can effectively do help write copy for our site.

Context can be screenshots (using [CloudApp] heavily) or just a lengthy comment explaining where a word is used in the site.

To help facilitate the actual translation we employ [Transifex][tx] as a translation hub:

* We take our extracted message template, upload it to transifex.
* Transifex merges those strings into templates for each language.
* Translators can download those language files and translate them, or they can translate them on the Transifex site directly.
* We download the translated strings.

We automate this process and upload our messages weekly and download translations twice daily.  This means developers just need to worry about marking new strings, everything routine is done for them.

### Lessons

**This process has gone well.**  We really liked focusing on *one language* to begin.  It helped us narrow our focus.  We learned that picking a *small set of translators* and eliminating as many of the levels as you can between engineer and translator is very useful.  Keeping that loop tight allows you to keep translation quality high.

We had a lot of outside help.  My former team, the web devs at Mozilla, specifically [Wil Clouser][wc], helped create some useful tools like [tower].  This utilizes [gettext] and [babel] which actually make light work of supporting internationalization.  A lot of people, including Dan from Dropbox and Dimitri from Transifex have given us a lot of great advice, both technically and operationally.  We've also had a lot of help from translators, volunteers and friendly Pinterest users, so thanks!

I'm excited to have Pinterest available to Spanish speakers (European Spanish is coming soon), and I'm excited to continue to bring this to the rest of the world.



[0]: http://playdoh.readthedocs.org/en/latest/userguide/l10n.html#good-practices
[1]: http://webdev.mozilla.org
[tower]: https://github.com/clouserw/tower
[3]: https://localize.mozilla.org/
[4]: http://mozweb.readthedocs.org/en/latest/l10n.html

[cloudapp]: http://getcloudapp.com/
[people]: http://www.hulu.com/watch/12879/office-space-people-skills
[tx]: http://transifex.net
[vim]: https://gist.github.com/2474435
[wc]: http://micropipes.com/blog/
[gettext]: http://www.gnu.org/software/gettext/
[babel]: http://babel.edgewall.org/
[6]: https://gist.github.com/2586745
[fa]: http://micropipes.com/blog/2012/05/31/adding-a-debug-language-to-%C8%A7%E1%B8%93%E1%B8%93-%C7%BF%C6%9Es-%E1%B8%BF%C7%BFzill%C8%A7-%C7%BFr%C9%A0/

[pin]: http://blog.pinterest.com/post/24408983821/pinterest-en-espanol
