---
wordpress_id: 62
layout: post
title: Digg-style AJAX comment editing in PHP/symfony
wordpress_url: http://spindrop.us/2006/08/13/digg-style-ajax-comment-editing-in-phpsymfony/
site: spindrop
tags: [reviewsby.us, programming, symfony]
---
[digg]: http://digg.com/
[s1]: http://spindrop.us/2006/07/02/comment-editing-in-reviewsbyus/ "Comment Editing in reviewsBy.us"

"[Digg]"-style anything can be pretty slick.  The <acronym title="Asynchronus Java and XML">AJAX</acronym>-interactions on that site make it very fun to use.  It's styles have been copied everywhere, and are definitely worth copying.  The latest feature that had caught my eye was the ability to edit your comments for a set time after posting them.  Of course, it wasn't just the ability to edit comments, it was <acronym title="Asynchronus Java and XML">AJAX</acronym> too and it has a timer.

This is totally [something I could use on a restaurant review site][s1].  So I started on this project.  It's pretty straight forward.<!--more-->  For all of your posted comments you check if the owner of them is viewing them within 3 minutes of posting the commen.  3 minutes is usually enough time to notice you made a typo, but if you disagree I'll leave it to you to figure out how to adjust the code.

For example, I make a comment, realize I spelled something wrong and then I can click on my comment to edit it.  Of course using <acronym title="Asynchronus Java and XML">AJAX</acronym> means this all happens without having to reload the web page.  Therefore the edits are seemingly quick.  So let's add it to any web site.

### In Place Forms

First and foremost, the ability to edit a comment means you have a form that you can use to edit and submit your changes.  But rather than deal with creating a boring un<acronym title="Asynchronus Java and XML">AJAX</acronym>y form, we'll enlist the help of [script.aculo.us].  

First, each comment is rendered using the following <acronym title="HypterText Markup Language">HTML</acronym> and PHP:

	<div class="review_block" id="comment_<?php echo $comment->getId() ?>">  
		<p class="author"><?php echo link_to_user($comment->getUser()) ?> - <?php echo $comment->getCreatedAt('%d %B %Y') ?></p>
		<div class="review_text" id="review_text_<?php echo $comment->getId()?>"><?php echo $comment->getHtmlNote() ?></div>
	</div>

Note that this `div` and it's child `div` have unique ids that we can refer back to (`comment_n` and `review_text_n` where `n` is the id of the comment).  We can use this to interact with the <acronym title="Document Object Model">DOM</acronym> via JavaScript.  What we do is for each comment, we check if it is owned by the current visitor *and* if it's within our prescribed 3 minute window.  We can do that with some simple PHP:

	<?php if ($comment->getUser() && $comment->getUserId() == $sf_user->getId() && time() < 181 + $comment->getCreatedAt(null) ): ?>
		<script type="text/javascript">
		//<![CDATA[
			makeEditable('<?php echo $comment->getId() ?>', "<?php echo url_for($module . '/save?id=' . $comment->getId()) ?>", "<?php echo url_for('restaurantnote/show?id=' . $comment->getId() . '&mode=raw') ?>", <?php echo 181-(time() - $comment->getCreatedAt(null)) ?>);
		//]]></script>
	<?php endif ?>	

As you can see we run the `makeEditable()` function for each applicable comment.  As you can guess, `makeEditable()` makes a comment editable.  For parameters it takes the comment's id (so it can refer to it in the <acronym title="Document Object Model">DOM</acronym> and other background scripts).  It also takes as an argument the "save" <acronym title="Universal Resource Locator">URL</acronym> as well as a <acronym title="Universal Resource Locator">URL</acronym> from which it can load the raw comment.  The last argument is for the timer.

Here is our function:

	var editor;
	var pe;
	makeEditable = function(id, url, textUrl, time) {
		var div = $("review_text_" + id);
		
		pe = new PeriodicalExecuter(function() { updateTime(id); }, 1);
		
		Element.addClassName($('comment_' + id), 'editable');
		new Insertion.Bottom(div, '<div class="edit_control" id="edit_control_'+id+'">Edit Comment (<span id="time_'+id+'">'+time+' seconds</span>)</div>');
		
		editor = new Ajax.InPlaceEditor(div, url, { externalControl: 'edit_control_'+id, rows:6, okText: 'Save', cancelText: 'Cancel', 
		loadTextURL: textUrl, onComplete: function() { makeUneditable(id) } });
	}

It does a couple things.  It runs a [PeriodicalExecuter][pe] to run the `updateTime` function which updates our countdown timer.  It adds a <acronym title="Cascading Style Sheets">CSS</acronym> class to our comment `div`.  It adds a control button to edit a comment.  Lastly it uses the [script.aculo.us][] [Ajax.InPlaceEditor][ipe] to do most of the magic.  The hard part is done.  


### Periodic Execution Timer

So the `updateTime` function is reasonably simple.  It finds the time written out in the <acronym title="Document Object Model">DOM</acronym> and decrements it by 1 second each second.  Once it hits zero seconds it disables itself and the ability to edit the block.  Let's take a look:


	updateTime = function(id) {
	  var div = $("time_"+id);
	  if (div) {
	    var time =  parseInt(div.innerHTML) - 1;
	    div.innerHTML = time;
	  }
	  if (time < 1) {
	    pe.stop();
	    var editLink = $('edit_control_'+id);
	    if (Element.visible(editLink)) {
	      makeUneditable(id);
	      editLink.parentNode.removeChild(editLink);
	    }
	  }
	}

### Call backs

We'll need a few call backs for the editor to work properly.  Since many content pieces are converted from something else to <acronym title="HypterText Markup Language">HTML</acronym> and not directly written in <acronym title="HyperText Markup Language">HTML</acronym> we'll need a callback that will load our text.  We'll also need a callback which will save our text (and then display it).

#### Load Text

The first call back we can see is referenced in the `makeEditable()` function.  In our example it's:

	url_for('restaurantnote/show?id=' . $comment->getId() . '&mode=raw');

Which is a [symfony] route to the `restaurantnote` module and the `show` action with an argument `mode=raw`.  Let's take a look at this action:

	public function executeShow ()
	{
    	$this->restaurant_note = RestaurantNotePeer::retrieveByPk($this->getRequestParameter('id'));
    	$this->forward404Unless($this->restaurant_note instanceof RestaurantNote);
	}

All this does is load the text (in our case the [markdown] formatting) into a template.

#### Save Text

The save text url in our example is:

	url_for('restaurantnote/save?id=' . $comment->getId());

Using the [Ajax.InPlaceEditor][ipe] the value of the text-area is saved to the `value` POST variable.  We consume it in our action like so:

	public function executeSave() 
	{
		$note = RestaurantNotePeer::retrieveByPk($this->getRequestParameter('id'));
		$this->forward404Unless($note instanceof RestaurantNote);
		if ($note->getUserId() == $this->getUser()->getId()) {
			$note->setNote($this->getRequestParameter('value'));
			$note->save();
		}
		$this->note = $note;
	}

The note is also sent to a template that renders it, so when the save takes place, the edit form will be replaced with the new text.

### Conclusion

As you can see with some [script.aculo.us] and [symfony], it's fairly easy to mimic "Digg-style" in-place comment editing.  You can test out a real example by visiting [reviewsby.us][rbu].

[script.aculo.us]: http://script.aculo.us/
[pe]: http://www.sergiopereira.com/articles/prototype.js.html#Reference.PeriodicalExecuter "PeriodicalExecutor"
[ipe]: http://wiki.script.aculo.us/scriptaculous/show/Ajax.InPlaceEditor
[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/
