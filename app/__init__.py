from flask import Flask
from flask_bootstrap import Bootstrap
import config

app = Flask(__name__)
app.config['SECRET_KEY'] = 'shhhhh_its_a_secret'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
Bootstrap(app)
from app import routes