#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from markdown import markdown

AUTHOR = 'Brian Blais'
SITENAME = 'bblais on the web'
SITEURL = 'https://bblais.github.io'

#THEME='themes/twenty-pelican-html5up-master'
THEME='themes/pelican-elegant-bblais'
CUSTOM_CSS=True
TIMEZONE = 'America/New_York'

if 'elegant' in THEME:

    #GOOGLE_ANALYTICS='UA-47046885-1'
    GOOGLE_ANALYTICS='UA-47048778-1'

    LOAD_CONTENT_CACHE = False  # False during debugging

    # Feed generation is usually not desired when developing
    FEED_ALL_ATOM = None
    CATEGORY_FEED_ATOM = None
    TRANSLATION_FEED_ATOM = None

    ARTICLE_EXCLUDES = ('pages',)

    #PAGE_ORDER_BY = 'page-order'

    # 
    SOCIAL=[
    ('Email','mailto://bblais@bryant.edu','Email'),
        ('LinkedIn','http://www.linkedin.com/profile/view?id=106100922','LinkedIn'),
        ('Google-plus','<a href="https://plus.google.com/103727926638180804243" rel="publisher">','Google+'),
        ('Twitter','http://twitter.com/bblais','Twitter'),    
        ('YouTube','https://www.youtube.com/channel/UC8cN5_0dy5o9qNPpdLxPa8w','YouTube',),    
        ]
    SOCIAL_PROFILE_LABEL='<h2>Contact</h2>'

    SUBSCRIBE=[ ('Rss','http://feeds.feedburner.com/bblaisontheweb','Rss'),
    ('Twitter','http://twitter.com/bblais','Twitter'),    
    ('Check-Square','http://cloud.feedly.com/#subscription%2Ffeed%2Fhttp://web.bryant.edu/~bblais/','Feedly'),
    ]
    SUBSCRIBE_PROFILE_LABEL='<h2>Subscribe</h2>'

    DELETE_OUTPUT_DIRECTORY=False

    DEFAULT_PAGINATION = 10

    # Uncomment following line if you want document-relative URLs when developing
    RELATIVE_URLS = True


    PROJECTS = [{'name':'Statistical Inference for Everyone',
    'url':'statistical-inference-for-everyone-sie.html',
    'description': '<em>Statistical Inference for Everyone</em> is an introductory textbook on statistical inference, motivated by probability theory as logic.  It is intended for a Statistics 101 audience.'},

    {'name':'pyndamics: Python Numerical Dynamics Simulator',
    'url':'https://github.com/bblais/pyndamics',
    'description': 'This package provides a way to describe a dynamical system in terms of the differential equations, or the stock-flow formalism. It is a wrapper around the Scipy odeint function, with further functionality for time plots, phase plots, and vector fields.'},
    {
        'name': 'plasticity: synaptic modification in rate-based neurons',
        'url': 'https://github.com/bblais/plasticity',
        'description': 'Plasticity is a package with a convenient interface, used to run simulations of single cells and networks of neurons.'},
        {'name':'more...',
        'url':'pages/projects.html',
        'description':'A detailed list of my projects...'
        },
        
        ]
        
    DISQUS_SITENAME = 'bblaisontheweb'
    IMAGE_PREVIEW='Saturn_with_Dice_Square.png'
        
    STATIC_PATHS=['static','images','theme/images','theme/css']
        
    LANDING_PAGE_ABOUT={'title':'Professor Brian Blais',
        'details': markdown(open('content/static/about.txt').read())}    
        
    DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', 'social_links','404'))


    #MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', 'headerid', 'toc','elementid','urlize']
    MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra','toc',
    #'headerid','elementid',
    ]
    TAG_SAVE_AS = ''
    CATEGORY_SAVE_AS = ''
    AUTHOR_SAVE_AS = ''
    PLUGIN_PATHS = ['../pelican-plugins']
    PLUGINS = ['render_math','sitemap', 'extract_toc', 'tipue_search']    
    SITEMAP={'format':'xml'}


else:

    PATH = 'content'

    TIMEZONE = 'America/New_York'

    DEFAULT_LANG = 'en'

    # Feed generation is usually not desired when developing
    FEED_ALL_ATOM = None
    CATEGORY_FEED_ATOM = None
    TRANSLATION_FEED_ATOM = None
    AUTHOR_FEED_ATOM = None
    AUTHOR_FEED_RSS = None

    DELETE_OUTPUT_DIRECTORY=False

    # Blogroll
    LINKS = (('Pelican', 'http://getpelican.com/'),
             ('Python.org', 'http://python.org/'),
             ('Jinja2', 'http://jinja.pocoo.org/'),
             ('You can modify those links in your config file', '#'),)

    # Social widget
    SOCIAL = (('twitter', 'http://twitter.com/bblais'),
              ('linkedin', 'http://www.linkedin.com/profile/view?id=106100922'),
              ('github', 'http://github.com/bblais'),
              ('googleplus', 'https://plus.google.com/103727926638180804243'),
              ('youtube','https://www.youtube.com/channel/UC8cN5_0dy5o9qNPpdLxPa8w'),
              )

    DEFAULT_PAGINATION = 10

    # Uncomment following line if you want document-relative URLs when developing
    RELATIVE_URLS = True

    USE_FOLDER_AS_CATEGORY = True
    # Generate yearly archive
    YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

    # Show most recent posts first
    NEWEST_FIRST_ARCHIVES = True

    def sidebar(value):
        if value.startswith('archives') or value.startswith('category'):
            return 'right-sidebar'
        elif value == 'index':
            return 'index'
        else:
            return 'no-sidebar'

    JINJA_FILTERS = {'sidebar':sidebar}        

    STATIC_PATHS = ['images',
                    'fonts',
                    'css',
                    'js',
                    ]

    ARTICLE_URL = "blog/{slug}"
    ARTICLE_SAVE_AS = "blog/{slug}/index.html"

    ARCHIVES_URL = "blog"
    ARCHIVES_SAVE_AS = "blog/index.html"

    PAGE_DIR = 'pages'
    PAGE_URL = '{slug}'
    PAGE_SAVE_AS = '{slug}/index.html'

    CATEGORY_URL = "category/{slug}/"
    CATEGORY_SAVE_AS = "category/{slug}/index.html"

    TAG_URL = "tag/{slug}/"
    TAG_SAVE_AS = "tag/{slug}/index.html"

    DISQUS_SITENAME = 'bblaisontheweb'
    IMAGE_PREVIEW='Saturn_with_Dice_Square.png'

    MD_EXTENSIONS = ['codehilite(css_class=highlight)', 
                        'toc',
                        ]
                    # 'extra','toc','headerid',
                    # 'elementid']


