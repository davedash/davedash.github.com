--- 
wordpress_id: 127
layout: post
title: goto() Bash scripts for changing directories
wordpress_url: http://spindrop.us/2007/11/27/goto-bash-scripts-for-changing-directories/
---
So one of the downsides to symfony is traversing the file system.  Lately I've had to do this a lot so I decided to write some `bash` functions to make this easier.  Here's one I call `goto` which works as such:

    `goto` filename.ext

Feel free to make this better, or if there exists a built-in that I know nothing about tell me about it.

Here's the function:

    goto () {
      FILE=`find . -iname $1|head -1`
      DIR=`dirname $FILE`
      cd $DIR
    }

### Update ###

I changed the function to take care of this syntax:

`goto default/../actions.class.php` (amongst other things) will now find `app/frontend/modules/default/actions`:

    goto () {
        FORMATTED_STR=`echo $1|sed -e 's|/../|/*/|g'`
        FILE=`find . -ipath *${FORMATTED_STR}*|head -1`
        DIR=`dirname $FILE`
        cd $DIR
    }
