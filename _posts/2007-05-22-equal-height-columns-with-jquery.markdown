---
wordpress_id: 100
layout: post
title: Equal height columns with jQuery
wordpress_url: http://spindrop.us/2007/05/22/equal-height-columns-with-jquery/
site: spindrop
---
[tags]css, jQuery, layout, javascript, equal, columns, equal columns[/tags]

I've seen a few examples of how to equalize column heights using javascript, and none of them seem appealing:

* [jquery.equalizecols.js](http://www.tomdeater.com/jquery/equalize_columns/)
	* This required a few other libraries, and I wanted more flexibility (e.g. where the column should grow in order to equalize)
* [Project 7](http://www.projectseven.com/tutorials/css/pvii_columns/index.htm)
	* The Project 7 approach was the most interesting, but the code seemed a bit messy and not so open source friendly (even thought it might have been).  It would let you specify which element was to grow inside a column.
* [Nifty Corners](http://www.html.it/articoli/nifty/index.html)
	* I had trouble with the syntax, but I liked how it just created a new element out of thin air...

So I wrote my own:

	$("#col1, #col2").equalizeCols();

will equalize the columns as expected


	$("#col1, #col2").equalizeCols("p,p");

will equalize the columns and add the extra space after the `p` tag in `#col1` or `#col2` (whichever is shorter).

Here's our function:
<div><textarea name="code" class="js">

(function($) {
  $.fn.equalizeCols = function(children){
    var child = Array(0);
    if (children) child = children.split(",");
    var maxH = 0;
    this.each(
      function(i) 
      {
        if (this.offsetHeight>maxH) maxH = this.offsetHeight;
      }
    ).css("height", "auto").each(
      function(i)
      {
        var gap = maxH-this.offsetHeight;
        if (gap > 0)
        {
          t = document.createElement('div');
          $(t).attr("class","fill").css("height",gap+"px");
          if (child.length > i)
          {
            $(this).find(child[i]).children(':last-child').after(t);
          } 
          else 
          {
            $(this).children(':last-child').after(t);
          }
        }
      }  
    );
    
  }
})(jQuery);

</textarea></div>

This requires jQuery of course, and it hasn't been tested much.
