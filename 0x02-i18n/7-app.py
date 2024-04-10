#!/usr/bin/env python3
"""Basic flask app
"""
import pytz
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """FLASK APP CONFIGURATION CLASS
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """returns the user dictionary if id is found
    """
    user_id = request.args.get('login_as')
    if user_id is None:
        return None
    if int(user_id) in users:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request():
    """executed before all
    """
    g.user = get_user()


@babel.localeselector
def get_locale():
    """get the locale
    """
    lang = request.args.get('locale')
    if lang in app.config["LANGUAGES"]:
        return lang
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """return timezone
    """
    try:
        if request.args.get('timezone'):
            return pytz.timezone(request.args.get('timezone')).zone
        if g.user and g.user.get('timezone'):
            return pytz.timezone(g.user['timezone']).zone
    except pytz.exceptions.UnknownTimeZoneError:
        pass
    return 'UTC'


@app.route('/')
def index():
    """render index page
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
