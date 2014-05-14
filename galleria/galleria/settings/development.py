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

