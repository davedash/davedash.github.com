import os
import re
import sys

import yaml

POST_HEADER_SEP_RE = r'^---[ ]*$'
POST_HEADER_SEP_RE = re.compile(POST_HEADER_SEP_RE, re.M)


for filename in sys.argv[1:]:
    f = file(os.path.join(filename))
    data = f.read()

    try:
        (crap, meta, content,) = re.split(POST_HEADER_SEP_RE, data, 2)
    except:
        print filename
        raise

    metadata = yaml.load(meta)

    if not metadata:
        continue

    if 'site' in metadata:
        continue

    wpurl = metadata.get('wordpress_url')

    if wpurl is None or not wpurl.startswith('http://spindrop.us/'):
        continue
    f = file(os.path.join(filename), 'w')
    f.write("".join(('---', meta, "site: spindrop\n", '---', content)))
    f.close()
    print "Done with %s" % metadata.get('title')
