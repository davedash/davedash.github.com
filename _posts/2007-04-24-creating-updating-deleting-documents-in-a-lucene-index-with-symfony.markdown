---
wordpress_id: 95
layout: post
title: Creating, Updating, Deleting documents in a Lucene Index with symfony
wordpress_url: http://spindrop.us/2007/04/24/creating-updating-deleting-documents-in-a-lucene-index-with-symfony/
site: spindrop
---
[s2]: http://spindrop.us/2007/04/23/the-lucene-search-index-and-symfony/

Previously we covered [an all-at-once approach][s2] to indexing objects in your symfony app.  But for some reason, people find the need to allow users to sign up, or change their email addresses and then all of a sudden our wonderful Lucene index is out of date.  

Here lies the strength of using [Zend Search Lucene][zsl] in your app, you can now get the flexibility of interacting with a Lucene index, no matter how it was created and add, update and delete documents to it.

[zsl]: http://framework.zend.com/manual/en/zend.search.html






<!--more-->






[s1]: http://spindrop.us/2006/08/25/using-zend-search-lucene-in-a-symfony-app/
[s2]: http://spindrop.us/2007/04/23/the-lucene-search-index-and-symfony/
[wf]: http://workface.com/
[sf]: http://symfony-project.com/
[p]: http://archivemati.ca/2007/03/08/zend-search-lucene-symfony-and-the-ica-atom-application/
[zsl]: http://framework.zend.com/manual/en/zend.search.html
[symfony]: http://symfony-project.com/
[szp]: http://www.symfony-project.com/trac/browser/plugins/sfZendPlugin
[zf]: http://framework.zend.com/
[p]: http://archivemati.ca/2007/03/08/zend-search-lucene-symfony-and-the-ica-atom-application/
[zfb]: http://www.symfony-project.com/book/trunk/17-Extending-Symfony#Bridges%20to%20Other%20Framework%20Components

The last thing you want to do is have a cron job in charge of making sure your index is always up to date by reindexing regularly.  This is an inelegant and inefficient process.

A smarter method would be to trigger an update of the index each time you update your database.  Luckily the <acronym title="Object Relational Mapping">ORM</acronym> layer allows us to do this using objects (in our case Propel objects).

If we look at our [user example from before][s2], we did set ourselves up to easily do this using our `User::generateZSLDocument()` function, which did most of the heavy lifting.

We can make a few small changes to the `User` class:

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

We have an attribute called `$reindex`.  When it is false we don't need to worry about the index.  When something significant changes, like an update to your name or email address, then we set `$reindex` to `true`.  Then when we save with an overridden save method:

<div><textarea name="code" class="php">
	public function save ($con = null)
	{
		parent::save($con);
      
		if ($this->reindex) 
		{
			$index = $this->removeFromIndex();
			$doc   = $this->generateZSLDocument();
			$index->addDocument($doc);
		}
  	}

	public function removeFromIndex() 
	{
		$index = Zend_Search_Lucene::open(sfConfig::get('app_search_user_index'));  

		// remove old documents
		$term  = new Zend_Search_Lucene_Index_Term($this->getId(), 'userid');
		$query = new Zend_Search_Lucene_Search_Query_Term($term);
		$hits  = array();
		$hits  = $index->find($query);

		foreach ($hits AS $hit) 
		{  
			$index->delete($hit->id);  
		}

		return $index;		
	}
</textarea></div>

Now we've got the *exact* same data that we created during [our original indexing][s2].  This handled creating and updating object, but we miss updating the index when deleting objects.  

Luckily we already made a function `User::removeFromIndex()` to remove any related documents from the index, so our delete function can be pretty simple:

<div><textarea name="code" class="php">
	public function delete($con = null)
	{
		parent::delete($con);
		$this->removeFromIndex();
	}
</textarea></div>
