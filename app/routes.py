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
       
# @app.route("/click_tracker", methods=['GET','POST'])
# def click_tracker():
#     view_name = {}
#     view_data[""]

#Login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    hasAccess = False
    # if request.method == 'POST':
    #     session['user_name'] = request.values['user_name']
    #     print('request.method is being called')
    
    if form.validate_on_submit():
        hasAccess = True
        return redirect('success')

    # view_data = {}
    # view_data["click_count"] = 0
    # if request.method == 'POST':
    #     view_data["click_count"] = request.values["click_count"]
    #     view_data["click_count"] = int(view_data["click_count"]) + 1

    
        
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
            

    #edit_page = render_markdown(edited_page_name + '.html')
    #base_path=temp_listings()
    #final_page = render_markdown(edit_file + '.html')


    # contents = ""
    # with open('app/templates/' + final_page) as f:
    #     for line in f.readlines():
    #         contents += line  
    #     return render_template('edit.html', contents=contents)
    
   

    #log = open(base_path, "r")

    # print(hasAccess)
    # if(hasAccess == True):
    #      return render_template_string(edit_page, edited_page_name = edited_page_name)
    # else:
    #     return '<h1>YOOOOOOOOOO NOOOOOOOOOOO</h1>'

@app.route('/createaccount')
def createaccount():
    return '<h1>POOP :D</h1>'
