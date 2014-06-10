"""
Django settings for deploying galleria to a staging site.

"""
"""
Local Django settings for galleria project.

"""

from .base import *

# Just in case we have a problem
#DEBUG = True
#TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


DATABASE_HOST = 'galleria-staging.cpgyypvjajxe.eu-west-1.rds.amazonaws.com'

#Allow local override which is per deployment instance.  There should probably then be an instance
# git for version control of that data
try:
    import sys
    #Use production settings to be just like production in this release.  The private path will need to match
    private_path = BASE_PRIVATE_DIR.child('production')
    sys.path.append(private_path)
    from private_settings import *
except ImportError:
    print(" No staging overide private_settings.py found in  = {}".format(private_path))
    # If it doesnt' exist that is fine and just use application defaults

