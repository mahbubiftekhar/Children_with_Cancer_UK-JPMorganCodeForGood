from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/messages.db'
db = SQLAlchemy(app)

class Messages(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	message = db.Column(db.String(10050), nullable = False)
	sentUserID = db.Column(db.Integer, nullable=False)
	receivedUserID = db.Column(db.Integer, nullable=False)
	timestamp = db.Column(db.DateTime, nullable=False)

	def addMessage(mmessage, msentUserID, mreceivedUserID, mtimestamp):
		message = Messages(message = mmessage, sentUserID = msentUserID, receivedUserID = mreceivedUserID, timestamp = mtimestamp)
		db.session.add(message)
		db.session.commit()
		return True
	def getAllSentMessages(uid):
		return Messages.query.filter_by(sentUserID=uid).all()
	def getAllReceivedMessages(uid):
		return Messages.query.filter_by(receivedUserID=uid).all()

db.create_all() #Call this before doing any database stuff

print(Messages.addMessage("Hi, I heard you like candy. I bought some.", 1, 3, datetime.utcnow()))
print(Messages.getAllSentMessages(1))
print(Messages.getAllReceivedMessages(3))
