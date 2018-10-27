from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/chatroommessages.db'
db = SQLAlchemy(app)

class ChatroomMessages(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	chatroomID = db.Column(db.Integer)
	message = db.Column(db.String(10050), nullable = False)
	sentUserID = db.Column(db.Integer, nullable=False)
	timestamp = db.Column(db.DateTime, nullable=False)

	def addChatroomMessage(cchatroomID, cmessage, csentUserID, ctimestamp):
		cr_message = ChatroomMessages(chatroomID = cchatroomID, message = cmessage, sentUserID = csentUserID, timestamp = ctimestamp)
		db.session.add(cr_message)
		db.session.commit()
		return True
	def getChatroomMessages(cid):
		return ChatroomMessages.query.filter_by(chatroomID=cid)

db.create_all() #Call this before doing any database stuff
#Testing stuff
print(ChatroomMessages.addChatroomMessage(1,"Hi",4,datetime.utcnow()))
print(ChatroomMessages.getChatroomMessages(1))
