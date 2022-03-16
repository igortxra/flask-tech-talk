from flask import Blueprint


bp_hello = Blueprint('hello', __name__)


from .routes import *