from flask import Flask, json, request, url_for, redirect, abort
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
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
        self.chat_id = None

def leave_chat(user):
    chatroom = get_chatroom_by_id(user.chat_id)
    user.chat_id = None
    chatroom.users.remove(user)

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

@app.route('/profile')
@login_required
def profile():
    return "profile"

@app.route('/logout')
@login_required
def logout():
    leave_chat(current_user)
    logout_user()
    return redirect(url_for('homepage'))

@app.route('/allchat')
@login_required
def all_chat():
    chatrooms = get_free_chatrooms(get_chatrooms())
    return "chatrooms"

@app.route('/chat/<int:chatyppl>')
@login_required
def chat(id):
    chatroom = get_chatroom_by_id(id)
    chatroom.users.append(current_user)
    current_user.chat_id = id
    return f'In chat {id}'

@app.route('/chat/<int:chatyppl>/post', methods = ['POST'])
@login_required
def post_chat(id):
    chatroom = get_chatroom_by_id(id)
    message = request.data
    chatroom.messages.append(message)

@app.route('/buddy')
@login_required
def buddy():
    return "ppl i liked"

@app.route('/forum')
@login_required
def forum():
    return "this is a forum, sorry i couldn't think of something funny"

if __name__ == "__main__":
    app.run()
