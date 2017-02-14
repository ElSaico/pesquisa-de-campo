#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Bruno Marques'
SITENAME = 'Pesquisa de Campo'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('StatsBomb', 'http://statsbomb.com/'),
    ('Deep xG', 'http://deepxg.com/'),
    ('Paste Soccer', 'https://www.pastemagazine.com/soccer'),
    ('American Soccer Analysis', 'http://www.americansocceranalysis.com/'),
    ('Front Office Report', 'http://frontoffice.report/'),
    ('Analytics FC', 'https://analyticsfc.co.uk/'),
    ('11tegen11', 'http://11tegen11.net/'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'http://twitter.com/DataMarques'),
    ('Facebook', 'http://facebook.com/bm2290'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['ipynb.markup']

