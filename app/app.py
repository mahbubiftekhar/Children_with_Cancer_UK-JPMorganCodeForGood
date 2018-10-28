#!/usr/bin/env python3

from flask import Flask, json, request, url_for, redirect, abort, render_template
from flask_login import UserMixin, LoginManager, login_user, login_required, current_user, logout_user
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
import uuid
from datahelper import *
import os
import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'secret')
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
socket = SocketIO(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/app.db'
database = SQLAlchemy(app)

active_users = {}
flagged_words = []

def check_content_type(content_type):
    return request.headers['Content-Type'] != content_type

def have_keys(info, keys):
    return (set(info.keys()) & keys) != keys

def leave_chat(user):
    chatroom = get_chatroom_by_id(user.chat_id)
    user.chat_id = None
    chatroom.users.remove(user)

def send_message(user, msg):
    data = {'name' : user.username,
            'msg'  : msg }
    socket.emit(f'chatroom_{user.chat_id}', data, broadcast=True)

def flag_to_moderator(user, msg):
    pass

@login_manager.user_loader
def load_user(id):
    return active_users.get(id)

@app.route('/', methods = ['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        if check_content_type('application/x-www-form-urlencoded'):
            abort(404)
        if have_keys(request.form, {'inputEmail', 'inputPassword'}):
            abort(404)
        username = request.form['inputEmail']
        password = request.form['inputPassword']
        user = auth(username, password)
        if user:
            user.session_token = uuid.uuid4()
            login_user(user)
            active_users[user.session_token] = user
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("login"))

@app.route('/sign_up', methods = ['GET', 'POST'])
def sign_up():
    if request.method == 'GET':
        return render_template('sign_up.html')
    else:
        if (check_content_type('application/x-www-form-urlencoded') or
            have_keys(request.form, {'name_signup',
                                     'email_signup',
                                     'password_signup',
                                     'datebirth_signup',
                                    'address_signup'})):
            return render_template('signup.html', error=True)
        name = request.form['name_signup']
        email = request.form['email_signup']
        password = request.form['password_signup']
        date = request.form['datebirth_signup']
        address = request.form['address_signup']
        add_user(name, email, password, date, address)
        return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/knowledgebase')
def knowledgebase():
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
    return redirect(url_for('login'))

@app.route('/allchat')
@login_required
def all_chat():
    chatrooms = {(name, room.id):[user.colour for user in room.users] for name, room in get_free_chatrooms(get_chatrooms()).items()}
    return "chatrooms"

@app.route('/chat/<int:id>', methods = ['GET', 'POST'])
@login_required
def chat(id):
    if request.method == 'GET':
        chatroom = get_chatroom_by_id(id)
        if not chatroom:
            abort(404)
        chatroom.users.append(current_user)
        current_user.chat_id = id
        return f'In chat {id}'
    else:
       chatroom = get_chatroom_by_id(id)
       message = request.data
       for word in flagged_word:
           if word in message:
               flag_to_moderator(current_user, message)
               break;
       chatroom.messages.append(message)
       send_message(current_user, message)
       return f'Posted Message in chat {id}'

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
