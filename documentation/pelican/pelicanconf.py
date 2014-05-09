#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Humphrey Drummond'
SITENAME = 'galleria documentation'
SITEURL = 'http://drummonds.gihub.io/galleria'
RELATIVE_URLS = False


TIMEZONE = 'Europe/london'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
	  ("Markdown syntax", 'http://daringfireball.net/projects/markdown/syntax'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),
          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = ['images']
THEME = "/home/trusty/projects/galleria/documentation/pelican_theme/bootstrap2H3"

#Exclude Archive directory
ARTICLE_EXCLUDES = (('archive','output')) #syntax error?
PAGE_EXCLUDES = (('archive','output')) #syntax error?

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""
