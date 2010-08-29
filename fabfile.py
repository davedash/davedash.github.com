import os

from fabric.api import local
import yaml

POSTS_DIR = '_posts'


def untagged():
    for filename in os.listdir(POSTS_DIR):
        if not filename.endswith('.markdown'):
            continue

        f = open(os.path.join(POSTS_DIR, filename))
        yml = f.read().split('---\n')[-2]

        try:
            tags =  yaml.load(yml).get('tags')
        except Exception, e:
            print filename
            import pdb; pdb.set_trace()

        if tags and len(tags):
            continue

        print f.name


def tagged(tag):
    """Show posts tagged with ``tag``"""

    # Open all files in _posts

    # Parse the yml section
    # Remember the file names that have tags matching tag
