from flask import Flask, json, request, url_for, redirect, abort
import datahelper

app = Flask(__name__)

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
		return redirect(url_for("db"))
	else:
		return redirect(url_for("homepage"), error="login failed")
	return "login"


@app.route('/db')
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
