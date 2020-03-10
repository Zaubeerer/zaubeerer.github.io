#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Robin Beer"
SITENAME = "Robin Beer"
SITEURL = ""
SITELOGO = SITEURL + '/images/BEER_2018_2896_zoom.jpg'

PATH = "content"

TIMEZONE = "Europe/Paris"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "http://getpelican.com/"),
    ("Python.org", "http://python.org/"),
    ("Jinja2", "http://jinja.pocoo.org/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

THEME = "/Users/robinbeer/Desktop/Pybites/pelican-themes/Flex"
STATIC_PATHS = ['images', 'pdfs']

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
