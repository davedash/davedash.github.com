--- 
wordpress_id: 40
layout: post
title: Random Selections using Propel
wordpress_url: http://spindrop.us/2006/06/12/random-selections-using-propel/
---
[Propel][] is a handy way to deal with <acronym title="Object-Relational Mapping">ORM</acronym>.   Rather than figuring out the correct <acronym title="Structured Query Language">SQL</acronym> statement to select your elements you just use a -`Peer` object to select it.

The one drawback is there's no way of choosing an object at random.  You can select the first element of a result set, but not a random one without some changes to your -`Peer` class.

The quick and dirty fix that I did is to use custom <acronym title="Structured Query Language">SQL</acronym> to populate a [propel][] object.  It's a rather suitable approach for more complicated selects.  So here's how we randomly select things:

	$con = Propel::getConnection('propel');
    $sql = 'SELECT %s.* FROM %s ORDER BY RAND()';
	$sql = sprintf($sql,MyObjectPeer::TABLE_NAME,MyObjectPeer::TABLE_NAME);
    $stmt = $con->createStatement();
    $rs = $stmt->executeQuery($sql, ResultSet::FETCHMODE_NUM);
    $objects =  MyObjectPeer::populateObjects($rs);
	$object = $objects[0];

If you know you're going to only use one object, `SELECT %s.* FROM %s ORDER BY RAND() LIMIT 1` will work as well.

[propel]: http://propel.phpdb.org/
