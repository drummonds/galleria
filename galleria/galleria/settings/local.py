"""
Local Django settings for galleria project.

"""
from .base import *


DEBUG = True
TEMPLATE_DEBUG = True

# Write the email to the console
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = 5432
DATABASE_USER = 'postgres_admin'
DATABASE_PASSWORD = 'K4B9-RUrg-bao9-osUb-77Ur'

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

INSTALLED_APPS += ("debug_toolbar", )

