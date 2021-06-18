#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Brian Blais'
SITENAME = 'bblais on the web'
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 12

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

import logging
LOG_FILTER = [(logging.WARN, 'Empty alt attribute for image %s in %s')]

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'

STATIC_PATHS=['static','images','theme/images',]
EXTRA_PATH_METADATA = {
    'theme/images/favicon.ico': {'path': 'favicon.ico'}
}

THEME='themes/Abstract - bblais'
CUSTOM_CSS=True
ARTICLE_EXCLUDES = ('pages','publish',)
DIRECT_TEMPLATES = ['index',]

PLUGIN_PATHS = ['/Users/bblais/Documents/Git/pelican-plugins']
PLUGINS = ['render_math','sitemap', 'extract_toc', 'tipue_search']    
SITEMAP={'format':'xml'}


