# Read each file
# Find all related tags
# Insert them in YML
import os
import re
import sys

import yaml
import MySQLdb

POST_HEADER_SEP_RE = r'^---\s*$'

con = MySQLdb.Connect(db='tmp_davedash', user='root')
cur = con.cursor()

POST_HEADER_SEP_RE = re.compile(POST_HEADER_SEP_RE, re.M)
files_done = 0
for filename in sys.argv[1:]:
    metadata = None
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

    sql = """
    SELECT
        name
    FROM wp_terms t
    LEFT JOIN wp_term_taxonomy tt ON (t.term_id = tt.term_id)
    LEFT JOIN wp_term_relationships tr
        ON (tr.term_taxonomy_id=tt.term_taxonomy_id)
    WHERE tr.object_id=%s
    """
    cur.execute(sql, wpid)
    tags = cur.fetchall()

    if not tags:
        continue

    tags = "tags: [" + ", ".join([t[0] for t in tags]) + "]"
    f = file(os.path.join(filename), 'w')
    f.write("".join(['---', meta, tags, "\n---", content]))
    f.close()
    print "Done with %d: %d/%d" % (wpid, files_done, len(sys.argv)-1)
