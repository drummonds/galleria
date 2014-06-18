"""
Django settings for deploying galleria to a staging site.

"""
"""
Local Django settings for galleria project.

"""
from .base import *

# Just in case we have a problem / can remove if impersonating exactly production
DEBUG = True
TEMPLATE_DEBUG = True

THIRD_PARTY_APPS += (
    'debug_toolbar',
    )

MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
  ) + MIDDLEWARE_CLASSES

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': "%s.true" % __name__,
}

def true(request):
    return True

#Allow local override which is per deployment instance.  There should probably then be an instance
# git for version control of that data
try:
    import sys
    #Use production settings to be just like production in this release.  The private path will need to match
    private_path = BASE_PRIVATE_DIR.child('staging')
    sys.path.append(private_path)
    from private_settings import *

except ImportError:
    print(" No staging override private_settings.py found in  = {}".format(private_path))
    # If it doesnt' exist that is fine and just use application defaults

# #Storage on S3 settings are stored as os.environs to keep settings.py clean
# if not DEBUG:
#    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
#    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
#    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
#    STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
#    S3_URL = 'http://%s.s3.amazonaws.com/' % AWS_STORAGE_BUCKET_NAME
#    STATIC_URL = S3_URL