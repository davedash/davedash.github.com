--- 
wordpress_id: 63
layout: post
title: Using Zend Search Lucene in a symfony app
wordpress_url: http://spindrop.us/2006/08/25/using-zend-search-lucene-in-a-symfony-app/
---
[tags]zend, search, lucene, zend search lucene, zsl, symfony,php[/tags]

[a21]: http://symfony-project.com/askeet/21
[zsl]: http://framework.zend.com/manual/en/zend.search.html
[symfony]: http://symfony-project.com/
[zdz1]: http://devzone.zend.com/node/view/id/91 "Roll Your Own Search Engine with Zend_Search_Lucene"
[zdz]: http://devzone.zend.com/
[dl]: http://framework.zend.com/download "Zend Framework Download"
[zf]: http://framework.zend.com/
[srbu]: http://spindrop.us/category/reviewsbyus "ReviewsBy.Us category of Spindrop"

If you're like me you've probably followed the [Askeet tutorial on Search][a21] in order to create a decent search engine for your web app.  It's fairly straight forward, but they hinted that when [Zend Search Lucene][zsl] (<acronym title="Zend Search Lucene">ZSL</acronym>) is released, that might be the way to go.  Well we are in luck, [<acronym title="Zend Search Lucene">ZSL</acronym>][zsl] is available, so let's just dive right in.





<!--more-->

[a21]: http://symfony-project.com/askeet/21
[zsl]: http://framework.zend.com/manual/en/zend.search.html
[symfony]: http://symfony-project.com/
[zdz1]: http://devzone.zend.com/node/view/id/91 "Roll Your Own Search Engine with Zend_Search_Lucene"
[zdz]: http://devzone.zend.com/
[dl]: http://framework.zend.com/download "Zend Framework Download"
[zf]: http://framework.zend.com/
[srbu]: http://spindrop.us/category/reviewsbyus "ReviewsBy.Us category of Spindrop"

If you aren't using [symfony] have a look at [this article][zdz1] from the [Zend Developer Zone][zdz].  It covers just enough to get you started.  If you are using [symfony], just follow along and we'll get you where you need to go.

### Obtaining Zend Search Lucene

First [download][dl] the [Zend Framework][zf] (<acronym title="Zend Developer Framework">ZF</acronym>).  The [Zend Framework][zf]  is supposed to be fairly "easy" in terms of installation.  So let's put that to the test.  Open your [<acronym title="Zend Developer Framework">ZF</acronym>][zf] archive.  Copy `Zend.php` and `Zend/Search` to your [symfony] project's library folder:

	cp Zend.php $SF_PROJECT/lib              
	mkdir $SF_PROJECT/lib/Zend
	cp -r Zend/Search $SF_PROJECT/lib/Zend
	cp Zend/Exception.php $SF_PROJECT/lib/Zend                 
	chmod -R a+r $SF_PROJECT/lib/Zend*


### Index Something

We'll deviate slightly from [food themed][srbu] tutorials and do something generic.  Let's try a user search where we can find a user by their name or email address.  It's fairly simple to accomplish, and hardly requires the use of [<acronym title="Zend Search Lucene">ZSL</acronym>][zsl], but by using <acronym title="Zend Search Lucene">ZSL</acronym> we can easily extend it to do a full-text search of a user's profile or any other textual data.

Each "thing" stored in the index is a "document" in <acronym title="Zend Search Lucene">ZSL</acronym>, specifically a `Zend_Search_Lucene_Document`.  Each document then consists of several "fields" (`Zend_Search_Lucene_Field` objects).  In our example, our document will be an individual user and the fields will be relevant attributes of the user (username, first name, last name, email, the text of their profile).

We're going to write a general re-indexing tool.  Something that will index all users.  

In our `userActions` class let's add the following action:

<div><textarea name="code" class="php">
	public function executeReindex()
	{
		require_once 'Zend/Search/Lucene.php';
		$index = new Zend_Search_Lucene(sfConfig::get('app_search_user_index_file'),true);
		
		$users = UserPeer::doSelect(new Criteria());
		foreach ($users AS $user)
		{
			$doc = new Zend_Search_Lucene_Document();
			$doc->addField(Zend_Search_Lucene_Field::Keyword('id', $user->getId()));
			$doc->addField(Zend_Search_Lucene_Field::Keyword('username', $user->getUsername()));
			$doc->addField(Zend_Search_Lucene_Field::Keyword('email', $user->getEmail()));
			$doc->addField(Zend_Search_Lucene_Field::Text('firstname', $user->getFirstname()));
			$doc->addField(Zend_Search_Lucene_Field::Text('lastname', $user->getLastname()));
			$doc->addField(Zend_Search_Lucene_Field::Unstored('contents', "{$user->getEmail()} {$user->getFirstname()} {$user->getLastname()} {$user->getUsername()}"));
			$index->addDocument($doc);
		}
		
		$index->commit();
	}
</textarea></div>

The code should be fairly easy to follow.  First of all we're requiring the necessary libraries for Lucene.  The next line we are creating the index:

<div><textarea name="code" class="php">
	$index = new Zend_Search_Lucene(sfConfig::get('app_search_user_index_file'),true);
</textarea></div>

`app_search_user_index_file` is a symfony configuration that you define in your `app.yml`.  It defines which file you want to use for your index.  `/tmp/lucene.user.index` works for our purposes.   The second parameter tells Lucene we are creating a new index.

We then loop through all the users and for each user create a document.  For all the search relevant attributes that a user might have we add a field into the document.  Note the last field:

