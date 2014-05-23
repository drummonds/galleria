"""
Django settings for deploying galleria to a staging site.

"""
"""
Local Django settings for galleria project.

"""

from .base import *

#Allow local override which is per deployment instance.  There should probably then be an instance
# git for version control of that data
try:
    import sys
    private_path = BASE_PRIVATE_DIR.child('staging')
    sys.path.append(private_path)
    from private_settings import *
except ImportError:
    print(" No staging overide private_settings.py found in  = {}".format(private_path))
    # If it doesnt' exist that is fine and just use application defaults

