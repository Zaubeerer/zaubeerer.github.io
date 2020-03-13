#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = "Robin Beer"
SITENAME = "Robin Beer"
SITEURL = ""
SITELOGO = SITEURL + "/images/BEER_2018_2896_zoom.jpg"
FAVICON = SITEURL + "/images/favicon_squared.ico"
# EXTENDED_FAVICON_DIR = SITEURL + "/images/favicon_io/"
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
    # ("Search", "/pages/search.html"),
    ("Home", "https://www.robin-beer.de"),  # TODO: exchange this with a relative URL ?
)

# Social widget
SOCIAL = (
    ("twitter", "https://twitter.com/R_E_Beer"),
    ("linkedin", "https://www.linkedin.com/in/robin-beer-7595b680/"),
    ("github", "https://github.com/Zaubeerer"),
)

# TWITTER_USERNAME = "RE_E_Beer"
# GITHUB_USERNAME = "Zaubeerer"
# LINKEDIN_USERNAME = "robin-beer-7595b680"  # might not be used at all

DEFAULT_PAGINATION = 10

# theme settings
THEME = "/Users/robinbeer/Desktop/Pybites/pelican-themes/Flex"

# Flex
SITETITLE = "Robin Beer"
SITESUBTITLE = "Energy Data Scientist"
SITEDESCRIPTION = "Pythonic Energy Data Science Blog"
# BROWSER_COLOR = ""
# PAGES_SORT_ATTRIBUTE = Date?
# PYGMENTS_STYLE = 'vs'
LINKS_IN_NEW_TAB = "external"  # TODO: fix this (especially when clicking on "Home" link should open in same window)
# GOOGLE_ANALYTICS

# TODO: Inform about copyright
# COPYRIGHT_NAME = "Robin Beer"
# COPYRIGHT_YEAR =
# CC_LICENSE
# ROBOTS

GITHUB_CORNER_URL = "https://github.com/Zaubeerer"

# MAIN_MENU = True
MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html"),
)

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# embed jupyter notebooks and post stats
MARKUP = ("md", "ipynb")
PLUGIN_PATHS = ["../pelican-plugins/"]

PLUGINS = ["readtime", "pelican-ipynb.markup", "post_stats"]
# IPYNB_USE_META_SUMMARY = True
# IGNORE_FILES = [".ipynb_checkpoints"]