<div><textarea name="code" class="php">
	$doc->addField(Zend_Search_Lucene_Field::Unstored('contents', "{$user->getEmail()} {$user->getFirstname()} {$user->getLastname()} {$user->getUsername()}"));
</textarea></div>

By default search is made for the "contents" field.  So in this example we want people to be able to type in someone's name, email, username without having to specify what field we're searching for.

### Find those users

Finding the user's is equally as straight-forward.  We make a new action called `search`:

<div><textarea name="code" class="php">
	public function executeSearch()
	{
		require_once('Zend/Search/Lucene.php');
		$query = $this->getRequestParameter('q');
	
		$this->getResponse()->setTitle('Search for \'' . $query . '\' &laquo; ' . sfConfig::get('app_title'), true);
	
		$hits = array();
	
		if ($query)
		{
			$index = new Zend_Search_Lucene(sfConfig::get('app_search_user_index_file'));
			$hits = $index->find(strtolower($query));
		}
		$this->hits = $hits;
	}

The magic happens in our `if` statement:

	if ($query)
	{
		$index = new Zend_Search_Lucene(sfConfig::get('app_search_user_index_file'));
		$hits = $index->find(strtolower($query));
	}
</textarea></div>

If we have a query, open the [ZSL] index (note that we only have one parameter here).  Run the `find` method to find our query and store it to the `$hits` array.  Note that our query was cleaned with `strtolower`, since [ZSL] is case sensitive.

The template takes care of the rest:

<div><textarea name="code" class="php">
	<?php use_helper('Form');?>
	<?php echo form_tag('@search_users') ?>
	<?php echo input_tag('q'); ?>
	<?php echo submit_tag() ?>
	</form>
	<?php foreach ($hits as $hit): ?>
	  <?php echo $hit->score ?>
	  <?php echo $hit->firstname ?>
	  <?php echo $hit->lastname ?>
	  <?php echo $hit->email ?>
	<?php endforeach ?>
</textarea></div>

Fairly simple... but it could use some cleaning up (enjoy).

### What about new users?	

Regularly reindexing might be nice in terms of having an optimized search index, but its lousy if you want to be able to search the network immediately when new people join on.  So why not automatically re-index each user every time they are created or everytime one of their indexed components is summoned?

This should be fairly simple by adding to the `User` class:

<div><textarea name="code" class="php">
	var $reindex = false;
	public function setUsername ( $v )
	{
		parent::setUsername($v);
		$this->reindex = true;
	}
	public function setFirstname ( $v )
	{
		parent::setFirstname($v);
		$this->reindex = true;
	}
	public function setLastname ( $v )
	{
		parent::setLastname($v);
		$this->reindex = true;
	}
	public function setEmail ( $v )
	{
		parent::setEmail($v);
		$this->reindex = true;
	}
</textarea></div>

We have an attribute called `$reindex`.  When it is false we don't need to worry about indexes.  When something significant changes, like an update to your name or email address, then we set `$reindex` to `true`.  Then when we save:

<div><textarea name="code" class="php">
	public function save ($con = null)
	{
		parent::save($con);
		if ($this->reindex) {
			require_once 'Zend/Search/Lucene.php';
			$index = new Zend_Search_Lucene(sfConfig::get('app_search_user_index_file'));
			// first find any references to this user and delete them
			$hits = $index->find('id:'. $this->getId());
			foreach ($hits AS $hit) {
				$index->delete($hit->id);
			}
		
			$doc = $this->generateZSLDocument();
			$index->addDocument($doc);
			$index->commit();
		}
	}
</textarea></div>

We're calling a new function called `generateZSLDocument`.  It might look familiar:

<div><textarea name="code" class="php">
	public function generateZSLDocument()
	{
	
		require_once 'Zend/Search/Lucene.php';
		$doc = new Zend_Search_Lucene_Document();
		$doc->addField(Zend_Search_Lucene_Field::Keyword('id', $this->getId()));
		$doc->addField(Zend_Search_Lucene_Field::Keyword('username', $this->getUsername()));
		$doc->addField(Zend_Search_Lucene_Field::Keyword('email', $this->getEmail()));
		$doc->addField(Zend_Search_Lucene_Field::Text('firstname', $this->getFirstname()));
		$doc->addField(Zend_Search_Lucene_Field::Text('lastname', $this->getLastname()));
		$doc->addField(Zend_Search_Lucene_Field::Unstored('contents', "{$this->getEmail()} {$this->getFirstname()} {$this->getLastname()} {$this->getUsername()}"));
		return $doc;
	}
</textarea></div>

Now, whenever a user is updated, so is our index.  Additionally we can modify our reindex action:

<div><textarea name="code" class="php">
	public function executeReindex()
	{
		require_once('Zend/Search/Lucene.php');
		$index = new Zend_Search_Lucene(sfConfig::get('app_search_user_index_file'),true);
		
		$users = UserPeer::doSelect(new Criteria());
		foreach ($users AS $user)
		{
			
			$index->addDocument($user->generateZSLDocument);
		}
		
		$index->commit();
	}
</textarea></div>

That's a **lot** easier to deal with.


### ...and beyond

Hope this article helps some of you jumpstart your [symfony] apps.  Really cool, easy to implement search is here.  We no longer have to stick with shoddy solutions like HT://Dig or spend time rolling our own full text search, as the [symfony team diligently showed us we could][a21].  But there is a lot more ground to cover.  Including optimization techniques and best practices.

Let me know what you think, and if you use this in any of your apps.


