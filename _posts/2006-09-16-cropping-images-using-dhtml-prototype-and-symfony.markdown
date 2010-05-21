--- 
wordpress_id: 64
layout: post
title: Cropping Images using DHTML (Prototype) and symfony
wordpress_url: http://spindrop.us/2006/09/16/cropping-images-using-dhtml-prototype-and-symfony/
---
[dd]: http://davedash.com/
[wf]: http://workface.com/
[d1]: http://demos.spindrop.us/image_cropper/
[digg]: http://digg.com/
[symfony]: http://symfony-project.com/
[php]: http://php.net/
[script.aculo.us]: http://script.aculo.us/
[prototype]: http://prototype.conio.net/
[gd2php]: http://www.php.net/manual/en/ref.image.php


[<img src="http://demos.spindrop.us/image_cropper/images/screenshot.png" style="float:left;margin-right:1em" />][d1]

**Note:** Like many of my tutorials, you don't *need* [symfony], just [PHP].  However, I develop in [symfony] and take advantage of the <acronym title="Model Viewer Controller">MVC</acronym>-support that it offers.

Years ago when I was working on a photo gallery for [davedash.com][dd] I got the art of making tumbnails down fairly well.  It was automated and didn't allow for specifying how the thumbnail should be made.  With dozens of photos (which was a lot back then), when would I find that kind of time.

Flashback to today, for [my company][wf]... we want users with avatars... but nothing too large.  Maybe a nice 80x80 picture.  Well the coolest <acronym title="User Interface">UI</acronym> I've seen was Apple's Address Book which let you use this slider mechanism to crop a fixed sized image from a larger image.

Here's a [demo][d1].

<!--more-->

### Overview

The front-end <acronym title="Graphical User Interface">GUI</acronym> is based on code from [digg] which is based on the look and feel (as near as I can tell) from Apple.

The <acronym title="Graphical User Interface">GUI</acronym> provides a clever visual way of telling the server how to chop the image.  The gist is this, sliding the image around and zooming in and out change a few form values that get passed to another script which uses this data to produce the image.

### Frontend: What would you like to crop?

In this tutorial, we're going to be cropping an 80x80 avatar from an uploaded image.  The front-end requires the correct mix of Javascript, <acronym title="Cascading Style Sheets">CSS</acronym>, <acronym title="HypterText Markup Languag">HTML</acronym> and images.  The Javascript sets up the initial placements of the image and the controls.  The <acronym title="Cascading Style Sheets">CSS</acronym> presents some necessary styling.  The images makeup some of the controls.  The <acronym title="HyperText Markup Language">HTML</acronym> glues everything together.

#### <acronym title="HyperText Markup Language">HTML</acronym>

Let's work on our <acronym title="HyperText Markup Language">HTML</acronym> first.  Since I used [symfony], I created a `crop` action for a `userpics` module.  So in our `cropSuccess.php` template:

	<div id="ava">
		<?php echo form_tag("userpics/crop") ?>
			<div id="ava_img">
				<div id="ava_overlay"></div>
				<div id="ava_drager"></div>
				<img src="<?php echo $image ?>" id="avatar" />
			</div>
			<div id="ava_slider"><div id="ava_handle"></div></div>
			<input type="hidden" id="ava_width" name="width" value="80" />
			<input type="hidden" id="ava_x" name="x" value="100" />
			<input type="hidden" id="ava_y" name="y" value="100" />
			<input type="hidden" id="ava_image" name="file" value="<?php echo $image ?>" />
			</div>
			<input type="submit" name="submit" id="ava_submit" value="Crop" style="width: auto; font-size: 105%; font-weight: bold; margin: 1em 0;" />
		</form>
	</div>

Right now a lot of this doesn't quite make sense.  If you attempt to render it, you will just see only the image.  As we add the corresponding <acronym title="Cascading Style Sheets">CSS</acronym> and images it will make some more sense.

#### <acronym title="Cascading Style Sheets">CSS</acronym> and corresponding images

We'll go through each style individually and explain what purpose it serves in terms of the <acronym title="Graphical User Interface">GUI</acronym>.

`#ava` is our container.

	#ava {
		border: 1px solid gray;
		 width: 200px;
	}

`#ava_img` is the area that contains our image.  Our window for editing this image 200x200 pixels.  If we drag out image out of bounds we just want the overflowing image to be clipped.  We also want our position to be relative so any child elements can be positioned absolutely with respect to `#ava_img`.

	#ava_img {
		width: 200px;
		height: 200px;
		overflow: hidden;
		position: relative;
	}

