from flask import redirect, url_for, request
# import flask_login

from disco import app, strava_client
from .. import mod


@mod.route('/authorized', methods=['GET'])
def authorized():
    """
    Authorize a user on the site.
    """
    code = request.args['code']
    token_resp = strava_client.exchange_code_for_token(
        client_id=app.config['STRAVA_CLIENT_ID'],
        client_secret=app.config['STRAVA_CLIENT_SECRET'],
        code=code
    )
    strava_client.access_token = token_resp["access_token"]
    strava_client.refresh_token = token_resp["refresh_token"]
    athlete = strava_client.get_athlete()

    # need something to store the athlete or access token
    # to allow us to get more information
    # profile = check_profile(athlete, access_token)
    # flask_login.login_user(profile)
    return redirect(url_for('main.logged_in', profile_id=athlete.id))
