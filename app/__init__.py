from flask import Flask
from flask_bootstrap import Bootstrap

from flask_user import login_required, UserManager, UserMixin, SQLAlchemyAdapter
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from flask_sqlalchemy import SQLAlchemy

import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shhhhh_it_is_a_secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['CSRF_ENABLED'] = True
app.config['USER_ENABLE_EMAIL'] = False
db = SQLAlchemy(app)
Bootstrap(app)

from app import routes

