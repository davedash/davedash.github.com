---
layout: tutorial
title: Simple Exploration of Python with IPython
---
This tutorial assumes you have a properly set
up python virtual environment.
Please don't be scared off if you don't, just read this [quick tutorial][v].
You'll thank me later.

## tl;dr

    pip install ipython
    easy_install readline  # if you are on a Mac
    ipython

    In [1]: # Enter Python Here

If you don't know what a certain method, object or value is, use the `?`, if
you need more details use `??`.
If you want to know what you can do to an object hit tab (see `In [4]` below):

    In [1]: from collections import defaultdict

    In [2]: defaultdict?
    Type:       type
    String Form:<type 'collections.defaultdict'>
    File:       /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/collections.py
    Docstring:
    defaultdict(default_factory) --> dict with default factory

    The default factory is called without arguments to produce
    a new value when a key is not present, in __getitem__ only.
    A defaultdict compares equal to a dict with the same items.


    In [3]: a = defaultdict()

    In [4]: a.<tab>
    a.clear            a.fromkeys         a.items            a.itervalues       a.popitem
    a.values           a.viewvalues       a.copy             a.get              a.iteritems
    a.keys             a.setdefault       a.viewitems        a.default_factory  a.has_key
    a.iterkeys         a.pop              a.update           a.viewkeys

For details keep reading.

## Poking around Python

If you are teaching yourself python from a place like [Code Academy][c], you
will learn basics about Python, but you might not understand the limits of the
language.  You might write a function that expects a dict, but not know why it
won't work when you feed it a list.  Things like
[`pdb` can be useful for this][p], or even the python shell.  Sometimes,
however, you want the spontaneity of the python shell (you don't even need to
save a program to a text file), but you do want the ability to inspect how
things work that `pdb` can give you.

`IPython` can fill that role.  It will let you type out arbitrary python as
well as explore how it works.  It also has some niceties like being able to hit
the up and down arrow or even Ctrl-R to cycle through your command history, a
way to edit larger pieces of code and a whole lot more.

## Installation

I suggest using a [`virtualenv`][v] to start.  You may want to use an existing
one or create a new one.  This tutorial will create a temporary one, in which
we can explore:

    mktmpenv
    pip install ipython
    easy_install readline

Now you can run `ipython` feel free to type in as much python as you want, you
shouldn't be able to do too much damage, unless that's your goal.

## How do things tick?

I wrote a library a long time ago called [textcluster][t]. It creates a
`Corpus` of `Document`s and groups them together by textual similarity.  Let's
install it:

    pip install textcluster

Let's say we know this provides a `textcluster` package, but we don't know much
else.  Let's explore:

    In [1]: import textcluster

    In [2]: textcluster.<tab>
    textcluster.Corpus   textcluster.cluster  textcluster.search

    In [2]: texcluster.Corpus?
    Object `texcluster.Corpus` not found.

    In [3]: from textcluster import Corpus

    In [4]: Corpus?

    In [5]: c = Corpus()

    In [6]: c.<tab>
    c.add           c.create_index  c.index         c.stopwords
    c.cluster       c.docs          c.similarity    c.words

    In [6]: c.add?
    Type:       instancemethod
    String Form:<bound method Corpus.add of <textcluster.cluster.Corpus instance at 0x100fb3fc8>>
    File:       /Users/davedash/.virtualenvs/e5c336e9c163d64b/lib/python2.7/site-packages/textcluster/cluster.py
    Definition: c.add(self, document, key=None, str=None)
    Docstring:  Adds a document to the corpus.

Within a few minutes, we've discovered that `textcluster` provides a `Corpus`
class.  We've learned that a `Corpus` instance has a method called `add` and
that we can add some sort of `document` to the `Corpus` this way.

If we're still confused and want to snoop around, you can try this:

    In [7]: c.add??
    Type:       instancemethod
    String Form:<bound method Corpus.add of <textcluster.cluster.Corpus instance at 0x100fb3fc8>>
    File:       /Users/davedash/.virtualenvs/e5c336e9c163d64b/lib/python2.7/site-packages/textcluster/cluster.py
    Definition: c.add(self, document, key=None, str=None)
    Source:
        def add(self, document, key=None, str=None):
            """Adds a document to the corpus."""
            if not key:
                try:
                    key = document.id
                except AttributeError:
                    key = document

            if not str:
                str = unicode(document)

            doc = Document(self, document, str=str, stopwords=self.stopwords)

            if len(doc.tf) < MIN_DOCUMENT_LENGTH:
                return

            for k in doc.tf.keys():
                if k in self.words:
                    self.words[k] += 1

            self.docs[key] = doc

