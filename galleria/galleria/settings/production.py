"""
Django settings for galleria production project.

"""
"""
Local Django settings for galleria project.

"""

from .base import *

ALLOWED_HOSTS = ['*'] # This is like the debug case and should be overridden in the private settings file

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

# #Storage on S3 settings are stored as os.environs to keep settings.py clean
# if not DEBUG:
#    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
#    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
#    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
#    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#    STATIC_URL = S3_URL