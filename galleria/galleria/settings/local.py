"""
Local Django settings for galleria project.

"""
from unipath import Path

from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

# Write the email to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = 5432
DATABASE_USER = 'postgres_admin'
DATABASE_PASSWORD = '0123-4567-890A-BCDE-FGHI'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'galleria_db',
        'USER': DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST' : DATABASE_HOST,
        'PORT': DATABASE_PORT,
    }
}

CRISPY_TEMPLATE_PACK = 'bootstrap3'

INSTALLED_APPS += (
    'debug_toolbar',
    'crispy_forms',
    'stocks',
    )
    

#Allow local override which is per deployment instance.  There should probably then be an instance
# git for version control of that data
try:
    import sys
    private_path = BASE_PRIVATE_DIR.child('local')
    sys.path.append(private_path)
    from private_settings import *
except ImportError:
    print(" No local overide private_settings.py found in  = {}".format(private_path))
    # If it doesnt' exist that is fine and just use application defaults


