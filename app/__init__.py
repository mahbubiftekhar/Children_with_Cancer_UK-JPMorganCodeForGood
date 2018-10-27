from flask import Flask, json, request, url_for, redirect, abort
from flask_login import UserMixin, LoginManager, login_user, login_required
import uuid
import datahelper
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'secret')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'homepage'


active_users = {}

class User(UserMixin):
    def __init__(self):
        self.id = str(uuid.uuid4())

@login_manager.user_loader
def load_user(id):
    return active_users.get(id)
        
@app.route('/')
def homepage():
    return "homepage things"

@app.route('/login', methods = ['POST'])
def login():
    if request.headers['Content-Type'] != 'application/json':
        abort(404)
    username = request.json["user"]
    password = request.json["key"]
    if datahelper.auth(username, password):
        login_user(User())
        return redirect(url_for("db"))
    else:
        return redirect(url_for("homepage"))

@app.route('/db')
@login_required
def db():
    return "good boi, logged in"

@app.route('/kb')
def kb():
    return "wiki"

@app.route('/logout')
def logout():
    return "bye bye"

@app.route('/allChat')
def allChat():
    return "chatrooms"

@app.route('/oneChat/<chatyppl>')
def oneChat(name):
    return ""

@app.route('/buddy')
def buddy():
    return "ppl i liked"

@app.route('/forum')
def forum():
    return "this is a forum, sorry i couldn't think of something funny"

if __name__ == "__main__":
    app.run()
