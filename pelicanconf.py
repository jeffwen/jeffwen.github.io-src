#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Jeff Wen'
SITENAME = u'Jeff Wen'
SITEURL = 'http://jeffwen.github.io'
#SITEURL = 'http://localhost:8000'


PATH = 'content'

TIMEZONE = 'America/Los_Angeles'
TAGLINE = 'aspiring data scientist, problem solver, wannabe tinkerer'

DEFAULT_LANG = u'en'
DEFAULT_DATE_FORMAT = ('%B %d %Y')

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

# Blogroll
# LINKS = (('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('LinkedIn', 'https://www.linkedin.com/in/wenjeff'),
          ('GitHub', 'https://github.com/jeffwen'),
          ('Email', 'mailto:jeff.li.wen@gmail.com'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme for the blog
THEME = '/Users/Jeffwen/Blog/ghblog/pelican-themes/svbhack'

USER_LOGO_URL = SITEURL + '/images/jeff_logo.png'


