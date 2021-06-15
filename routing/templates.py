from app import app
from flask import render_template
from models.profile import Profile
from app import twitterAPI

@app.route('/')
def index():
    profiles = Profile.get_last()
    
    return render_template("profiles.html", profiles=profiles)

@app.route('/<account_twitter>', methods=['GET'])
def profile(account_twitter):
    profile = Profile.get(account_twitter)
    tweets = twitterAPI.last_tweets(account_twitter)

    return render_template("one.html", profile=profile, tweets=tweets)

@app.route('/test')
def routing_test():
    return '<h2>It\'s works!!</h2>'
