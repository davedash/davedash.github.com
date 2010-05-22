---
wordpress_id: 102
layout: post
title: Boosting terms in  Zend Search Lucene
wordpress_url: http://spindrop.us/2007/05/29/boosting-terms-in-zend-search-lucene/
site: spindrop
tags: [programming, symfony, symfony, zend, lucene, zend-search-lucene, php, search]
---
[tags]Zend, Zend Search Lucene, Search, Lucene, php, symfony, zsl[/tags]

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


### Boosting terms &mdash; some fields are better than others

[Lucene][zsl] supports boosting or weighting terms.  For example, if I search for members of a web site, and I type in <q>Dash</q>, I want people with the name <q>Dash</q> to take precendence over somebody who has a hobby of running the 50-yard Dash.

If we look at our `generateZSLDocument()` method we defined we just need to adjust a few lines:
<div><textarea name="code" class="php">

		$doc->addField(Zend_Search_Lucene_Field::Text('firstname', $this->getFirstname()));
		$doc->addField(Zend_Search_Lucene_Field::Text('lastname', $this->getLastname()));
</textarea></div>

Should be turned into:
<div><textarea name="code" class="php">

		$field = Zend_Search_Lucene_Field::Text('firstname', $this->getFirstname());
		$field->boost = 1.5;
		$doc->addField($field);
		$field = Zend_Search_Lucene_Field::Text('lastname', $this->getLastname());
		$field->boost = 1.5;
		$doc->addField($field);

</textarea></div>

This is pretty straight forward way to add weight (1.5 times the weight of a normal term) and you can customize it to the needs of your site.  