Two `??` will output metadata about an object as well as any source code if it
was written in python.  Now we know that for `document` it needs to be
something that has an `id` or apparently it can just be a string of text.  The
`author` of this package could have done a better job with his documentation.

## Together with pdb.

If you use [`pdb`][p] to debug, you can drop into `iPython` by typing `i` if
you add this to your `~/.pdbrc`:

    alias i from IPython.terminal.embed import InteractiveShellEmbed as s; s()()

Now you can have the full power of an interactive shell while you debug.

## An Extended Example

This is just the tip of the iceberg of what you can do with `IPython`.
I use this tool almost daily as software engineer on the Pinterest Technical Operations team.

I often use it to automate one-off tasks.  Or even provide the template for scripts
(as you'll see at the end of this).

I had the task of downloading a file from Amazon S3 onto a server, using the [`boto`][b] library.
I had already done a lot of work with `boto` in the `deploy-tools` that I wrote, so I switched into
that project and opened `iPython`:

    In [3]: import deploy.s3

    In [4]: s3 = deploy.s3.S3()

    In [5]: s3.get_file('')
    Out[5]: <Key: my-s3-bucket,>

    In [6]: k = s3.get_file('')

    In [7]: k.<tab>
    k.BufferSize                  k.content_type
    k.get_file                    k.metadata                    k.set_canned_acl
    k.DefaultContentType          k.copy
    k.get_md5_from_hexdigest      k.mode                        k.set_contents_from_file
    k.RestoreBody                 k.delete
    k.get_metadata                k.name                        k.set_contents_from_filename
    ...trimmed...

I wasn't really finding what I wanted.  So I tried some other things, by
hitting `s3.<tab>` I discovered `s3.bucket`... that looked promising.  I wanted
to get every member of a bucket:

    In [7]: s3.bucket.
    s3.bucket.BucketPaymentBody                   s3.bucket.generate_url
    s3.bucket.list
    s3.bucket.LoggingGroup                        s3.bucket.get_acl
    s3.bucket.list_grants
    s3.bucket.MFADeleteRE                         s3.bucket.get_all_keys
    s3.bucket.list_multipart_uploads
    s3.bucket.VersionRE                           s3.bucket.get_all_multipart_uploads
    s3.bucket.list_versions
    s3.bucket.VersioningBody                      s3.bucket.get_all_versions
    s3.bucket.lookup
    s3.bucket.add_email_grant                     s3.bucket.get_cors
    s3.bucket.make_public


    In [7]: s3.bucket.list()
    Out[7]: <boto.s3.bucketlistresultset.BucketListResultSet instance at 0x2070368>

It's okay to make mistakes:

    In [8]: l = s3.bucket.list()

    In [9]: l.next()
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-9-49b5b93d8a22> in <module>()
    ----> 1 l.next()

    AttributeError: BucketListResultSet instance has no attribute 'next'


    In [10]: l[0]
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-10-44e56f8a6e9f> in <module>()
    ----> 1 l[0]

    AttributeError: BucketListResultSet instance has no attribute '__getitem__'

    In [11]: l.
    l.bucket     l.delimiter  l.headers    l.marker     l.prefix

    In [11]: print l
    <boto.s3.bucketlistresultset.BucketListResultSet instance at 0x2070170>


Eventually I tried something else that I had seen:

    In [12]: s3.bucket.get_all_keys
    Out[12]: <bound method Bucket.get_all_keys of <Bucket: my-s3-bucket>>

    In [13]: s3.bucket.get_all_keys()
    Out[13]:
    [<Key: my-s3-bucket,optimus/prime-0071eeb.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-0200bcd.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-035cb2c.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-06ba0eb.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-0910f70.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-0a9e431.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-0b9e35c.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-0bdce86.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-0c99123.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-0f96dfe.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-106df7f.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-14177f2.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-1450d38.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-1704896.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-1848e93.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-1995802.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-1b36734.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-1cf69e5.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-1d710e1.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-1d71e08.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-21039f0.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-26f412c.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-2753ed2.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-28f6a27.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-29f8ea0.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-29fe769.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-2a3fcb8.tar.gz>,
     <Key: my-s3-bucket,optimus/prime-2c2a9ab.tar.gz>]

Bingo!  I was able to list the files in the bucket, now I just had to download it:

    In [15]: s3.get
    s3.get_builds       s3.get_file         s3.get_last_builds

    In [15]: s3.get_file('optimus/prime-86b84f1.tar.gz')
    Out[15]: <Key: my-s3-bucket,optimus/prime-86b84f1.tar.gz>

    In [16]: s3.get_file('optimus/prime-86b84f1.tar.gz').get_contents_to_file('/tmp/foo')
    ---------------------------------------------------------------------------
    AttributeError                            Traceback (most recent call last)
    <ipython-input-16-fdb33fb41eb6> in <module>()
    ----> 1 s3.get_file('optimus/prime-86b84f1.tar.gz').get_contents_to_file('/tmp/foo')

    /usr/local/lib/python2.7/dist-packages/boto/s3/key.pyc in
    get_contents_to_file(self, fp, headers, cb, num_cb, torrent, version_id,
    res_download_handler, response_headers)
       1561                 self.get_file(fp, headers, cb, num_cb, torrent=torrent,
       1562                               version_id=version_id,
    -> 1563                               response_headers=response_headers)
       1564
       1565     def get_contents_to_filename(self, filename, headers=None,

    /usr/local/lib/python2.7/dist-packages/boto/s3/key.pyc in
    get_file(self, fp, headers, cb, num_cb, torrent, version_id, override_num_retries, response_headers)
       1401                                 response_headers=response_headers,
       1402                                 hash_algs=None,
    -> 1403                                 query_args=None)
       1404
       1405     def _get_file_internal(self, fp, headers=None, cb=None, num_cb=10,
    import deploy.s3

    /usr/local/lib/python2.7/dist-packages/boto/s3/key.pyc in
    _get_file_internal(self, fp, headers, cb, num_cb, torrent, version_id, override_num_retries, response_headers, hash_algs, query_args)
       1455         try:
       1456             for bytes in self:
    -> 1457                 fp.write(bytes)
       1458                 data_len += len(bytes)
       1459                 for alg in digesters:

    AttributeError: 'str' object has no attribute 'write'

    In [17]: s3.get_file('optimus/prime-86b84f1.tar.gz').get_contents_to_filename('/tmp/foo')

I was able to save the file to `/tmp/foo`.  Perfect.  I had to copy this to a file so I could run
this script in multiple places.  `history` is a useful command that helped:

    In [18]: history
    import boto
    import boto.s3
    import deploy.s3
    s3 = deploy.s3.S3()
    s3.get_file('')
    k = s3.get_file('')
    s3.bucket.list()
    l = s3.bucket.list()
    l.next()
    l[0]
    print l
    s3.bucket.get_all_keys
    s3.bucket.get_all_keys()
    s3.bucket.get_all_keys()
    s3.get_file('optimus/prime-86b84f1.tar.gz')
    s3.get_file('optimus/prime-86b84f1.tar.gz').get_contents_to_file('/tmp/foo')
    s3.get_file('optimus/prime-86b84f1.tar.gz').get_contents_to_filename('/tmp/foo')

I was able to remove a few lines and create this simple 4 liner.

    import deploy.s3
    s3 = deploy.s3.S3()
    s3.get_file('optimus/prime-86b84f1.tar.gz')
    s3.get_file('optimus/prime-86b84f1.tar.gz').get_contents_to_filename('/tmp/foo')

I was free to explore the `boto` API without having to re-run a script over and
over again.  This made the process of coding a lot less daunting, and a lot
quicker.  I hope this helps you become a more efficient developer too.

[v]: /tutorial/virtualenv/
[i]: http://ipython.org/
[c]: http://www.codecademy.com/
[p]: /tutorial/pdb-the-python-debugger/
[t]: https://github.com/davedash/textcluster/
[b]: http://boto.readthedocs.org/en/latest/
