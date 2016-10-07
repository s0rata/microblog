# -*- coding: utf-8 -*-

import os

basedir = os.path.abspath(os.path.dirname(__file__))

# SqlAlchemy config
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True

# Mail server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

# Administrator list
ADMINS = ['skimchhorng@yahoo.com']

# WTForms config
WTF_CSRF_ENABLED = True 
SECRET_KEY = 'you-will-never-guess'
OPENID_PROVIDERS = [
	{'name': 'Google', 'url': 'http://google.com/'},
	{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
	{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
	{'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
	{'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

# Pagination 
POSTS_PER_PAGES = 3 

# Whoosh config
WHOOSH_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50 

#available languages
LANGUAGES = {
	'en': 'English',
	'es': 'Español'
}

SQLALCHEMY_RECORD_QUERIES = True
# slow database query threshold (in seconds)
DATABASE_QUERY_TIMEOUT = 0.5