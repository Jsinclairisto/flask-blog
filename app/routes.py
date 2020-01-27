from app import app
from markdown import markdown
from flask import render_template_string 
from app.blog_helpers import render_markdown

'''
global import (try to avoid)
from flask imprt *
'''
#home page
@app.route("/")
def home():
    
    '''
    #old way to open files
    html_file = open('app/views/index.html')
    html_file = html_file.read()
    html_file.close()
    return html
    '''

    #new way to open files (safer, easier)
    return render_markdown('index.md')

#about page
@app.route("/<view_name>")

#input parameter must match route parameter
def render_page(view_name):
    html = render_markdown(view_name + '.md')
    return render_template_string(html, view_name = view_name)

# #messages page
# @app.route("/Messages")
# def contact():
#     return render_markdown('messages.md')

