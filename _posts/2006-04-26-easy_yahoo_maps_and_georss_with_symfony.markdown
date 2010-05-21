--- 
wordpress_id: 12
layout: post
title: Easy Yahoo! Maps and  GeoRSS with symfony
excerpt: |
  [rbu]: http://reviewsby.us/
  [ymap]: http://developer.yahoo.com/maps/index.html
  [gmap]: http://www.google.com/apis/maps/
  [ygeo]: http://developer.yahoo.com/maps/rest/V1/geocode.html
  [GeoRSS]: http://developer.yahoo.com/maps/georss/index.html
  [symfony]: http://www.symfony-project.com/
  
  [GeoRSS][GeoRSS] is an extension of RSS that incorporates geographic data (i.e. latitude/longitude coordinates).  This is useful for plotting any data that might need to be placed on a map.
  
  While building out the [reviewsby.us][rbu] map, I decided to use the [Yahoo! Maps API][ymap] versus the [Google Maps API][gmap] because I wanted to gain some familiarity with another API.
  
  It was worth trying [Yahoo!'s API][ymap].  First of all, [reviewsby.us][rbu] has addresses for restaurants and Yahoo! provides a simple [Geocoding REST][ygeo] service.  This made it easy for me to convert street addresses to latitude and longitude pairs (even though this wasn't required as we'll soon see).<sup id="fnr1">[1]</sup>  The real selling point of [Yahoo!][ymap] was the [GeoRSS] functionality.  I can extend an RSS feed (which [symfony] generates quite easily) to add latitude or longitude points (or even the street address), direct my [Yahoo! map][ymap] to the feed and voila, all the locations in that feed are now on the map, and when I click on them, the RSS item is displayed.  That cut down on a lot of development time.

---
[rbu]: http://reviewsby.us/
[ymap]: http://developer.yahoo.com/maps/index.html
[gmap]: http://www.google.com/apis/maps/
[ygeo]: http://developer.yahoo.com/maps/rest/V1/geocode.html
[GeoRSS]: http://developer.yahoo.com/maps/georss/index.html
[symfony]: http://www.symfony-project.com/

[GeoRSS][GeoRSS] is an extension of RSS that incorporates geographic data (i.e. latitude/longitude coordinates).  This is useful for plotting any data that might need to be placed on a map.

While building out the [reviewsby.us][rbu] map, I decided to use the [Yahoo! Maps API][ymap] versus the [Google Maps API][gmap] because I wanted to gain some familiarity with another API.

It was worth trying [Yahoo!'s API][ymap].  First of all, [reviewsby.us][rbu] has addresses for restaurants and Yahoo! provides a simple [Geocoding REST][ygeo] service.  This made it easy for me to convert street addresses to latitude and longitude pairs (even though this wasn't required as we'll soon see).<sup id="fnr1">[1]</sup>  The real selling point of [Yahoo!][ymap] was the [GeoRSS] functionality.  I can extend an RSS feed (which [symfony] generates quite easily) to add latitude or longitude points (or even the street address), direct my [Yahoo! map][ymap] to the feed and voila, all the locations in that feed are now on the map, and when I click on them, the RSS item is displayed.  That cut down on a lot of development time.
<!--break--><!--more-->
### [Yahoo's GeoRSS][GeoRSS]

The GeoRSS format that Yahoo uses is fairly simple to grasp if you know what an RSS feed looks like.  Here's a typical RSS feed:

	<?xml version="1.0" encoding="UTF-8" ?>
	<rss version="2.0">
		<channel>
			<title>Latest restaurants</title>
			<link>http://reviewsby.us/</link>
			<description>A list of the latest restaurants posted to my reviewsby.us</description>
			<language>en</language>
			<item>
				<title>Bubba Gump Shrimp Co. Restaurant and Market</title>
				<description>A *Forest Gump* themed restaurant.  Featuring a large selection of seafood items.</description>
				<link>http://reviewsby.us/restaurant/bubba-gump-shrimp-co-restaurant-and-market</link>
				<guid>25</guid>
				<pubDate>Sun, 23 Apr 2006 08:04:00 -0700</pubDate>
			</item>
			<item>
				<title>Famous Dave's Barbeque</title>
				<link>http://reviewsby.us/restaurant/famous-daves-barbeque</link>
				<guid>24</guid>
				<pubDate>Wed, 19 Apr 2006 19:58:08 -0700</pubDate>
			</item>
		</channel>
	</rss>	

The `<item />` in this example is a restaurant.  To turn this into a GeoRSS feed, we only need to change a few things:

	<?xml version="1.0" encoding="UTF-8" ?>
	<rss version="2.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
		<channel>
			<title>Latest restaurants' locations</title>
			<link>http://reviewsby.us/</link>
			<description>A geocoded list of the latest restaurants' locations posted to my reviewsby.us</description>
			<language>en</language>
			<item>
				<title>Bubba Gump Shrimp Co. Restaurant and Market (Mall of America (Bloomington, MN))</title>
				<link>http://reviewsby.us/restaurant/bubba-gump-shrimp-co-restaurant-and-market/location/mall-of-america</link>
				<guid>18</guid>
				<pubDate>Sun, 23 Apr 2006 08:08:19 -0700</pubDate>
				<geo:lat>44.85380173</geo:lat>
				<geo:long>-93.24040222</geo:long>
			</item>
		</channel>
	</rss>

We just added `xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#"` as an attribute to the `<rss/>` tag and added `<geo:lat />` and `<geo:long />` tags to any given item.  If you'd rather use address, city, state and zip fields instead of latitude and longitude coordinates, [the Yahoo! Georss page][georss] will tell you how.

### [symfony] and Geodata

I knew full well that [Yahoo! Maps][ymap] did not require me to have everything in latitude longitude coordinates, but I felt that from an efficiency standpoint, it made more sense for me to convert them once using a [geocoder][ygeo] and then Yahoo! wouldn't have to translate them later.  Also, I'm trying to think ahead when more than just Minneapolis restaurants become a part of the [reviewsby.us][rbu] site, I now have an easy way of determining distance between a user's home and a given restaurant.  Also, if Yahoo! Maps doesn't work out, I can use these coordinates in other mapping systems.

#### Extending the model

Models in [symfony] lend themselves to being easily extended.  So we can easily take a model for a location:

	<table name="location" phpName="Location">
		<column name="id" type="integer" primaryKey="true" autoIncrement="true"/>
		<column name="restaurant_id" type="integer" />
		<foreign-key foreignTable="restaurant">
			<reference local="restaurant_id" foreign="id"/>
		</foreign-key>
		<column name="stripped_title" type="varchar" size="255" />
		<column name="name" type="varchar" size="255" />
		<column name="address" type="varchar" size="255" />
		<column name="city" type="varchar" size="128" />
		<column name="state" type="varchar" size="16" />
		<column name="zip" type="varchar" size="9" />
		<column name="phone" type="varchar" size="16" />
		<column name="approved" type="boolean" />
		<column name="updated_at" type="TIMESTAMP" />
		<column name="created_at" type="TIMESTAMP" />
	</table>

and simply add two columns inside the `<table/>`:

	<column name="latitude" type="float" size="10" scale="8"/>
	<column name="longitude" type="float" size="10" scale="8"/>

Easy!  However, we don't want to have to set the latitude and longitude by hand each time we update a `Location`.  So first we write a function that takes an address and converts it to latitude/longitude.  I placed mine in a `myTools.class.php` in my `lib` folder:

	class myTools
	{
		public static function getLatLng($address, $city = null, $state = null, $zip = null)
		{
			$url = sfConfig::get('app_yahoo_geocode');
			$query['appid'] = sfConfig::get('app_yahoo_app_id');
			$query['street'] = $address;
			$query['city'] = $city;
			$query['state'] = $state;
			$query['zip'] = $zip;
			$query['output'] = 'php'; 
			$url .= '?' . http_build_query($query);	
			$response = @file_get_contents($url);
			if ($response) {
				$response = unserialize($response);
				return $response['ResultSet']['Result'];
			}
			return null;
		}
	}

Defined in my `app.yml` is `app_yahoo_geocode` and my `app_yahoo_app_id`.  `myTools::getLatLng()` queries the [Yahoo! REST][ygeo] service and returns the coordinates that Yahoo! delivers.  Note that the generated query string includes `output=php`.  Yahoo! supports serializing output as PHP instead of XML.  This can save a bundle of time over decoding XML.

So now let's look at our `Location.php` and override its inherited save function:

	public function save($con = null)
	{
		// save latitude and longitude
		$locdata = myTools::getLatLng($this->getAddress(), $this->getCity(), $this->getState(), $this->getZip());
		if ($locdata) 
		{
			$this->setLatitude($locdata['Latitude']);
			$this->setLongitude($locdata['Longitude']);
		}
		parent::save($con);
	}

If you stop here, you'll at least now know how to add latitude and longitude coordinates to an object automagically.

#### Producing a GeoRSS feed

[symfony] very easily will allow you to [generate an RSS feed][sf1].  How do we create a [GeoRSS] feed?  Just extend the `sfFeed` class.  Rather than instantiating a feed like this:

	$feed = sfFeed::newInstance('rss201rev2');

We do this:

	$feed = sfFeed::newInstance('geoRSS');	

And then create an [sfGeoRssFeed.class.php][spin1] and we're done.  We've created a GeoRSS feed fairly easily.  Comb through [sfGeoRssFeed.class.php][spin1] and compare it to the [sfRss201rev2Feed.class.php][sf2], you'll notice it's not that different and that it's fairly easy to extend the sfFeed plugin for [symfony].

[sf1]: http://www.symfony-project.com/content/book/page/syndication.html
[sf2]: http://www.symfony-project.com/trac/browser/trunk/lib/symfony/addon/sfFeed/sfRss201rev2Feed.class.php?rev=403
[spin1]: http://spindrop.us/files/symfony/sfGeoRssFeed.class.txt

### Adding your feed to a Yahoo! Map.	

[Adding a GeoRSS feed to Yahoo! maps][y1] is simple.  Before I embedded the RSS feed into my Yahoo! Map I was prepared to write an algorithm to cluster only on the points in my RSS feed, lucky for me (and you), [Yahoo! Maps][ymap] does this automatically.  One pitfall you might reach during development is that Yahoo! Maps must be able to reach your GeoRSS feed.  My development machine is my personal laptop, so this didn't work so well until I uploaded to a publically accessible staging server.  [The maps][rbu] worked like a charm as you can see.

[y1]: http://developer.yahoo.com/maps/ajax/index.html#ex6

### Conclusion

[Yahoo! Maps][ymap] are very powerful, and [symfony] is up to the task.  I hope you found this tutorial useful.  If you have any trouble, let me know.  I hope your [next meal][rbu] is a good one.

[1]: #fn1
<div class="footnotes">
	<ol>
		<li id="fn1">
			<p>
				Using Yahoo! Maps wasn't a requisite of using the Yahoo! Geocoder.  
				The datasets that were returned could have been used to populate a Google Map just as easily.
				<a href="#fnr1"  class="footnoteBackLink"  title="Jump back to footnote 1 in the text.">&#8617;</a>
			</p>
		</li>
	</ol>
</div>
