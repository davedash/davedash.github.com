# Read each file
# Find all related tags
# Insert them in YML
import os
import re

import yaml
import MySQLdb

POST_HEADER_SEP_RE = r'^---$'
POSTS = '_posts'

files = os.listdir(POSTS)

con = MySQLdb.Connect(db='tmp_davedash', user='root')
cur = con.cursor()

POST_HEADER_SEP_RE = re.compile(POST_HEADER_SEP_RE, re.M)
files_done = 0
for filename in files:
    f = file(os.path.join(POSTS, filename))
    data = f.read()
    (meta, content,) = re.split(POST_HEADER_SEP_RE, data, 1)
    try:
        metadata = yaml.load(meta)
    except:
        pass

    if not metadata:
        continue

    if 'tags' in metadata:
        continue

    wpid = metadata['wordpress_id']
    cur.execute(("SELECT name FROM wp_terms WHERE term_id IN "
        "(SELECT term_taxonomy_id FROM wp_term_relationships "
        "WHERE object_id = %s)"), wpid)
    tags = cur.fetchall()

    if not tags:
        continue

    tags = "tags: " + " ".join([t[0] for t in tags])
    f = file(os.path.join(POSTS, filename), 'w')
    f.write("\n".join([meta, tags, '---', content]))
    f.close()
    files_done += 1
    print "Done with %d: %d/%d" % (wpid, files_done, len(files))
