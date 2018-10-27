from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/login')
def login():
    return "login "

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
