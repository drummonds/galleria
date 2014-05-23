"""
Django settings for galleria development project.

"""
"""
Local Django settings for galleria project.

"""

from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

INSTALLED_APPS += ("debug_toolbar", )

#Allow local override which is per deployment instance.  There should probably then be an instance
# git for version control of that data
try:
    import sys
    private_path = BASE_PRIVATE_DIR.child('development')
    sys.path.append(private_path)
    from private_settings import *
except ImportError:
    print(" No development overide private_settings.py found in  = {}".format(private_path))
    # If it doesnt' exist that is fine and just use application defaults


