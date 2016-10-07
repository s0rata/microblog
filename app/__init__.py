import os
from flask import Flask
from flask_login import LoginManager
from flask_openid import OpenID 
from config import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from flask_sqlalchemy import SQLAlchemy 
from .momentjs import momentjs
from flask_babel import Babel 

app = Flask(__name__)
app.config.from_object('config')
app.jinja_env.globals['momentjs'] = momentjs

db = SQLAlchemy(app)

babel = Babel(app)

lm = LoginManager()
oid = OpenID(app, os.path.join(basedir, 'tmp'))
lm.init_app(app)
lm.login_view = 'login'



from app import views, models

if not app.debug:
	import logging
	from logging.handlers import SMTPHandler, RotatingFileHandler

	# Mail 
	credentials = None
	if MAIL_USERNAME or MAIL_PASSWORD:
		credentials = (MAIL_USERNAME, MAIL_PASSWORD)
	mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'microblog failure', credentials)
	mail_handler.setLevel(logging.ERROR)
	app.logger.addHandler(mail_handler)

	# Loggin
	file_handler = RotatingFileHandler('tmp/microblog.log', 'a', 1 * 1024 * 1024, 10)
	file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
	app.logger.setLevel(logging.INFO)
	file_handler.setLevel(logging.INFO)
	app.logger.addHandler(file_handler)
	app.logger.info('microblog startup')