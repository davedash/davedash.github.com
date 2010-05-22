---
wordpress_id: 140
layout: post
title: YUI Autocomplete the easy way
wordpress_url: http://spindrop.us/2008/01/27/yui-autocomplete-the-easy-way/
site: spindrop
---
[tags]yui, autocomplete, javascript, jquery, symfony[/tags]

I'm redoing the UI for [reviewsby.us][rbu] and for the Javascript library I am standardizing on is [YUI][].  The trick with [YUI][] is that it's very verbose and very configurable.

Unfortunately to do simple things you have to write quite a lot.  Which, coming from a jQuery background, is not what I'm used to.  Yahoo provides a lot of useful examples for Auto Complete, I'll provide you with another (built in [symfony][], but anything in any server-side language will work).  You'll need:

1. A data source
2. Some YUI
3. Some javascript of your own
4. And some HTML


We're building a tool to grab random items from our database and put them into our Autocomplete field.  We also want to capture and id of these items and set them in our form.

Here we go...

[yui]: http://developer.yahoo.com/yui/
[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/
[ac]: http://developer.yahoo.com/yui/autocomplete/
<!--more-->

[yui]: http://developer.yahoo.com/yui/
[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/
[ac]: http://developer.yahoo.com/yui/autocomplete/

### Data Source

YUI gives you a lot of options with data sources.  In many cases a remote script that returns JSON will be best.  JSON is nice, compact, human debuggable and machine-readable.

We can make a `searchJSON` method that simply takes your database results and wraps them in to a formatted array and then using PHP's `json_encode` we can return a nice JSON object.

<div><textarea name="code" class="php">
	public static function searchJSON($phrase, $exact = false, $offset = 0, $max = 10)
	{
		$rs = self::doSearch($phrase, $exact, $offset, $max);

		// Manage the results
		$restaurants = array();
		while ($rs->next())
		{
		  $r                           = self::retrieveByPK($rs->getInt(1));
			$objs[] = array('Id'=>$rs->getInt(1), 'Title'=>$r->getName());
		}

    return json_encode(array('ResultSet' => array("Result" => $objs)));
	}
</textarea></div>

The `ResultSet` and `Result` keys are important as we'll see later.

We can serve this JSON method very easily in symfony like so:
<div><textarea name="code" class="php">
  public function executeAjaxList()
  {
    $q    = $this->getRequestParameter('query');
    $objs = ObjPeer::searchJSON($q);
    return $this->renderText($objs);
  }
</textarea></div>

Note that we use `renderText` rather than a separate `ajaxListSuccess.php` file.

### YUI

There's some [YUI][] code that you need.  It's described well in the [Autocomplete documentation][ac].

Add the following to your page:

	http://yui.yahooapis.com/2.4.1/build/yahoo-dom-event/yahoo-dom-event.js" type="text/javascript
	http://yui.yahooapis.com/2.4.1/build/connection/connection-min.js type="text/javascript
	http://yui.yahooapis.com/2.4.1/build/autocomplete/autocomplete-min.js
	http://yui.yahooapis.com/2.4.1/build/autocomplete/assets/skins/sam/autocomplete.css

These are the bare YUI requirements to get Autocomplete working.

### Javascript

There's a good deal of Javascript that you'll need to provide on your own.  Here's what I wrote:

<div><textarea name="code" class="javascript">
    var MA = {};
    MA.autocomplete = function()
    {
      var e = YAHOO.util.Event;
      var w = YAHOO.widget;
  
      return {
        init: function()
        {
           e.onAvailable("myInput", this.fnHandler);
        },
        fnHandler: function()
        {
          var rDS = new w.DS_XHR("/ajax/object/list", ["ResultSet.Result","Title"]);

          rDS.maxCacheEntries    = 60; 
          rDS.queryMatchContains = true;

          var rAC = new w.AutoComplete("myInput","myACContainer", rDS); 

          rAC.formatResult = function(item, query) 
          {
            return item[1].Title;
          };
      
          rAC.forceSelection           = true; 
          rAC.allowBrowserAutocomplete = false; 
      
          rAC.itemSelectEvent.subscribe(
            function(sType, aArgs) 
            { 
              var data = aArgs[2];
              document.getElementById("object_id").value = aArgs[2][1]['Id'];
            }
          ); 
        },
    
      }
    }();

    MA.autocomplete.init();

</textarea></div>

`MA` is my own private namespace.  `/ajax/object/list` is the url of our data source we defined earlier.  `myInput`, `myACContainer` and `object_id` are all IDs of elements in our DOM which we'll look at next.

### HTML

Okay I went through this backwards, now we have the HTML.

This is all you need:

<div>
<textarea name="code" class="html">
    <div id="myAutoComplete">
      <?php echo input_tag('myInput',null,'class=text') ?>
      <div id="myACContainer"></div>
      <?php echo input_hidden_tag('object_id') ?>
    </div>
</textarea>
</div>

### The End

That's it.  It might seem like a lot, but [YUI][] offers a tested working solution that works and is very customizable.
