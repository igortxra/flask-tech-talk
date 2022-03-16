from flask import Blueprint


bp_welcome = Blueprint('welcome', __name__)


from .routes import *