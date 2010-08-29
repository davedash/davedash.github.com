layout: post
title: Installing a PHP that can do symfony+doctrine on Dreamhost
site: spindrop
tags: [symfony, symfony, php, doctrine, syfony, dreamhost]
---
Lately I've been experimenting with Doctrine on a few projects.  It does have some requirements, including the PDO layer of PHP 5.2.  Things didn't work right off the bat on Dreamhost (which I still use for non-critical things), so I opted to build my own php.


<!--more-->


This is based on the numerous `installphp` scripts floating around:

    #!/bin/sh

    # Script updated 2006-12-25 by Carl McDade (hiveminds.co.uk) to allow memory limit and freetype
    # Save the code to a file as *.sh

    # The domain in which to install the PHP CGI script.
    export DOMAIN="example.com"

    # Where do you want all this stuff built? I'd recommend picking a local
    # filesystem.
    # ***Don't pick a directory that already exists!***  We clean up after
    # ourselves at the end!
    SRCDIR=${HOME}/source

    # And where should it be installed?
    INSTALLDIR=${HOME}/php5

    # Set DISTDIR to somewhere persistent, if you plan to muck around with this
    # script and run it several times!
    DISTDIR=${HOME}/dist

    # Pre-download clean up!!!!
    #rm -fr $SRCDIR # $DISTDIR

    # Update version information here.
    PHP5="php-5.2.2"
    LIBICONV="libiconv-1.11"
    LIBMCRYPT="libmcrypt-2.5.7"
    LIBXML2="libxml2-2.6.27"
    LIBXSLT="libxslt-1.1.18"
    MHASH="mhash-0.9.7.1"
    ZLIB="zlib-1.2.3"
    CURL="curl-7.14.0"
    LIBIDN="libidn-0.6.8"
    CCLIENT="imap-2004g"
    CCLIENT_DIR="imap-2004g" # Another pest!
    FREETYPE="freetype-2.2.1"


    PHPFEATURES="--prefix=${INSTALLDIR}
      --enable-fastcgi \
      --with-mysql=/usr \
      --enable-calendar \
      --enable-force-cgi-redirect \
      --with-config-file-path=${INSTALLDIR}/etc/php5/${DOMAIN} \
      --enable-trans-sid \
      --with-gd \
      --with-xml \
      --with-ttf=/usr \
      --with-freetype-dir=/usr \
      --enable-exif \
      --with-jpeg-dir=/usr \
      --with-png-dir=/usr \
      --with-zlib-dir=/usr \
      --with-pdo-mysql \
      --enable-ftp \
      --with-curl=${INSTALLDIR} \
      --enable-mbstring \
      --with-mcrypt=${INSTALLDIR} \
      --with-mysqli \
      --with-gettext \
      "

    #  
    # # What PHP features do you want enabled?
    # PHPFEATURES="--prefix=${INSTALLDIR} \
    #  --with-config-file-path=${INSTALLDIR}/etc/php5/${DOMAIN} \
    #  --enable-fastcgi \
    #  --enable-force-cgi-redirect \
    #  --with-xml \
    #  --with-libxml-dir=${INSTALLDIR} \
    #  --with-freetype-dir=${INSTALLDIR} \
    #  --enable-soap \
    #  --with-mhash=${INSTALLDIR} \
    #  --with-mcrypt=${INSTALLDIR} \
    #  --with-zlib-dir=${INSTALLDIR} \
    #  --with-jpeg-dir=/usr \
    #  --with-png-dir=/usr \
    #  --with-gd \
    #  --enable-gd-native-ttf \
    #  --enable-memory-limit
    #  --enable-ftp \
    #  --with-exif \
    #  --enable-sockets \
    #  --enable-wddx \
    #  --with-iconv=${INSTALLDIR} \
    #  --enable-calendar \
    #  --with-curl=${INSTALLDIR} \
    #  --enable-mbstring \
    #  --enable-mbregex \
    #  --with-mysql=/usr \
    #  --with-mysqli \
    #  --with-gettext"
     # --with-imap=${INSTALLDIR} \
     # --with-imap-ssl=/usr"

    # ---- end of user-editable bits. Hopefully! ----

    # Push the install dir's bin directory into the path
    export PATH=${INSTALLDIR}/bin:$PATH

    #setup directories
    mkdir -p ${SRCDIR}
    mkdir -p ${INSTALLDIR}
    mkdir -p ${DISTDIR}
    cd ${DISTDIR}

    # Get all the required packages
    wget -c http://us3.php.net/distributions/${PHP5}.tar.gz
    wget -c http://mirrors.usc.edu/pub/gnu/libiconv/${LIBICONV}.tar.gz
    wget -c http://easynews.dl.sourceforge.net/sourceforge/mcrypt/libmcrypt-2.5.7.tar.gz
    wget -c ftp://xmlsoft.org/libxml2/${LIBXML2}.tar.gz
    wget -c ftp://xmlsoft.org/libxml2/${LIBXSLT}.tar.gz
    wget -c http://superb-west.dl.sourceforge.net/sourceforge/mhash/${MHASH}.tar.gz
    wget -c http://www.zlib.net/${ZLIB}.tar.gz
    wget -c http://curl.haxx.se/download/${CURL}.tar.gz
    wget -c http://kent.dl.sourceforge.net/sourceforge/freetype/${FREETYPE}.tar.gz
    wget -c ftp://alpha.gnu.org/pub/gnu/libidn/${LIBIDN}.tar.gz
    wget -c ftp://ftp.cac.washington.edu/imap/old/${CCLIENT}.tar.Z

    # Abort on any errors
    set -e

    echo ---------- Unpacking downloaded archives. This process may take several minutes! ----------

    cd ${SRCDIR}
    # Unpack them all
    echo Extracting ${PHP5}...
    tar xzf ${DISTDIR}/${PHP5}.tar.gz
    echo Done.
    echo Extracting ${LIBICONV}...
    tar xzf ${DISTDIR}/${LIBICONV}.tar.gz
    echo Done.
    echo Extracting ${LIBMCRYPT}...
    tar xzf ${DISTDIR}/${LIBMCRYPT}.tar.gz
    echo Done.
    echo Extracting ${LIBXML2}...
    tar xzf ${DISTDIR}/${LIBXML2}.tar.gz
    echo Done.
    echo Extracting ${LIBXSLT}...
    tar xzf ${DISTDIR}/${LIBXSLT}.tar.gz
    echo Done.
    echo Extracting ${MHASH}...
    tar xzf ${DISTDIR}/${MHASH}.tar.gz
    echo Done.
    echo Extracting ${ZLIB}...
    tar xzf ${DISTDIR}/${ZLIB}.tar.gz
    echo Done.
    echo Extracting ${CURL}...
    tar xzf ${DISTDIR}/${CURL}.tar.gz
    echo Done.
    echo Extracting ${LIBIDN}...
    tar xzf ${DISTDIR}/${LIBIDN}.tar.gz
    echo Done.
    echo Extracting ${CCLIENT}...
    uncompress -cd ${DISTDIR}/${CCLIENT}.tar.Z |tar x
    echo Done.
    echo Extracting ${FREETYPE}...
    tar xzf ${DISTDIR}/${FREETYPE}.tar.gz
    echo Done.

    # Build them in the required order to satisfy dependencies.

    #libiconv
    cd ${SRCDIR}/${LIBICONV}
    ./configure --enable-extra-encodings --prefix=${INSTALLDIR}
    # make clean
    make
    make install

    #libxml2
    cd ${SRCDIR}/${LIBXML2}
    ./configure --with-iconv=${INSTALLDIR} --prefix=${INSTALLDIR}
    # make clean
    make
    make install

    #libxslt
    cd ${SRCDIR}/${LIBXSLT}
    ./configure --prefix=${INSTALLDIR} \
     --with-libxml-prefix=${INSTALLDIR} \
     --with-libxml-include-prefix=${INSTALLDIR}/include/ \
     --with-libxml-libs-prefix=${INSTALLDIR}/lib/
    # make clean
    make
    make install

    #zlib
    cd ${SRCDIR}/${ZLIB}
    ./configure --shared --prefix=${INSTALLDIR}
    # make clean
    make
    make install

    #libmcrypt
    cd ${SRCDIR}/${LIBMCRYPT}
    ./configure --disable-posix-threads --prefix=${INSTALLDIR}
    # make clean
    make
    make install

    #libmcrypt lltdl issue!!
    cd  ${SRCDIR}/${LIBMCRYPT}/libltdl
    ./configure --prefix=${INSTALLDIR} --enable-ltdl-install
    # make clean
    make
    make install

    #mhash
    cd ${SRCDIR}/${MHASH}
    ./configure --prefix=${INSTALLDIR}
    # make clean
    make
    make install

    #freetype
    cd ${SRCDIR}/${FREETYPE}
    ./configure --prefix=${INSTALLDIR}
    # make clean
    make
    make install

    #libidn
    cd ${SRCDIR}/${LIBIDN}
    ./configure --with-iconv-prefix=${INSTALLDIR} --prefix=${INSTALLDIR}
    # make clean
    make
    make install

    #cURL
    cd ${SRCDIR}/${CURL}
    ./configure --with-ssl=${INSTALLDIR} --with-zlib=${INSTALLDIR} \
      --with-libidn=${INSTALLDIR} --enable-ipv6 --enable-cookies \
      --enable-crypto-auth --prefix=${INSTALLDIR}
    # make clean
    make
    make install

    # # c-client
    # cd ${SRCDIR}/${CCLIENT_DIR}
    # make ldb
    # # Install targets are for wusses!
    # cp c-client/c-client.a ${INSTALLDIR}/lib/libc-client.a
    # cp c-client/*.h ${INSTALLDIR}/include

    #PHP 5
    cd ${SRCDIR}/${PHP5}
    ./configure ${PHPFEATURES}
    #make clean
    make
    make install

    #copy config file
    mkdir -p ${INSTALLDIR}/etc/php5/${DOMAIN}
    cp ${SRCDIR}/${PHP5}/php.ini-dist ${INSTALLDIR}/etc/php5/${DOMAIN}/php.ini

    #copy PHP CGI
    mkdir -p ${HOME}/${DOMAIN}/web/cgi-bin
    chmod 0755 ${HOME}/${DOMAIN}/web/cgi-bin
    cp ${INSTALLDIR}/bin/php ${HOME}/${DOMAIN}/web/cgi-bin/php.cgi
    #rm -fr $SRCDIR $DISTDIR
    echo ---------- INSTALL COMPLETE! ----------

Now to your `.htaccess` add:

	AddHandler phpFive .php
	Action phpFive /cgi-bin/php.cgi

And you are set.  I'm not a big "compiling guy."  So if there are issues with this please let me know and give me some good explanations.

[tags]dreamhost, syfony, doctrine, php[/tags]
