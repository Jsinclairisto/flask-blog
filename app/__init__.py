from flask import Flask
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shhhhh_its_a_secret'
from app import routes