"""
Django settings for galleria production project.

"""
"""
Local Django settings for galleria project.

"""

from .base import *

#Allow local override which is per deployment instance.  There should probably then be an instance
# git for version control of that data
try:
    import sys
    private_path = BASE_PRIVATE_DIR.child('production')
    sys.path.append(private_path)
    from private_settings import *
except ImportError:
    print(" No production overide private_settings.py found.  This is probably an error  = {}".format(private_path))
    # If it doesnt' exist that is fine and just use application defaults

