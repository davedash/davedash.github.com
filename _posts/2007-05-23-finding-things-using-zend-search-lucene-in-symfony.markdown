--- 
wordpress_id: 101
layout: post
title: Finding things using Zend Search Lucene in symfony
wordpress_url: http://spindrop.us/2007/05/23/finding-things-using-zend-search-lucene-in-symfony/
---
[tags]Zend, Zend Search Lucene, Search, Lucene, php, symfony, zsl[/tags]

[s1]: http://spindrop.us/2007/04/24/creating-updating-deleting-documents-in-a-lucene-index-with-symfony/
[s2]: http://spindrop.us/tag/zsl


<span class="notice">This is part of an [on going series][s2] about the Zend Search Lucene libraries and symfony.  We'll pretty everything up when we're done =)</span>

We now know how to [manipulate the index via our model classes][s1].  But let's actually do something useful with our search engine... let's search!



<!--more-->

[tags]Zend, Zend Search Lucene, Search, Lucene, php, symfony, zsl[/tags]

At the time of this writing we're dealing with Propel which uses `Peer` classes which are meant for dealing with multiple objects<sup id="#fnr_1">[1](#fn_1)</sup>.  This is the perfect place for a `::search()` method.  In otherwords, `UserPeer::search('dave');` should query Lucene for users matching "dave".  Let's make that happen:

<div><textarea name="code" class="php">

	public static function search($query)
	{
		$index = self::getLuceneIndex();
		
		$hits = $index->find(strtolower($query));
		$pks = array();
    
		foreach($hits AS $hit)
		{
			$pks[] = $hit->user_id;
		}
		
		return self::retrieveByPks($pks);
	}

</textarea></div>

What we're doing is retrieving our Lucene index.  Somewhere between tutorials we wrote this `Peer` function to handle that:

<div><textarea name="code" class="php">
	public static function getLuceneIndex($autoIndex = true)
	{
		try 
		{
			return $index = Zend_Search_Lucene::open(sfConfig::get(self::$luceneIndex));
		} 
		catch (Exception $e) 
		{
			$index = $autoIndex ? self::reindex() : null;
			return $index;
		}
	}
</textarea></div>



If our index is missing we'll conveniently create it on the fly.  We then use the Zend Search Lucene API to retrieve the matching hits in this index and then use some Propel trickery to retrieve by an array of primary keys.

It's now simple to use `::search()` functions in the same manner as you use `::doSelect()`.

At this point you should be able to create a basic symfony app that can utilize a Lucene index.


<div id="footnotes">
	<hr/>
	<ol>
		<li id="fn_1">The examples refer to using Propel, but it's trivial to adapt this to sfDoctrine <a href="#fnr_1" class="footnoteBackLink"  title="Jump back to footnote  in the text.">&#8617;</a></li>
	</ol>
</div>
