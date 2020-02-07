from flask import Flask
from flask_bootstrap import Bootstrap
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shhhhh_its_a_secret'
Bootstrap(app)
from app import routes