--- 
wordpress_id: 83
layout: post
title: PHP double versus single quotes
wordpress_url: http://spindrop.us/2007/03/03/php-double-versus-single-quotes/
---
[tags]best practices, php[/tags]

If you're familiar with PHP, the difference between double and single quotes is obvious.  Double quotes evaluate variables and control characters (e.g. `\n` or `\r`), whereas single quotes do not.

I've been indoctrinated with the "use single quotes whenever possible" methodology, but I never really put it to the test.  Is it really worth it for me to go back and look at old code that uses double quotes and change them?  Like all best practices, the answer is "maybe."

So I wrote a simple test harness (there's a lot of room for error with these, but I tried my best).  

<div><textarea name="code" class="php">
<?php

define ('MAX',2000000);

function f1()
{
    for($i=0;$i<MAX; $i++)
    {
        $c = "test " . $i;
    }
}


function f2()
{
    for($i=0;$i<MAX; $i++)
    {
        $c = "test $i";
    }
}


function f3()
{
    for($i=0;$i<MAX; $i++)
    {
        $c = 'test ' . $i;
    }
}



$t1 = microtime(true);
f1();
echo 'Time 1: ' , (microtime(true) - $t1) , "\n";

$t2 = microtime(true);
f2();
echo 'Time 2: ' , (microtime(true) - $t2) , "\n";

$t3 = microtime(true);
f3();
echo 'Time 3: ' , (microtime(true) - $t3) , "\n";



</textarea></div>

I tried different permutations of which order to run `f1()`, `f2()` and `f3()` they seemed to give similar results no matter which order they were run.  

My results were:

<pre>
Time 1: 2.898087978363
Time 2: 3.5480048656464
Time 3: 2.8503499031067
</pre>

My interpretation is that quotes versus double quotes isn't as big of a deal as concatenation versus putting variables within double quotes.  My guess is that PHP 5.2.0 (which is what I used for the tests) is smarter with strings than older versions.

So really if you look at the test harness there isn't any discernible differences until you hit 2 million iterations and even then nobody gets fired over 0.6 seconds of performance.  Chances are it doesn't matter too much, but over time you can write enough code in the right spots or shared in the right open source projects and that few seconds will snowball.  After all, I'm not so much concerned about how optimized a script is that I write, but rather how optimized is a script that everyone ends up using.  But rather than do mental calculations about whether or not to optimize something, let's just assume that everything should be as optimal as we can stand to write it.

Update: 6 March 2006, I updated the test harness to reflect my intended tests.
Update: 7 March 2006, I updated the results to be more clear.
