--- 
wordpress_id: 165
layout: post
title: "py vs php: stemming"
wordpress_url: http://spindrop.us/2008/02/16/py-vs-php-stemming/
---
I've been porting some PHP to python during SuperHappyDevHouse and was amazed at how little code I needed to write since python makes list manipulation a breeze.

Today I was working on stemming (ala [Porter Stemming algorithm](http://tartarus.org/martin/PorterStemmer/)).  [reviewsby.us][rbu] uses stemming in the search engine to make queries:

Stemming turns `hello everybody how are you guy's` into a collection `'everybodi', 'gui', 'hello'`.  To produce this in php I do the following:

<!--more-->

<div><textarea name="code" class="php">
	public static function stemPhrase($phrase)
	{
		// remove apostrophe's and periods
		$phrase = strtolower(str_replace(array('\'', '.'), null, $phrase));
		
		// split into words
		$words = str_word_count($phrase, 1);

		// ignore stop words
		$words = array_diff($words, STOP_WORDS_ARRAY);

		// stem words
		$stemmed_words = array();

		foreach ($words as $word)
		{
			$stemmed_words[] = PorterStemmer::stem($word, true);
		}

		return $stemmed_words;
	}
</textarea></div>

With some magic python:

<div><textarea name="code" class="python">
def stem_phrase(phrase):
    words = phrase.lower().replace('.','').replace("'",'').split()

    # ignore stop words
    words = list(set(words)-set(STOP_WORDS))

    p = PorterStemmer()
    
    return [p.stem(word,0,len(word)-1) for word in words]

</textarea></div>

The magic here is list mappings.  Learning about them, they don't seem that great, but as soon as you start coding you stop using a lot of for loops.

I'm sure my PHP can be cleaned up and reduced as well, but its fun exploiting the magic of languages.

[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/
