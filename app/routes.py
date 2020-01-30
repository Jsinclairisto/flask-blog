#import certain functions into the global
#namespace
from app import app
from os import walk
from markdown import markdown
from flask import render_template_string
from flask import render_template
from app.blog_helpers import render_markdown
from app.blog_helpers import LoginForm
import os
#safe global import (okay to use)
import flask

#global import (try to avoid)
#from flask import *

#home page
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()

    # if request.methpd == 'POST':
    #     session['key'] = request.values['user_name']

    return render_template('login.html', title='Sign In', form=form)

@app.route('/all')
def temp_listings():

    file_path = os.chdir('app/templates/')

    print(file_path)
    # temp_path = os.path.basename('/home/jakob/Desktop/flask-blog/app/')

    files = os.listdir(file_path)
    print(files)

    return render_template('all.html', files=files)

    #if (os.getcwd = os.curdir()):

    

#generic page
@app.route("/<view_name>")

#input parameter name must match route parameter
def render_page(view_name):
    html = render_markdown(view_name + '.html')
    return render_template_string(html, view_name = view_name)


