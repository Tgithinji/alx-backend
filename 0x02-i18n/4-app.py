#!/usr/bin/env python3
"""Basic flask app
"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """get the locale
    """
    lang = request.args.get('locale')
    if lang in app.config["LANGUAGES"]:
        return lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """render index page
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run()