<div style="float:left;margin: 1em 1em 1em 0">
    <img src="http://demos.spindrop.us/image_cropper/images/overlay.png" alt="overlay" />
</div>

`#ava_overlay` is a window we use to see what exactly will be our avatar.  If it's in the small 80x80 window in the center of the image, then it's part of the avatar.  If it's in the fuzzy region, then it's getting cropped out.  This overlay of course needs to be positioned absolutely.

	#ava_overlay {
		width: 200px;
		height: 200px;
		position: absolute;
		top: 0px;
		left: 0px;
		background: url('/images/overlay.png');
		z-index: 50;
	}

`#ava_drager` is probably the least intuitive element (Heck, I'm not even sure if I've even got it right).  In [our demo][d1] you're not actually dragging the image, because you can drag anywhere within the `#ava_img` container and move the image around.  You're using dragging an invisible handle.  It's a 400x400 pixel square that can be dragged all over the container and thusly move the image as needed.
	
	#ava_drager {
		width: 400px;
		height: 400px;
		position: absolute;
		z-index: 100;
		color: #fff;
		cursor: move;
	}

`#avatar` is our image, and since it will be moving all around the window, it requires absolute positioning.

	#avatar {
		position: absolute;
	}

<div style="float:left;margin: 1em 1em 1em 0">
    <img src="http://demos.spindrop.us/image_cropper/images/slider_back.png" alt="overlay" />
</div>
<div style="float:left;margin-left: 1em 1em 1em 0;">
    <img src="http://demos.spindrop.us/image_cropper/images/handle.png" alt="overlay" />
</div>

`#ava_slider` and `#ava_handle` are our slider components.  They should be self-explanatory.
  
	#ava_slider {
		width: 200px;
		height: 27px;
		background: #eee;
		position: relative;
		border-top: 1px solid gray;	
		background: url('/images/slider_back.png');
	}
	#ava_handle {
		width: 19px;
		height: 20px;
		background: blue;
		position: absolute;
		background: url('/images/handle.png');
	}


##### Internet Explorer

<acronym title="Portable Network Graphics">PNG</acronym> do not work so well in Internet Explorer, but there is a small trick, adding these components into a style sheet that only IE can read will make things work:

    #ava_overlay {
      background: none;
      filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='/images/ui/cropper/overlay.png', sizingMethod='crop');
    }
    
    #ava_handle {
      background: none;
      filter:progid:DXImageTransform.Microsoft.AlphaImageLoader(src='/images/ui/cropper/handle.png', sizingMethod='crop');
    }

#### The Javascript

The Javascript is actually not as complicated as you'd expect thanks to the wonder of [prototype].  This framework provides so much so easily.  You'll need to include [prototype.js][prototype] and [dom-drag.js](http://boring.youngpup.net/2001/domdrag/project).

So let's take a look.

	<script type="text/javascript" language="javascript" charset="utf-8">
	// <![CDATA[
	function setupAva() {
		if ($("avatar")) {
			var handle = $("ava_handle");
			var avatar = $("avatar");
			var drager = $("ava_drager");
			var slider = $("ava_slider");
			var ava_width = $("ava_width");
			var ava_x = $("ava_x");
			var ava_y = $("ava_y");
			// four numbers are minx, maxx, miny, maxy
			Drag.init(handle, null, 0, 134, 0, 0);
			Drag.init(drager, avatar, -100, 350, -100, 350);
			var start_w = avatar.width;
			var start_h = avatar.height;
			var ratio = (start_h / start_w);
			var new_h;
			var new_w;
			if (ratio > 1) {
				new_w = 80;
				new_h = (80*start_h)/start_w;
			} else {
				new_h = 80;
				new_w = (80*start_w)/start_h;
			}
			// these need to be set after we init
			avatar.style.top = '100px';
			avatar.style.left = '100px';
			avatar.style.width = new_w + 'px';
			avatar.style.height = new_h + 'px';
			avatar.style.margin = '-' + (new_h / 2) + 'px 0 0 -' + (new_w / 2) + 'px';
			handle.style.margin = '3px 0 0 20px';
			avatar.onDrag = function(x, y) {
				ava_x.value = x;
				ava_y.value = y;
			}
			handle.onDrag = function(x, y) {
				var n_width = (new_w + (x * 2));
				var n_height = (new_h + ((x * 2) * ratio));			
				avatar.style.width = n_width + 'px';
				avatar.style.height = n_height+ 'px';
				ava_width.value = n_width;	
				avatar.style.margin = '-' + (n_height / 2) + 'px 0 0 -' + (n_width / 2) + 'px';
			}
		}
	}
	Event.observe(window,'load',setupAva, false);
	// ]]>
	</script>

If this isn't exactly crystal clear, I can explain.  If you're new to [prototype], `$()` is the same as `doucment.getElementByID()` (at least for our purposes).

We need to initialize two draggable elements, one is our slider for zooming and the other is our avatar itself.  We initialize the draggers using `Drag.init()`.  We specify what to drag, if another element should be used as a handle and then the range of motion in xy coordinates.  In the second call we use that `#dragger` to move around the image in this manner.  

	Drag.init(handle, null, 0, 134, 0, 0);
	Drag.init(drager, avatar, -100, 350, -100, 350);

We want to initialize the the size and placement of the avatar.  We do that using maths.  First we want it in our 80x80 pixel box.  So it should be roughly 80x80.  I've set the math up so that the *smallest* side is 80 pixels (there's reasons for doing this the other way around).

		if (ratio > 1) {
			new_w = 80;
			new_h = (80*start_h)/start_w;
		} else {
			new_h = 80;
			new_w = (80*start_w)/start_h;
		}

