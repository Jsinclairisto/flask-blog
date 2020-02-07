from markdown import markdown
from flask_wtf import FlaskForm
from flask import render_template
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Length

import os

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=25)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')

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


