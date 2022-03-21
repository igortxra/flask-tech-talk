from flask import Blueprint
from .routes import hello_name, hello_world


bp = Blueprint('hello', __name__, url_prefix='/')

bp.add_url_rule("/", view_func=hello_world)
bp.add_url_rule("/name", view_func=hello_name)


def init_app(app):
    app.register_blueprint(bp)
