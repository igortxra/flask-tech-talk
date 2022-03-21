from flask import Blueprint
from .routes import get_users, insert_user


bp = Blueprint('user', __name__, url_prefix='/user')
bp.add_url_rule('get', view_func=get_users, methods=["GET"])
bp.add_url_rule('insert', view_func=insert_user, methods=["POST"])


def init_app(app):
    app.register_blueprint(bp)