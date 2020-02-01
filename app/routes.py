#import certain functions into the global
#namespace
from app import app
from os import walk
from markdown import markdown
from flask import render_template_string, render_template, flash, redirect, request, url_for
from app.blog_helpers import render_markdown, LoginForm
import os
#safe global import (okay to use)
import flask

#home page
@app.route("/")
def home():
    return render_template('index.html')

#Success page. Directs here after form is submitted
@app.route('/success')
def success():
    return render_template('contacts.html')

#Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    # if request.method == 'POST':
    #     session['user_name'] = request.values['user_name']
    #     print('request.method is being called')
        
    if form.validate_on_submit():
        return redirect(url_for('success'))
        
    return render_template('login.html', title='Sign In', form=form)


@app.route('/all')
def temp_listings():

    #assigns current directory to base_path variable
    base_path = os.getcwd()
    #combines base path with target path. This way, it will work with all users.
    #They'll have different base paths, but will have the same sub-path of '/app/templates'
    dest_path = base_path + '/app/templates'

    #assigns combo to file_path
    file_path = os.path.relpath(dest_path, base_path)


    files = os.listdir(file_path)

    return render_template('all.html', files=files)

#generic page
@app.route("/<view_name>")

#input parameter name must match route parameter
def render_page(view_name):
    html = render_markdown(view_name + '.html')
    print('YOOOOO IT WORKS AYYYYY')
    return render_template_string(html, view_name = view_name)
    