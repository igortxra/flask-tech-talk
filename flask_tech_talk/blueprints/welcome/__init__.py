from flask import Blueprint
from .routes import welcome_world, welcome_name_age


bp = Blueprint('welcome', __name__, url_prefix='/welcome')
bp.add_url_rule('/', view_func=welcome_world, methods=['GET'])
bp.add_url_rule('/name', view_func=welcome_name_age, methods=['POST'])


def init_app(app):
    app.register_blueprint(bp)