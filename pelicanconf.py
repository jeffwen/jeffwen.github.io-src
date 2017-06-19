#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Jeff Wen'
SITENAME = u'Jeff Wen'
SITEURL = 'http://jeffwen.github.io'
#SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'America/New_York'

# Default language and date formatting
DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = ('%B %d %Y')

# URL set up
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'

ARCHIVES_SAVE_AS = 'archives.html'
YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Google Analytics
GOOGLE_ANALYTICS = 'UA-70808160-1'

#DISQUS
DISQUS_SITENAME = 'jeffwen-blog'

# Blogroll
# LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/wenjeff'),
          ('GitHub', 'https://github.com/jeffwen'),
          ('Email', 'mailto:jeff.li.wen@gmail.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme specfic modifications for the blog
THEME = '/Users/jwen/Blog/ghblog/pelican-themes/svbhack'
TAGLINE = 'aspiring data scientist, problem solver, wannabe tinkerer'
USER_LOGO_URL = SITEURL + '/images/jeff_logo.png'


