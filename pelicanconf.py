#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Brian Blais'
SITENAME = 'bblais on the web'
SITEURL = 'http://localhost:8000'

DISQUS_SITEURL = 'https://bblais.github.io'
DISQUS_SITENAME = 'bblaisontheweb'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None



# Social widget
SOCIAL = {'twitter': 'https://twitter.com/bblais',
'linkedin':'https://www.linkedin.com/in/brian-blais-bb66482b/',
'github':'https://github.com/bblais',
'email':'mai&#108;&#116;o&#58;b&#37;6&#50;%6C&#37;61i%&#55;3%40%62ry&#37;61nt%2Eed&#37;7&#53;',
'youtube':'https://www.youtube.com/channel/UC8cN5_0dy5o9qNPpdLxPa8w',
'rss':'https://bblais.github.io/feeds/all.atom.xml'}

DEFAULT_PAGINATION = 21
SUMMARY_MAX_LENGTH = 30

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

ABOUT = """I am a Scientist, Skeptic, and Professor at <a href='http://www.bryant.edu/'>Bryant University</a>.  My goal is to make technical subject matters widely accessible and to use my analytical and computational skills to assist anyone with their science-related problems."""

ABOUT_LONG= """
I am a Scientist, Skeptic, and Professor at <a href='http://www.bryant.edu/'>Bryant University</a>.  
My goal is to make technical subject matters widely accessible and to use my analytical and computational skills 
to assist anyone with their science-related problems.
<p>
I am a big fan of Babylon 5 and MST3K, and have a a broad interest in scientific reasoning and quantifying uncertainties.  As such, I have 
published in disease modeling, paleoclimate, neuroscience, and molecular biology.  I also work in science pedagogy, always looking
for improved ways to communicate science, its processes, and the confidence we can place on claims.  As such, I use my blog to explore
the intersection of science and society.  
<p>
I sincerely enjoy helping develop tools to aid in quantitative research, so please contact me if you'd like to collaborate!
"""
ABOUT_PICTURE='bblais_mst3k_b5.png'
AVATAR='bblais_avatar.jpg'


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





# THEME='themes/elegant-master'
# AUTHORS=['bblais']
# DIRECT_TEMPLATES = ['index','archives', 'search','tags']



CUSTOM_CSS=True
ARTICLE_EXCLUDES = ('pages','publish',)

THEME='themes/html5up-editorial - bblais'
DIRECT_TEMPLATES = ['index','about','archives', 'contact','thanks','search','tags']

import markdown
print("Markdown version: ",markdown.__version__)

from markdown import markdown

MARKDOWN = {
    'extensions': [
        'markdown.extensions.attr_list',
        'markdown.extensions.codehilite',
        'markdown.extensions.extra',
        'markdown.extensions.meta',
        'markdown.extensions.toc',
        'markdown.extensions.footnotes',
        'mdx_linkify',
    ],
    'extension_configs': {
        'markdown.extensions.codehilite': {
            'noclasses': True,
            'pygments_style': 'native',
            'css_class': 'highlight',
        },
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc': {
            'title': 'Table of Contents',
        },
        'markdown.extensions.footnotes': {},
    },
    'output_format': 'html5',
}

PLUGIN_PATHS = ['/Users/bblais/Documents/Git/pelican-plugins']
IGNORE_FILES = [".ipynb_checkpoints",'*.py']
IPYNB_MARKUP_USE_FIRST_CELL = True

PLUGINS = ['pelican_katex','sitemap', 'tipue_search','obsidian']    
SITEMAP={'format':'xml'}
TIPUE_SEARCH = True
TEMPLATE_PAGES = {
    'search.html': 'search.html',
}