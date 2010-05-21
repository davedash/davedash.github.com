---
wordpress_id: 176
layout: post
title: Star Rating using YUI (and Django)
wordpress_url: http://spindrop.us/2008/03/04/star-rating-using-yui-and-django/
---
[django]: http://djangoproject.com/
[yui]: http://developer.yahoo.com/yui/
[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/

I have a very good star rater on [reviewsby.us][rbu], but it was written using
some sloppy prototype code.  I wanted to redo star raters in a well thought out
manner and I wanted to use [YUI][].  In this particular tutorial I will use
[Django][] although it is not a requirement.

For some background information on star raters, see this
[Yahoo! Design Pattern][yp].  Our pattern is more of a join star rater, similar
to what's found on Netflix: you see an average rating for a restaurant or dish
unless you yourself have rated it.

This was a thought out design decision for our [reviewsby.us][rbu] redesign.
Our site is primarily a personal utility that answers the question, "What
dishes do I like at a particular restaurant?"  If you haven't rated something
the website can only offer up an average and you can use that as a decision as
to whether you should eat something or not.

If you have eaten something however, that average rating is irrelevant.  You
don't need fellow meal advisors to tell you that you liked Chicken Makhani, you
already know that for yourself.  Therefore we show only your rating unless you
haven't rated something.

### Working backwards

I like to "work backwards" as it were.  Meaning, I like to just write the code
that I ultimately will use to output a star rater.  From there I will work on
the supporting code that is necessary.  I find by using this strategy, I can
keep my code fairly clean and organized.

### The template ###

So ultimately I want this:
	{\% star 'mything' 3 4 '/path/to/script' %}

To show up as this:

<div style="text-align:center">
<img src="http://spindrop.us/wp-content/uploads/2008/03/starrater.png" alt="starrater.png" border="0" width="105" height="31" />
</div>

<!--more-->

Unfortunately [Django templates][dt] doesn't seem to have named attributes for [template tags][tt], so I'll need to explain my syntax:

[dt]: http://www.djangoproject.com/documentation/templates/
[tt]: http://www.djangoproject.com/documentation/templates_python/

* `star`: is the template tag which we define below
* `'mything'`: is an id string we will use for this rater and its associated objects
* `3`: this is the second argument to star, it will be the users current rating, it can also be None
* `4.1`: this is the third argument, it will be the average rating, it can also be None
* `/path/to/script`: is the form that will process our rating

### The HTML we want

Another developer had a [good approach for handling star ratings][ysr] and for handling Javascript in general.  Create an underlying Javascript-free system, and then let the Javascript make it pretty.  This is way to degrade gracefully.

Ultimately, I had my own approach to this problem, I wanted much of the visual lifting to happen on the CSS layer.  So, we'll use the following code:

<p><textarea name="code" class="html">
<span class="joint_star_rater">
	<form id="rater_restaurant" method="post" action="/restaurant/pizza-luce/rate/">
		<fieldset>
			<legend>Rating</legend>
			<ul>

        <li style="width: 100px;" title="5" class="current meta">Current Rating: 5</li>


		<li title="Poor" class="star_1 star">
			<label for="restaurant_rating_1">Poor</label>
			<input type="radio" name="rating" value="1" id="restaurant_rating_1"/>
		</li>

		<li title="Fair" class="star_2 star">
			<label for="restaurant_rating_2">Fair</label>
			<input type="radio" name="rating" value="2" id="restaurant_rating_2"/>
		</li>

		<li title="Good" class="star_3 star">
			<label for="restaurant_rating_3">Good</label>
			<input type="radio" name="rating" value="3" id="restaurant_rating_3"/>
		</li>

		<li title="Very Good" class="star_4 star">
			<label for="restaurant_rating_4">Very Good</label>
			<input type="radio" name="rating" value="4" id="restaurant_rating_4"/>
		</li>

		<li title="Excellent" class="star_5 star">
			<label for="restaurant_rating_5">Excellent</label>
			<input type="radio" name="rating" value="5" id="restaurant_rating_5"/>
		</li>

			</ul>
		</fieldset>
		<input type="submit" name="rate" value="rate it" class="submit"/>
	</form>
</span>

</textarea></p>

A couple things to note in our HTML.  Our unique string is `restaurant`.  It's got an ID that is as unique as you want: `rater_restaurant` where `restaurant` was the first argument to our template tag.  We use `restaurant` to create some other unique IDs as well.

Also, this rating form makes a lot of sense semantically.  While this form in its current state is a far cry from some ajaxy goodness, it makes clear sense as to what is going on.


### The template tag

Well we know what we want from the HTML side, so let's start coding our `star` tag:

<p><textarea name="code" class="python">
@register.simple_tag
def star(id_string, current, average, path, spanfree=False):
    meta = None
    if current != None:
        meta = """
        <li class="current meta" title="%d" style="width:%dpx">Current Rating: %d</li>
        """ % (int(current), int(current)*20, int(current))
    else:
        meta = """
        <li class="average meta" title="%.1f" style="width:%dpx">Average Rating: %.1f</li>
        """ % (average, average*20,average)

    stars   = ''
    ratings = ['Poor', 'Fair', 'Good', 'Very Good', 'Excellent']

    for i in range(1,6):
        stars = stars + """
		<li class="star_%d star" title="%s">
			<label for="%s_rating_%d">%s</label>
			<input id="%s_rating_%d" type="radio" value="%d" name="rating"/>
		</li>
        """ % (i, ratings[i-1],id_string, i, ratings[i-1], id_string, i, i)
    html = """
	<form action="%s" method="post" id="rater_%s">
		<fieldset>
			<legend>Rating</legend>
			<ul>
			%s
			%s
			</ul>
		</fieldset>
		<input type="submit" class="submit" value="rate it" name="rate"/>
	</form>
    """ % (path, id_string, meta,stars)
    if spanfree:
        return html
    else:
        return """<span class="joint_star_rater">%s</span>""" % html
    return html

</textarea></p>


### The CSS

A lot of work will happen via CSS.  The CSS will remove quite a bit of the textual data that can be interpreted graphically with stars.

The strategy we use is to:

* fix the `UL` at a certain width with a background of grey stars
* decorate the `LI.average` and `LI.current` with repeating stars (blue and orange respectively) with a  `z-index` of `1`
* decorate the `LI.average:hover` and `LI.current:hover` with a transparent background
* decorate `LI:hover input` as a colored in star and a `z-index` of `2`

This might not make sense now, until you see the CSS in full action.  Also for the stars we'll use a sprite of 3 stars.  A grey defunct star as the default background, a blue star if it's the average rating for an item and an orange star if it's what the user wants.

I use the following sprite:
<div style="background: #000;text-align:center; padding:1em">
<img src="http://spindrop.us/wp-content/uploads/2008/03/stars.png" alt="stars.png" border="0" width="20" height="60" />
</div>

The following CSS will do some magic:

<p><textarea name="code" class="css">
.joint_star_rater {display:inline-block;}
.joint_star_rater ul{width:100px;position:relative;height:20px;background:url(../images/icons/stars.png) repeat-x 0 0}
.joint_star_rater li.meta{position:absolute;text-indent:-9999px;display:block;z-index:1;}
.joint_star_rater ul:hover li.meta{display:none;}
.joint_star_rater li.current{background:url(../images/icons/stars.png) repeat-x 0 -40px}
.joint_star_rater li.average{background:url(../images/icons/stars.png) repeat-x 0 -20px}
.joint_star_rater li{height:20px;width:20px;position:absolute;text-indent:-9999px;z-index:3;}
.joint_star_rater li.star_2{left:20px;}
.joint_star_rater li.star_3{left:40px}
.joint_star_rater li.star_4{left:60px}
.joint_star_rater li.star_5{left:80px}
.joint_star_rater li.star_1:hover{width:20px}
.joint_star_rater li.star_2:hover{width:40px}
.joint_star_rater li.star_3:hover{width:60px}
.joint_star_rater li.star_4:hover{width:80px}
.joint_star_rater li.star_5:hover{width:100px}
.joint_star_rater li.star:hover{background:url(../images/icons/stars.png) repeat-x 0 -40px;z-index:2;left:0;}
.joint_star_rater input.submit{display:none;}
</textarea></p>

The `inline-block` value for `display` is not supported very well.  I recently switched to Firefox 3 Beta and it renders as expected.  Firefox 2 has problems with it.  I may revise the CSS later to accommodate it.

### The Javascript

The fundamental drawback to the design here, is that it really only works well with the Javascript on.  In fact, with the CSS on and Javascript off, this code will not work very well for the end user.  This too will be revised in the future.

Our Javascript needs to do something very simple:
* extract the star value you clicked on
* send it to the server
* redraw the stars

It's a very simple operation, but I honestly think other libraries have an advantage to YUI in this regard.<sup id="#fnr_1">[1](#fn_1)</sup>  Here's some unobtrusive code I came up with:

<p><textarea name="code" class="js">
var MA = {}; // MA namespace
MA.e = YAHOO.util.Event;
MA.d = YAHOO.util.Dom;
MA.c = YAHOO.util.Connect;

MA.star_rater = function() {
    var e = YAHOO.util.Event;
    var d = YAHOO.util.Dom;

    return {
        init: function() {
            e.onDOMReady(this.setup,this, true)
        },

        setup: function() {
            e.on(d.get('doc4'),'click',this.handleClick,this,true);
        },

        handleClick: function(ev) {
            var target = e.getTarget(ev);
            if (d.hasClass(target, 'star')
            && d.hasClass(target.parentNode.parentNode.parentNode.parentNode, 'joint_star_rater')) {
                this.rate(target);
            }
        },

        rate: function(el) {
            if (MA.is_authenticated('Please sign in before rating =)')) {

                root   = el.parentNode.parentNode.parentNode.parentNode;
                action      = el.parentNode.parentNode.parentNode.action;
                input       = MA.d.getFirstChildBy(el, function(d) {return (d.tagName == 'input'||d.tagName=='INPUT')});
                this.value  = input.value;
                postdata    = "value="+this.value;

                handleSuccess = function(o) { root.innerHTML = o.responseText }
                callback = {
                    success:handleSuccess,
                }


                var request = MA.c.asyncRequest('POST', action, callback, postdata);
                // construct a connection object to this and use it to make a post
                // retrieve the post and then replace it with the original span
            }
        },

    }
}();

MA.star_rater.init();
</textarea></p>

Note: I intentionally left out irrelevant pieces of code, like the function definition of `MA.is_authenticated()`, this code isn't meant for cutting and pasting, it's meant for cutting-pasting and then some careful editing.

### The callback view

The callback script is what you specify when you call `{\% star ... %}`.  The view I use is as follows:

<p><textarea name="code" class="python">
@login_required
def rate(request, slug):
    MyObject = get_my_object()
    value    = request['value']

    MyObject,rate(value);
    return render_to_response("rating.html", locals(), context_instance=RequestContext(request))

</textarea></p>

That code is oversimplified... you have to write your own logic as it applies to our site.  The `rating.html` is simply the call to your star tag:

	{\% load tags %}
	{\% star 'mything' restaurant.current_rating restaurant.average_rating restaurant.get_rating_url 1 %}

Note the `1` at the end.  It's a flag to turn off the outer `span` so we can just insert the guts back into the original `span`.

### Final Thoughts

The star-rater is really a large problem that's hard to tackle in one sitting and quite frankly is not documented well anywhere.  The code I've provided is a shadow of the real code I'll be using, but hopefully it's enough to get you started.

I definitely will update my production code to solve a few outstanding issues, as I mentioned above.  I'll try to update this tutorial at the same time.  If there are questions about the examples given, feel free to ask and I'll attempt to answer.

[ysr]: http://www.unessa.net/en/hoyci/projects/yui-star-rating/
[yp]: http://developer.yahoo.com/ypatterns/pattern.php?pattern=ratinganobject

<div class="footnotes">
<ol>
<li id="fn_1">YUI has the <code>Selector</code> and that might alleviate some problems, but jQuery has very nice selection capabilities.  In this future version I keep promising, I'll use the YUI <code>Selector</code> <a href="#fnr_1" class="footnoteBackLink"  title="Jump back to footnote 1 in the text.">&#8617;</a></li></ol>
</div>
