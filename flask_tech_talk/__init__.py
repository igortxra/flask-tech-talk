from flask import Flask

from flask_tech_talk.ext import configuration, database
from flask_tech_talk.blueprints import hello, welcome, user


def create_app():
    app = Flask(__name__)
    
    configuration.init_app(app)
    database.init_app(app)
    hello.init_app(app)
    welcome.init_app(app)
    user.init_app(app)

    return app