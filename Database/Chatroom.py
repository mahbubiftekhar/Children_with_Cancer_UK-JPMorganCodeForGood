from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

class Chatroom(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(150), nullable = False)
	creationDate = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	lastUpdatedBy = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)

	colour = db.Column(db.String(150), nullable=False)
	chattype = db.Column(db.String(150), nullable=False)

	def __repr__(self):
        	return '<User %r>' % self.name

	def addNewChatroom(fname, fcreationDate, flastUpdatedBy, fcolour, fchattype):
		chat = Chatroom(name = fname, creationDate = fcreationDate, lastUpdatedBy = flastUpdatedBy, colour = fcolour, chattype = fchattype )
		db.session.add(chat)
		db.session.commit()
		return True
	def getChatroomById(fcid):
		return db.session.query(Chatroom).get(fcid)
	def deleteById(fcid):
		Chatroom.query.filter_by(id=fcid).delete()
		print("Deleted Chatroom with id " + str(fcid))

db.create_all()

print(Chatroom.addNewChatroom("Mahub", datetime.utcnow(), datetime.utcnow(),"Red", "typee"))
print(Chatroom.getChatroomById(1))
Chatroom.deleteById(2)

