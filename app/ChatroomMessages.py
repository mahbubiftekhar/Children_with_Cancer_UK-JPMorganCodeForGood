from datetime import datetime
from app import database as db

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
