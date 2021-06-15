from os import environ
from dotenv import load_dotenv
from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from twitter.twitter import TwitterApi

load_dotenv()

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URI')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

consumer_key = environ.get('CONSUMER_KEY')
consumer_secret = environ.get('CONSUMER_SECRET')
access_token = environ.get('ACCESS_TOKEN')
access_token_secret = environ.get('ACCESS_TOKEN_SECRET')

twitterAPI = TwitterApi(consumer_key, consumer_secret, access_token, access_token_secret)

from models.profile import Profile
