--- 
wordpress_id: 19
layout: post
title: Collecting and displaying phone numbers on the web
excerpt: |
  [re]: http://en.wikipedia.org/wiki/Regular_expression
  [php]: http://php.net/
  
  Using some [regular expressions][re] we can easily convert this:
  
  	8005551212
  
  Into this:
  
  	800.555.1212
  
  In [PHP] we can use this function:
  
  	function format_phone($phone)
  	{
  		return preg_replace("/([0-9]{3})([0-9]{3})([0-9]{4})/", "$1.$2.$3", $phone); 
  	}
  
  Not terribly complicated.  We can even go in reverse and remove the dots as I'll demonstrate below.  Despite the ease of going from a formatted string to a string of digits and back again, we often run into forms that aren't usable.
  
  <!-- break -->

---
[re]: http://en.wikipedia.org/wiki/Regular_expression
[php]: http://php.net/

Using some [regular expressions][re] we can easily convert this:

	8005551212

Into this:

	800.555.1212

In [PHP] we can use this function:

	function format_phone($phone)
	{
		return preg_replace("/([0-9]{3})([0-9]{3})([0-9]{4})/", "$1.$2.$3", $phone); 
	}

Not terribly complicated.  We can even go in reverse and remove the dots as I'll demonstrate below.  Despite the ease of going from a formatted string to a string of digits and back again, we often run into forms that aren't usable.

<!-- break --><!--more-->


## Input of phone numbers

Practical everyday usability involves following some basic design guidelines.  One maxim is, computers are made for mundane repetitive tasks.  If you're making a user do something mundane and repetitive, perhaps some automation is in order.  


Requiring a user to [format a number a specific way is mundane][ui1].  It serves little purpose, and contributes to form validation errors, confusion and errors.  Forms are always frustrating because they need to be filled out for every web site and web service.  Websites don't typically collaborate on how form items will work, especially phone numbers and dates.  I live in the <acronym title="United States">US</acronym> and there are a few ways to format a phone number, here:

* 800.555.1212
* 800-555-1212
* (800) 555-1212
* 800/555-1212

Or anything that separates the area code (800 in our example), the exchange (555) and the last four digits (1212).  There's a number of approaches to inputing these in a standard way that allows us to store the data uniformly.  If we were to create a phone directory from the [reviewsby.us][rbu] site, for example, and people chose at random what phone format they'd use, we'd have quite an unprofessional display of digits, parenthesis, hyphens and slashes.

### Input the numbers in a specific format

The easiest is to tell a user that numbers need to be entered in a specific format:

> Phone: <input /> (format: 800-555-1212)

This solution isn't half bad...  Someone using the form knows to enter the number as directed.  This can be frustrating for someone who has a different preference for entering in numbers.  For example, I like to cut to the chase and just enter the digits.  My $20 cell phone can figure it out when I enter 10 digits in a row, why can't a web site.  If I enter `8005551212`, I might get hit with form validation errors on a site that asks for hyphens.

A rigid interpretation of this solution is *all* bad.

### Input numbers separately

Another technique is having three input fields for entering the phone number:

	Phone: (<input size="3"/>) <input size="3"/> - <input size="4"/>

This is three forms for what amounts to one piece of data.  Not easy to use.  It inevitably requires some data massaging on the computer side, so if we need to expend that effort anyway, let's find a more usable solution.

### Javascript to the Rescue?

No!  There's two ways which we see Javascript involved.  One is the enforced formatting.  As you type numbers your entry is magically formatted before you hit submit.  The other allows you to use three forms and the cursor moves from one field to the next as you type out the digits.

The trouble with both of these, is the user isn't expecting this to happen.  So they have to learn your system.  No matter how clever or unobtrusive you are, it ends up being problematic to do something unexpected.

### Inputting numbers in any format

Open the floodgates.  Let the server handle everything.  A user should be able to use any phone number format.  When the form starts processing, if there's at 10-11 digits and the server thinks it's reasonably valid, let them pass.  Store just the digits in the database.

The following PHP code can take care of this input:

	$phone = preg_replace('/\D/', '', $phone);

If you're new to regular expressions, all this code is doing is searching for non digits, `\D`, and replacing them with empty strings, thus leaving us with only digits.  In our above list, each formatting would be stored on our system as `8005551212`.  This makes a lot of sense.

## Outputting that number

Keeping the data as a string of digits allows the above code `preg_replace("/([0-9]{3})([0-9]{3})([0-9]{4})/", "$1.$2.$3", $phone);` the ability to easily parse it into any format.  Not into the *hip* dot notation?  How about hyphens?  No problem, `preg_replace("/([0-9]{3})([0-9]{3})([0-9]{4})/", "$1-$2-$3", $phone);`  Simple regular expressions can change a string of digits into any format you'd like.  Amazingly simple, so let the computer do the work and save us humans the trouble of learning the phone number format du jour.

You can view this in practice by [adding a restaurant to reviewsby.us][rbu] or at least looking at the page for a [restaurant location][r2].

[r2]: http://reviewsby.us/restaurant/cheesecake-factory/location/southdale-center
[rbu]: http://reviewsby.us/
[ui1]: http://www.useit.com/alertbox/20031222.html
