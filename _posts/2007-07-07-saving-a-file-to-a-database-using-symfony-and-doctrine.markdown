---
wordpress_id: 105
layout: post
title: Saving a file to a database using symfony and doctrine
wordpress_url: http://spindrop.us/2007/07/07/saving-a-file-to-a-database-using-symfony-and-doctrine/
site: spindrop
---
[tags]symfony, doctrine, database, uploads, wordpress, fixme[/tags]

I like to save content uploaded by website visitors to a database versus the file system.  It makes it easy having the data all in one spot.

I tend to overcomplicate this process, so I wanted to write down the important steps:

1. In the template set `multipart=true` for the form.  If you're using symfony helpers you can do this via:

        form_tag('@action', 'multipart=true')

2. Extract the binary data you want to store in the database in your action:

		$path = $this->getRequest()->getFilePath('my_file');
		$size = $this->getRequest()->getFileSize('my_file');
		$type = $this->getRequest()->getFileType('my_file');    
		$data = fread(f_open($path, "r"), $size);
		
		$myObject              = new MyObject();
		$myObject['file_data'] = $data;
		$myObject['file_size'] = $size;
		$myObject['mime_type'] = $type;
		$myObject->save();
    
**Note**: Wordpress is garbage so f_open should not have an underscore... what to do...

At least that's how we role with Doctrine.  Note, Doctrine syntax is changing, and this may not be the most efficient way to create a new `Doctrine Record` in your application.

