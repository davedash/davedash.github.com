# Read each file
# Find all related tags
# Insert them in YML
import os
import re
import sys

import yaml
import MySQLdb

POST_HEADER_SEP_RE = r'^---\s*$'

con = MySQLdb.Connect(db='tmp_spindrop', user='root')
cur = con.cursor()

POST_HEADER_SEP_RE = re.compile(POST_HEADER_SEP_RE, re.M)
files_done = 0
for filename in sys.argv[1:]:
    f = file(os.path.join(filename))
    files_done += 1
    if filename.endswith('.swp'):
        continue
    data = f.read()
    try:
        (garbage, meta, content,) = re.split(POST_HEADER_SEP_RE, data, 2)
    except:
        import pdb; pdb.set_trace()
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

    tags = "tags: [" + ", ".join([t[0] for t in tags]) + "]"
    f = file(os.path.join(filename), 'w')
    f.write("".join(['---', meta, tags, "\n---", content]))
    f.close()
    print "Done with %d: %d/%d" % (wpid, files_done, len(sys.argv)-1)
