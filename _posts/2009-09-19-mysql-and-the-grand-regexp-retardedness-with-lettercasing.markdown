---
wordpress_id: 317
layout: post
title: mySQL and the grand regexp retardedness with lettercasing
wordpress_url: http://spindrop.us/?p=317
site: spindrop
---
I wanted to find a list of Firefox addons that had smushed text in their title.  E.g. FireBug or StumbleUpon.  The normal porter stemming algorithm that Sphinx uses does not turn "StumbleUpon" into "stumbl upon" as it would with "Stumble Upon".  I was hoping for, and unfortunately could not find a method to do a regular expression search/replace using mysql.  If I could, I could have Sphinx read "StumbleUpon" as "Stumble Upon" and all would be well (although in theory this would backfire).

So my Plan B was to get a list of common smushed named addons (I'd say camelCase, but camelCase is different from SmushedText).  Naturally I used my exceptional skill at regular expressions to concoct this query:

    mysql> SELECT name FROM translated_addons WHERE name REGEXP '[a-z][A-Z][a-z]' = 1 LIMIT 10;
    +------------------------+
    | name                   |
    +------------------------+
    | Orbit Grey             | 
    | Phoenity               | 
    | Pinball                | 
    | Qute                   | 
    | FirefoxModern          | 
    | Adblock                | 
    | Add Bookmark Here      | 
    | All-in-One Gestures    | 
    | Bookmarks Synchronizer | 
    | Browser Uptime         | 
    +------------------------+
    10 rows in set (41.28 sec)

Wait... none of these match.  I scratched my head for a bit and then thought, oh wait, mysql is case insenstivie maybe it's turning `[a-z][A-Z][a-z]` into `[a-z][a-z][a-z]` &#8213; stupid, but consistent with mysql.  Then I pulled my other regexp card out of my sleve, character classes:

    mysql> SELECT name FROM translated_addons WHERE name REGEXP '[[:lower:]][[:upper:]][[:lower:]]' = 1 LIMIT 10;
    +------------------------+
    | name                   |
    +------------------------+
    | Orbit Grey             |
    | Phoenity               |
    | Pinball                |
    | Qute                   |
    | FirefoxModern          |
    | Adblock                |
    | Add Bookmark Here      |
    | All-in-One Gestures    |
    | Bookmarks Synchronizer |
    | Browser Uptime         |
    +------------------------+
    10 rows in set (12.96 sec)

No difference.  Time to pull out the [mysql documentation](http://dev.mysql.com/doc/refman/5.1/en/regexp.html):

> REGEXP is not case sensitive, except when used with binary strings. 

ORLY?

Case-insenstive regular expressions when looking for `[[:upper:]]` or `[[:lower:]]`?  Fine... I'll add some syntax to make you work right:

    mysql> SELECT DISTINCT name FROM translated_addons WHERE name REGEXP BINARY '[[:lower:]][[:upper:]][[:lower:]]' = 1 LIMIT 10;
    +---------------------------+
    | name                      |
    +---------------------------+
    | FirefoxModern             |
    | ChatZilla                 |
    | ChromEdit                 |
    | CuteMenus                 |
    | DownloadWith              |
    | easyGestures              |
    | JavaScript Console Status |
    | LinkVisitor               |
    | OpenBook                  |
    | QuickNote                 |
    +---------------------------+
    10 rows in set (9.68 sec)

That's more like it!

Unfortunately there's about 2609 addons matching this query and since I can't automatically fix these in mysql, I'll need to do some work:

    1.  Create a new table for additional indexable data.
    2.  Upon creation of any new addons with names that have SmushedText - store the "un smushed text".
    3.  Index this "extras" field in Sphinx.

Bug: [517699](https://bugzilla.mozilla.org/show_bug.cgi?id=517699)
