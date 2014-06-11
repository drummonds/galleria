__author__ = 'ubuntu'
# from here http://stackoverflow.com/questions/4664724/distributing-django-projects-with-unique-secret-keys/24171873#24171873
from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
print("Run this and then add the next line to your ~/project/galleria_private/production/private_settings.py")
print("SECRET_KEY='{}'".format(get_random_string(50, chars)))
