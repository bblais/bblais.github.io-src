#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from markdown import markdown

AUTHOR = 'Brian Blais'
SITENAME = 'bblais on the web'
SITEURL = 'http://localhost:8000'
#SITEURL = 'https://bblais.github.io'

ABOUT = "I am a Scientist, Skeptic, and <a href='http://web.bryant.edu/~science'>Professor</a> at <a href='http://web.bryant.edu/~science'>Bryant University</a> and the <a href='https://www.brown.edu/research/projects/brain-and-neural-systems/'>IBNS, Brown University</a>.  I have published in synaptic plasticity in vision, paleoclimate proxies, the dynamics of zombies, and using automatic flushing toilets to teach scientific methods.  My goal is to make technical subject matters widely accessible and to use my analytical and computational skills to assist anyone with their science-related problems."

ABOUT = "I am a Scientist, Skeptic, and <a href='http://web.bryant.edu/~science'>Professor</a> at <a href='http://web.bryant.edu/~science'>Bryant University</a> and the <a href='https://www.brown.edu/research/projects/brain-and-neural-systems/'>IBNS, Brown University</a>.  My goal is to make technical subject matters widely accessible and to use my analytical and computational skills to assist anyone with their science-related problems."

ABOUT_BLOG="Here I explore the intersection of science and society, as well as the life and tools of an academic, and anything else that strikes my fancy."

SLIDER=[]

SLIDER.append(
    {
    'image':'rosie-fraser-187327-unsplash.jpg',
    'attribution': 'Photo by Rosie Fraser on Unsplash',
    'url':'posts/2019/Jan/14/dynamical-systems-with-pyndamics/',
    'title':'Zombies, Twitter, and the Fate of the Universe',
    'text':"Use <em>pyndamics</em> to model dynamical systems and fit your data."
    }
)

SLIDER.append(
    {
    'image':'Saturn1.jpg',
    'attribution':'https://en.wikipedia.org/wiki/File:Saturn_eclipse.jpg',
    'url':'posts/2019/Jan/14/stats-for-everyone/',
    'title':'Stats for Everyone',
    'text':"Read the book, see the movie, let's talk about your research."
    }
)

SLIDER.append(
    {
    'image':'neuron1.jpg',
    'attribution':'https://www.flickr.com/photos/functionalneurogenesis/7930156342',
    'url':'posts/2019/Jan/14/models-of-learning-and-memory/',
    'title':'Rewiring the Brain',
    'text':"Explore models of synaptic plasticity from molecules to memory with <em>Plasticnet</em>"
    }
)



THEME='themes/elen - bblais'
#THEME='themes/colossus - bblais'
#THEME='themes/pelican-elegant-1.3'

CUSTOM_CSS=True
TIMEZONE = 'America/New_York'

#GOOGLE_ANALYTICS='UA-47046885-1'
GOOGLE_ANALYTICS='UA-47048778-1'

LOAD_CONTENT_CACHE = False  # False during debugging

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

ARTICLE_EXCLUDES = ('pages','publish',)

#PAGE_ORDER_BY = 'page-order'

# 
TWITTER_USERNAME='bblais'

SOCIAL = {'twitter': 'https://twitter.com/bblais',
'linkedin':'https://www.linkedin.com/in/brian-blais-bb66482b/',
'github':'https://github.com/bblais',
'email':'mai&#108;&#116;o&#58;b&#37;6&#50;%6C&#37;61i%&#55;3%40%62ry&#37;61nt%2Eed&#37;7&#53;',
'youtube':'https://www.youtube.com/channel/UC8cN5_0dy5o9qNPpdLxPa8w',}

SUBSCRIBE=[ ('Rss','http://feeds.feedburner.com/bblaisontheweb','Rss'),
('Twitter','http://twitter.com/bblais','Twitter'),    
('Check-Square','http://cloud.feedly.com/#subscription%2Ffeed%2Fhttp://web.bryant.edu/~bblais/','Feedly'),
]
SUBSCRIBE_PROFILE_LABEL='<h2>Subscribe</h2>'

SUMMARY_MAX_LENGTH = 30

DELETE_OUTPUT_DIRECTORY=False

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

   
DISQUS_SITENAME = 'bblaisontheweb'
IMAGE_PREVIEW='Saturn_with_Dice_Square.png'
    
STATIC_PATHS=['static','images','theme/images','theme/layout','theme/css']
EXTRA_PATH_METADATA = {
    'theme/images/favicon.ico': {'path': 'favicon.ico'}
}

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
    
    
#DIRECT_TEMPLATES = (('index', 'tags', 'categories','archives', 'search', 'social_links','404'))
DIRECT_TEMPLATES = ['index', 'categories', 'contact','about', 'search','thanks','archives']
#DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors','contact', 'archives', 'search']
#(('index', 'about','contact','search'))

from mdx_urlize import UrlizeExtension

MARKDOWN = {
    'extensions':['attr_list','codehilite','extra','meta','toc','footnotes',UrlizeExtension()],
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown.extensions.toc' : {},
        'markdown.extensions.footnotes' : {},
    },
    'output_format': 'html5',
}


# TAG_SAVE_AS = ''
# CATEGORY_SAVE_AS = ''
AUTHOR_SAVE_AS = ''
PLUGIN_PATHS = ['/Users/bblais/Documents/Git/pelican-plugins']
PLUGINS = ['render_math','sitemap', 'extract_toc', 'tipue_search']    
SITEMAP={'format':'xml'}

ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = 'pages/{slug}.html'
PAGE_SAVE_AS = 'pages/{slug}.html'
