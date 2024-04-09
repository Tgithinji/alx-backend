#!/usr/bin/env python3
"""Basic flask app
"""
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """FLASK APP CONFIGURATION CLASS
    """
    LANGUAGE = ['EN', 'FR']
    default_locale = 'en'
    default_timezone = 'UTC'


app.config.from_object(Config)


@app.route('/')
def index():
    """render index page
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
