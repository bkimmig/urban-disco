from flask import render_template
import flask_login

from .. import mod
from ... import authorize_url

@mod.route('/', methods=['GET'])
def landing():
    """
    Return a greeting on the main page.
    """
    greeting = 'Welcome to Urban Disco!'

    return render_template(
        'main/home.html',
        greeting=greeting,
        auth_url=authorize_url
    )


@mod.route('/home', methods=['GET'])
def logged_in():
    """
    Somewhere to redirect when logged in.
    """
    profile = flask_login.current_user
    return render_template(
        'main/home.html',
        profile=profile.to_dict()
    )

