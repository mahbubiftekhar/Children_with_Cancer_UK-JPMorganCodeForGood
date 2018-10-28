from datetime import datetime
from app import database as db

class Chatroom(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(150), nullable = False)
	creationDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	lastUpdate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	colour = db.Column(db.String(150), nullable=False)
	chattype = db.Column(db.String(150), nullable=False)

	def __repr__(self):
        	return '<Chatroom %r>' % self.name

	def addNewChatroom(fname, fcreationDate, flastUpdate, fcolour, fchattype):
		chat = Chatroom(name = fname, creationDate = fcreationDate, lastUpdate = flastUpdate, colour = fcolour, chattype = fchattype )
		db.session.add(chat)
		db.session.commit()
		return chat

	def getAllTypes():
		return set(chatroom.chattype for chatroom in Chatroom.query.all())

	def getChatroomById(fcid):
		return db.session.query(Chatroom).get(fcid)

	def deleteById(fcid):
		Chatroom.query.filter_by(id=fcid).delete()
		print("Deleted Chatroom with id " + str(fcid))

db.create_all()
