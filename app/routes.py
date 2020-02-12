#import certain functions into the global
#namespace
from app import app
from os import walk
from flask_user import roles_required, login_required
from markdown import markdown
from flask import render_template_string, render_template, flash, redirect, request
from app.blog_helpers import render_markdown, LoginForm
import urllib.request
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
    hasAccess = True
    print(hasAccess)
    return render_template('success.html')
       
#Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    hasAccess = False

    
    if form.validate_on_submit():
        hasAccess = True
        return redirect('success')        
    # else:
    #     return '<h1>YOU FUCKED UP AAAHHH!</h1>'

    return render_template('login.html', title='Sign In', form=form)

@app.route('/all')
def temp_listings():

    #view_data["pages"] = (['about.html', 'butt.html', 'icecream.html'])

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
@app.route('/<view_name>')

#input parameter name must match route parameter
def render_page(view_name):
    html = render_markdown(view_name + '.html')
    print('YOOOOO IT WORKS AYYYYY')
    return render_template_string(html, view_name = view_name)

@app.route('/edit/<edit_file>')   
@login_required
def edit(edit_file):
    hasAccess = login()
    output_page = render_markdown(edit_file + '.html')
    return render_template('edit.html', output_page=output_page)
            
@app.route('/createpost')
@login_required
def createpost():
    return '<h1>Hello People of Earth</h1>'
    
@app.route('/createaccount')
def createaccount():
    return '<h1>Currently in development...</h1>'
