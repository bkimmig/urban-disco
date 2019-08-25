from flask import Flask
import flask_login

# Define the WSGI application object
app = Flask(__name__)
app.config.from_object('config')

# ########################################################################## #
## Strava
from stravalib.client import Client

strava_client = Client()
authorize_url = strava_client.authorization_url(
    client_id=app.config['STRAVA_CLIENT_ID'],
    redirect_uri='http://localhost:8888/authorized'
)

# ########################################################################## #
from . import main

## blueprints, set up the routes
app.register_blueprint(main.mod)

## login manager - THIS IS NOT SECURE but it is fine for a minute
login_manager = flask_login.LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(profile_id):
    profile = [] # Profile.objects(id=profile_id)[0]
    if len(profile) == 0:
        profile = None

    return profile