We then place the avatar element.  We initialize it to be in the center of the screen (`top: 100px;left:100px`) and then nudge the image using margins.

		avatar.style.top = '100px';
		avatar.style.left = '100px';
		avatar.style.width = new_w + 'px';
		avatar.style.height = new_h + 'px';
		avatar.style.margin = '-' + (new_h / 2) + 'px 0 0 -' + (new_w / 2) + 'px';

We also use margins to place the handle.

		handle.style.margin = '3px 0 0 20px';

`#ava_x` and `#ava_y` tell us where the center of the avatar is.  So when the avatar is moved we need to set these again:

		avatar.onDrag = function(x, y) {
			ava_x.value = x;
			ava_y.value = y;
		}

That was easy.  Slighly more complicated is the zoomer function.  We are basically adjusting the width and the height proportionately based on roughly where the slider is.  Note that we're still using that `ratio` variable that we calculated earlier.  We basically take the new x-coordinate of the handle and allow our image to get just slightly larger than the `#ava_image` container.

		handle.onDrag = function(x, y) {
			var n_width = (new_w + (x * 2));
			var n_height = (new_h + ((x * 2) * ratio));			
			avatar.style.width = n_width + 'px';
			avatar.style.height = n_height+ 'px';
			ava_width.value = n_width;	
			avatar.style.margin = '-' + (n_height / 2) + 'px 0 0 -' + (n_width / 2) + 'px';
		}

We want to load initialize the slider right away when the page loads: `Event.observe(window,'load',setupAva, false);`

Not terribly hard or complicated.  Once these elements are all in place you have a working functioning slider.  It returns the x and y coordinates of the center of the image with respect to our 200x200 pixel `#ava_image`.  It also tells us the new width of our image.  We feed this information into a new script and out should pop a new image which matches *exactly* what we see in our <acronym title="Graphical User Interface">GUI</acronym>.

<!--nextpage-->

### Processing the crop

Initially I was frustrated with the data that was being sent.  I knew the center of the image in relation to this 200x200 pixel canvas and its width... but what could I do with that.  Well I could just recreate what I saw in the <acronym title="Graphical User Interface">GUI</acronym>.  I needed to create a 200x200 pixel image first, place my original avatar resized (and resampled) at the precise coordinates and *then* cut out the center most 80x80 pixels to become the final avatar image.

