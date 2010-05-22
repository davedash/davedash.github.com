---
wordpress_id: 94
layout: post
title: The Lucene Search Index and symfony
wordpress_url: http://spindrop.us/2007/04/23/the-lucene-search-index-and-symfony/
site: spindrop
tags: [programming, symfony, symfony, zend, lucene, zend-search-lucene, php, search, index]
---
[tags]Zend, Zend Search Lucene, Search, Lucene, php, symfony, zsl, index[/tags]

[s1]: http://spindrop.us/2006/08/25/using-zend-search-lucene-in-a-symfony-app/
[wf]: http://workface.com/
[sf]: http://symfony-project.com/
[p]: http://archivemati.ca/2007/03/08/zend-search-lucene-symfony-and-the-ica-atom-application/
[zsl]: http://framework.zend.com/manual/en/zend.search.html
[symfony]: http://symfony-project.com/
[szp]: http://www.symfony-project.com/trac/browser/plugins/sfZendPlugin
[zf]: http://framework.zend.com/
[p]: http://archivemati.ca/2007/03/08/zend-search-lucene-symfony-and-the-ica-atom-application/
[zfb]: http://www.symfony-project.com/book/trunk/17-Extending-Symfony#Bridges%20to%20Other%20Framework%20Components

This article is meant to followup [sfZendPlugin](http://spindrop.us/2007/04/10/sfzendplugin/) where we learn a newer way of obtaining the [Zend Framework][zf].

In this tutorial we're going to delve into the Lucene index.  [Zend Search Lucene][zsl] relies on building a Lucene index.  This is a directory that contains files that can be indexed and queried by Lucene or other ports.  In our example we'll be creating a search for user profiles. 



<!--more-->

[s1]: http://spindrop.us/2006/08/25/using-zend-search-lucene-in-a-symfony-app/
[wf]: http://workface.com/
[sf]: http://symfony-project.com/
[p]: http://archivemati.ca/2007/03/08/zend-search-lucene-symfony-and-the-ica-atom-application/
[zsl]: http://framework.zend.com/manual/en/zend.search.html
[symfony]: http://symfony-project.com/
[szp]: http://www.symfony-project.com/trac/browser/plugins/sfZendPlugin
[zf]: http://framework.zend.com/
[p]: http://archivemati.ca/2007/03/08/zend-search-lucene-symfony-and-the-ica-atom-application/
[zfb]: http://www.symfony-project.com/book/trunk/17-Extending-Symfony#Bridges%20to%20Other%20Framework%20Components


We'll want to store in our `app.yml` the precise location of this index file so we can refer to it in our app<sup id="#fnr_lucene_index1">[1](#fn_lucene_index1)</sup>.

Here's an example:

    all:
      search:
	    user_index: /tmp/myapp.user.lucene.index

Now when we need to refer to the index we can do `sfConfig::get('app_search_user_index')`.

### Index Something

Let's try a user search where we can find a user by their name or email address.  It's fairly simple to accomplish, and hardly requires the use of [<acronym title="Zend Search Lucene">ZSL</acronym>][zsl], but by using <acronym title="Zend Search Lucene">ZSL</acronym> we can easily extend it to do a full-text search of a user's profile or any other textual data.

Each "thing" stored in the index is a Lucene "document".  Each document then consists of several "fields" (`Zend_Search_Lucene_Field` objects).  In our example, each document will be an individual user and the fields will be relevant attributes of the user (username, first name, last name, email, the text of their profile).

Initially we'll want to populate our index.  We may also want to regularly reindex all the users at once to optimize the search performance.  Since reindexing involves multiple users it would make sense to have a static `reindex` method in our `UserPeer` class<sup id="#fnr_lucene_index2">[2](#fn_fn_lucene_index2)</sup>.

<div><textarea name="code" class="php">
class UserPeer extends BaseUserPeer
{
	public static function reindex()
	{
		$index = Zend_Search_Lucene::create(sfConfig::get('app_search_user_index'));

		$user = UserPeer::doSelect(new Criteria());
		foreach ($users AS $user)
		{
			$index->addDocument($user->generateZSLDocument());
		}

		return $index;
	}
}
</textarea></div>

Very simply, we're creating a new index, getting all the users, adding a document to the index and then committing the index (to disk).  You might have noticed that there's a strange function, `User::generateZSLDocument()`.  This function contains all the magic.  In order to not repeat ourselves we keep the internals of making a document for the Lucene index in the `User` class itself.  Let's look at it:

<div><textarea name="code" class="php">
	public function generateZSLDocument()
	{
		$doc = new Zend_Search_Lucene_Document();
		$doc->addField(Zend_Search_Lucene_Field::Keyword('uid', $this->getId()));
		$doc->addField(Zend_Search_Lucene_Field::Keyword('username', $this->getUsername()));
		$doc->addField(Zend_Search_Lucene_Field::Keyword('email', $this->getEmail()));
		$doc->addField(Zend_Search_Lucene_Field::Text('firstname', $this->getFirstname()));
		$doc->addField(Zend_Search_Lucene_Field::Text('lastname', $this->getLastname()));
		/* An unstored contents field as an aggregate 
          * of all data is no longer needed in *ZEND* Lucene 
          * But it's here.
          */
		$doc->addField(Zend_Search_Lucene_Field::Unstored('contents', implode(' ', array($this->getEmail(), $this->getFirstname(), $this->getLastname(), $this->getUsername())));
		return $doc;
	}
</textarea></div>

We're really just dumping the relevant search terms into this document.  The beauty of keeping this code internalized in the `User` class is we can reuse it later if we need to index a single `User` at a time.

A couple things to note.  `Zend_Search_Lucene_Field::Keyword` allows us to store data that we can lookup later.  We store the `User::id` in a field called `uid` since `id` is a reserved word for the index and we can't access it from [Zend Search Lucene][zsl].

In a batch script or a reindex action we can now just call `UserPeer::reindex()` and have a working search index for our users.

<div id="footnotes">
	<hr/>
	<ol>
		<li id="fn_lucene_index1">Storing things in <code>app.yml</code> is great for indexes that don't need to be searched in multiple applications. <a href="#fnr_lucene_index1" class="footnoteBackLink"  title="Jump back to footnote 1 in the text.">&#8617;</a></li>
		<li id="fn_lucene_index2">
Since we're using a Lucene index, which has an open documented structure, we aren't limited to just using Zend Search Lucene or Apache Lucene (java).  We can mix and match and read and write to the same index file.  For very large indexes (65,000+ documents), I rewrote a Java application to index all the documents at once as PHP would time out during such a task.
<a href="#fnr_lucene_index2" class="footnoteBackLink"  title="Jump back to footnote 2 in the text.">&#8617;</a></li>
	</ol>
</div>
