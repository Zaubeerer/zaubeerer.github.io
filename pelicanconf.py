#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys

from emojiextension import EmojiExtension

AUTHOR = "Robin Beer"
SITENAME = "Robin Beer"
SITEURL = "https://www.robin-beer.de"
SITELOGO = "/images/BEER_2018_2896_small.jpg"
FAVICON = "/images/favicon_squared.ico"
EXTENDED_FAVICON_DIR = SITEURL + "/content/images/favicon_io/"
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
    # ("Schedule a call", "/pages/search.html"), # TODO: write a "Schedule a call" page and create the respective link here
    ("Home", SITEURL),  # TODO: exchange this with a relative URL ?
    # ("Python", "/category/python.html"),
    # ("Energy", "/category/energy.html"),
    # ("Collaboration", "/category/collaboration.html"),
    # ("Tools", "/category/tools.html"),
    # ("Miscellanea", "/category/miscellanea.html"),
    # ("PyBites", "https://www.pybit.es"),
)

# Social widget
SOCIAL = (
    ("twitter", "https://twitter.com/R_E_Beer"),
    ("linkedin", "https://www.linkedin.com/in/robin-beer-7595b680/"),
    ("github", "https://github.com/Zaubeerer"),
    ("envelope-o", "mailto:dev@robin-beer.de"),
    # ("gitlab", ""), # TODO: add (?)
    # ("stack-overflow")  #TODO: add (?)
)

# TWITTER_USERNAME = "RE_E_Beer"
# GITHUB_USERNAME = "Zaubeerer"
# LINKEDIN_USERNAME = "robin-beer-7595b680"  # might not be used at all

DEFAULT_PAGINATION = 10

# theme settings
THEME = r"C:\Users\rbeer\code\personal\Flex"
# Flex
SITETITLE = "Robin Beer"
SITESUBTITLE = "Energy Data Scientist"
SITEDESCRIPTION = "Pythonic Energy Data Science Blog"
# BROWSER_COLOR = ""
# PAGES_SORT_ATTRIBUTE = Date?
PYGMENTS_STYLE = "vs"  # TODO: maybe change highlighting style: https://github.com/alexandrevicenzi/Flex/wiki/Code-Highlight
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
PLUGIN_PATHS = ["./plugins/"]

# Markdown Configuration:
# MARKDOWN = {
#     "extensions": [EmojiExtension.create_from_json("./resources/emojis.json")],
#     "extension_configs": {
#         "markdown.extensions.codehilite": {"css_class": "highlight"},
#         "markdown.extensions.toc": {},
#         "markdown.extensions.extra": {},
#         "markdown.extensions.meta": {},
#     },
#     "output_format": "html5",
# }

PLUGINS = [
    "readtime",
    "pelican-ipynb.markup",
    "minchin.pelican.plugins.post_stats",
    "seo",
]
# IPYNB_USE_META_SUMMARY = True
IPYNB_USE_METACELL = True
IGNORE_FILES = [".ipynb_checkpoints"]

SEO_REPORT = True  # To enable this feature
SEO_ENHANCER = True  # To disable this feature
SEO_ENHANCER_OPEN_GRAPH = True  # The default value for this feature
SEO_ENHANCER_TWITTER_CARDS = True  # The default value for this feature

