from markdown import markdown
from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from flask_sqlalchemy import SQLAlchemy
from app import app
import os

db = SQLAlchemy(app)


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password = db.Column(db.String(50))


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

class SignInForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)]) 
    emailAddress = StringField('Email', validators=[DataRequired(),Length(min=6, max=25)])

db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)

def render_markdown(file_name, dir_path = 'app/templates'):
    """Takes the specified file path and
    returns it as HTML
    """
    html = ""

    #os.path.join creates an OS-valid path
    path = os.path.join(dir_path, file_name)
    with open(path) as html_file:
        html = html_file.read()
        html = markdown(html)
    return html


