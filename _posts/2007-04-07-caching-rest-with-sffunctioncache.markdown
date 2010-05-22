---
wordpress_id: 87
layout: post
title: Caching REST with sfFunctionCache
wordpress_url: http://spindrop.us/2007/04/07/caching-rest-with-sffunctioncache/
site: spindrop
tags: [reviewsby.us, programming, symfony, symfony, php, geocoding, sfFunctionCache, cache, Cache_Lite, REST, caching]
---
[tags]geocoding, caching, REST, symfony, Cache_Lite, php, cache, sfFunctionCache[/tags]

[ygc]: http://developer.yahoo.com/maps/rest/V1/geocode.html
[rbu]: http://reviewsby.us/
[symfony]: http://symfony-project.com/
[sf1]: http://www.symfony-project.com/book/trunk/18-Performance#Caching%20the%20Result%20of%20a%20Function%20Call

For [reviewsby.us][rbu] we do a lot of geocoding.  To facilitate we use [Yahoo! Geocoding API][ygc].  This helps us normalize data, obtain latitude and longitude, interpret location specific searches.

These <acronym title="REpresentational State Transfer">REST</acronym> queries happen a lot and will continue to happen, but this data that Yahoo! provides is fairly static.  We're basically querying a database of sorts.  So it makes sense that we should cache this data.

We'll demonstrate how to cache these queries using [symfony][]'s [`sfFunctionCache`][sf1] class. 








<!--more-->






I wrote a wrapper (I'll release it as a plugin if requested) for the [Geocoding API][ygc], the bulk of the work (the <acronym title="REpresentational State Transfer">REST</acronym> call) occurs in a function called `doQueryGIS`:

<div><textarea name="code" class="php">
		public static function doQueryGIS($location)
		{
			$url               = sfConfig::get('app_yahoo_geocode');

			$query             = array();
			$query['appid']    = sfConfig::get('app_yahoo_app_id');
			$query['location'] = $location;
			$query['output']   = 'php';

			$url .= '?' . http_build_query($query,null,'&');	
              $curl = curl_init($url);
			curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
			$response = curl_exe c($curl); 
              // note there should be no space between curl_exe and c($curl) 
              // wordpress is just dumb
		

			if ($response != 'Array') 
			{
				return unserialize($response);
			} 
			else 
			{
				throw new sfException('Yahoo! GeoCoder does not understand: "'. $location . "\"\n");
			}
			return false;	
			
			
		}

</textarea></div>

The call to this function is always wrapped with `queryGIS`:

<div><textarea name="code" class="php">
	  protected function queryGIS()
		{
			$function_cache_dir = sfConfig::get('sf_cache_dir').'/function';
			$cache = new sfFunctionCache($function_cache_dir);
			$this->rawData = $cache->call(array('YahooGeo','doQueryGIS'), $this->rawLocation);
			return $this->rawData;
			
		}
</textarea></div>

This wrapper creates a `sfFunctionCache` objet and calls the function and caches it for subsequent queries.

What this means is once Yahoo! teaches [reviewsby.us][rbu] that India is located at (25.42&deg;, 77.830002&deg;) and that the precision is 'country' we remember it in the future.

These features will be incorporated into future versions of [reviewsby.us][rbu].

