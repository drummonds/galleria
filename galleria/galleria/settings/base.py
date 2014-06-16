"""
Django settings for galleria project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
import os

# Build paths inside the project like this: BASE_DIR.child("media")

from unipath import Path
SETTINGS_DIR = Path(__file__).expand_user().expand_vars().norm().absolute()
BASE_DIR = SETTINGS_DIR.ancestor(3) #Root of Django project
BASE_APP_DIR = SETTINGS_DIR.ancestor(2) #Root of main app of Django project
PROJECT_NAME = BASE_DIR.name # eg galleria

#The BASE_PRIVATE_DIR is the root of settings that should not be in the public GIT they are the information
# that will customise the application to a specific client. So for development this should be very little but possible
# if you like to have something a particular way and vital for production.

BASE_PRIVATE_DIR = SETTINGS_DIR.ancestor(5).child(PROJECT_NAME + '_private')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5rg#+%$#&c@q6#5r=u^ji0q9&&+5*v(r5wd)y(autnmz5n0bd%'

ALLOWED_HOSTS = []


# Application definition

DEFAULT_APPS = (
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles', #Automatically serves static files from runserver when DEBUG==True
)

THIRD_PARTY_APPS = (
    'south',
    'bootstrap3',
    'django_markdown', # to provide markdown editing
    'crispy_forms',
    'django_tables2',
    'django_filters',
)

LOCAL_APPS = (
    'categories',
    'contacts',
    'artists',
    'galleria',
    'stocks',
    'products',
)

INSTALLED_APPS = DEFAULT_APPS + THIRD_PARTY_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'galleria.urls'

WSGI_APPLICATION = 'galleria.wsgi.application'

TEMPLATE_DIRS = (
    BASE_APP_DIR.child('templates'),
)

CRISPY_TEMPLATE_PACK = 'bootstrap3'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

from django.conf import global_settings
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",

    "galleria.context_processors.galleria_context_processor",
)

DATABASE_HOST = 'galleria.somewhere.eu-west-1.rds.amazonaws.com'
DATABASE_PORT = 3306
DATABASE_USER = 'postgres_admin'
DATABASE_PASSWORD = '1234-is-not-safe'

#Defined in private
#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2',
#        'NAME': 'galleria_db',
#        'USER': DATABASE_USER,
#        'PASSWORD': DATABASE_PASSWORD,
#        'HOST' : DATABASE_HOST,
#        'PORT': DATABASE_PORT,
#    }
#}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/ubuntu/projects/galleria/galleria/static/'

LOGIN_URL = '/login'
LOGIN_REDIRECT_URL = '/'

try:
    from local_settings import *
except ImportError:
    pass

#Application settings to customise the look and feel of the application
GALLERIA_BRAND = PROJECT_NAME
GALLERIA_FRONTPAGE = '<img src="https://raw.githubusercontent.com/drummonds/galleria/master/documentation/images/home-sketch.png" alt=" Galleria home page" />'

# For grappelli the appdirectories needs to be first
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

#Grappelli customisation
GRAPPELLI_ADMIN_TITLE="Galleria admin"

#Just in case Debug toolbar is being used it must be configured explicitly to work under UWSGI
DEBUG_TOOLBAR_PATCH_SETTINGS = False