If you note in our template above for `cropSuccess.php` we submit our form back to the `crop` action.  Let's look at the action:

	public function executeCrop()
	{
		if ($this->getRequestParameter('file')&&$this->getRequestParameter('width')) {			// we are saving our cropped image
			// Load the original avatar into a GD image so we can manipulate it with GD
			$o_filename = $this->getRequestParameter('file');  // we'll use this to find the file on our system
			$o_filename = sfConfig::get('sf_root_dir').'/web' . $o_filename;
			$o_im = @imagecreatetruecolor(80, 80) or die("Cannot Initialize new GD image stream");
			$o_imagetype = exif_imagetype($o_filename); // is this gif/jpeg/png
		
			// appropriately create the GD image
			switch ($o_imagetype) {
				case 1: // gif
					$o_im = imagecreatefromgif($o_filename);
					break;
				case 2: // jpeg
					$o_im = imagecreatefromjpeg($o_filename);	
					break;
				case 3: // png
					$o_im = imagecreatefrompng($o_filename);
					break;
			}
			
			// Let's create our canvas
			$im = @imagecreatetruecolor(200, 200) or die("Cannot Initialize new GD image stream");
			imagecolortransparent ( $im, 127 ); // set the transparency color to 127
			imagefilledrectangle( $im, 0, 0, 200, 200, 127 ); // fill the canvas with a transparent rectangle
		
			// let's get the new dimension for our image
		
			$new_width = $this->getRequestParameter('width');
			$o_width = imageSX($o_im);
			$o_height = imageSY($o_im);
			
			$new_height = $o_height/$o_width * $new_width;
		
			// we place the image at the xy coordinate and then shift it so that the image is now centered at the xy coordinate
			$x = $this->getRequestParameter('x') - $new_width/2;
			$y = $this->getRequestParameter('y') - $new_height/2;
			
			// copy the original image resized and resampled onto the canvas
			imagecopyresampled($im,$o_im,$x,$y,0,0,$new_width,$new_height,$o_width,$o_height); 
			imagedestroy($o_im);
			
			// $final will be our final image, we will chop $im and take out the 80x80 center
			$final = @imagecreatetruecolor(80, 80) or die("Cannot Initialize new GD image stream");
			imagecolortransparent ( $final, 127 ); // maintain transparency
		
			//copy the center of our original image and store it here
			imagecopyresampled ( $final, $im, 0, 0, 60, 60, 80, 80, 80, 80 );
			imagedestroy($im);
		
			//save our new user pic
			$p = new Userpic();
			$p->setUser($this->getUser()->getUser());
			$p->setGD2($final);
			$p->save();
			imagedestroy($final);
			$this->userpic = $p;
			return "Finished";
		}
	
	
		$this->getResponse()->addJavascript("dom-drag");
		$this->getResponse()->addJavascript('/sf/js/prototype/prototype');
		$this->getResponse()->addJavascript('/sf/js/prototype/effects');
		$this->image = '/images/userpics/originals/' . $this->getRequestParameter('file');
	}

It's doing exactly what the paragraph above explains when the image dimensions are given.  The code is well commented so it should be easy enough to follow.

[GD image functions in PHP][gd2php] are fairly robust and can help you do a lot of tricks with image data.  Note the code to save the image, we'll cover it in detail soon.


### The Model

	$p = new Userpic();
	$p->setUser($this->getUser()->getUser());
	$p->setGD2($final);
	$p->save();

First some clarification the second line.  `myUser::getUser()` gets the `User` object associated with the currently logged in user.  The third line, however, is where the magic happens.  Before we look at it, let's have a quick look at our model:

	userpic:
     _attributes: { phpName: Userpic }
     id:
     user_id:
	 image: blob
     thumb: blob
     created_at:
     updated_at:

We have an `image` attribute and a `thumb` property to our `Userpic` object.  This is where we store <acronym title="Portable Network Graphics">PNG</acronym> versions of each icon and their 16x16 thumbnails respectively.  We do this in `Userpic::setGD2()`:

	public function setGD2($gd2_image)
	{
		//convert to PNG
		ob_start();
		imagepng($gd2_image);
		$png = ob_get_clean();
		//save 16x16
		$gd2_tn = @imagecreatetruecolor(16, 16) or die("Cannot Initialize new GD image stream");
		imagealphablending( $gd2_tn, true );
		imagecolortransparent ( $gd2_tn, 127 );
		
		imagecopyresampled ( $gd2_tn, $gd2_image, 0, 0, 0, 0, 16, 16, 80, 80 );
		ob_start();
		imagepng($gd2_tn);
		$tn = ob_get_clean();
		
		$this->setImage($png);
		$this->setThumb($tn);
	}

We capture the output of the full size <acronym title="Portable Network Graphics">PNG</acronym>, then we scale it again and capture the output of the thumbnail and set them.

### Conclusion

When it comes to web apps, having a relatively simple <acronym title="Graphical User Interface">GUI</acronym> for people to resize images can go a long way in terms of adoption rate of avatars and custom user pictures by non technical users.

Enjoy, and if you found this useful (or better implemented it) let me know.

