from flask import Flask


app = Flask(__name__)


from flask_tech_talk.hello import bp_hello
app.register_blueprint(bp_hello, url_prefix='/')

from flask_tech_talk.welcome import bp_welcome
app.register_blueprint(bp_welcome, url_prefix='/welcome')
