import os
import re

import yaml

POST_HEADER_SEP_RE = r'^---$'
POST_HEADER_SEP_RE = re.compile(POST_HEADER_SEP_RE, re.M)

POSTS = '_posts'

files = os.listdir(POSTS)

for filename in files:
    f = file(os.path.join(POSTS, filename))
    data = f.read()
    (meta, content,) = re.split(POST_HEADER_SEP_RE, data, 1)
    metadata = yaml.load(meta)

    if not metadata:
        continue

    if 'site' in metadata:
        continue

    wpurl = metadata.get('wordpress_url')

    f = file(os.path.join(POSTS, filename), 'w')
    f.write("\n".join(('---', meta,)))
    f.write("\n")
    if wpurl.startswith('http://spindrop.us/'):
        f.write("site: spindrop\n")

    f.write("\n".join(('---', content)))
    f.close()
    print "Done with %s" % metadata.get('title')
