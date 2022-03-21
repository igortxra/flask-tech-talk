from flask import Flask

from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'sqlite:///dev.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
from flask_tech_talk.user.models import User # Importing After SQLAlchemy to avoid circular imports
db.create_all()


from flask_tech_talk.hello import bp_hello
app.register_blueprint(bp_hello, url_prefix='/')

from flask_tech_talk.welcome import bp_welcome
app.register_blueprint(bp_welcome, url_prefix='/welcome')


from flask_tech_talk.user import bp_user
app.register_blueprint(bp_user, url_prefix='/user')
