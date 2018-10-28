from datetime import datetime
from app import database as db

class Profile(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(150), nullable = False)
	level = db.Column(db.String(150), nullable=False)
	username = db.Column(db.String(150), nullable=False)
	colour = db.Column(db.String(150), nullable=False)
	date_of_birth = db.Column(db.DateTime,nullable=False)
	password = db.Column(db.String(150), nullable=False) #This is stored in plaintext for now
	chatroomID = db.Column(db.Integer, nullable = False)

	@property
	def is_active(self):
		return True

	@property
	def is_authenticated(self):
		return True

	@property
	def is_anonymous(self):
		return False

	def get_id(self):
		return self.session_token

	def __repr__(self):
        	return '<User %r>' % self.email

	def addProfile(pemail, plevel,pusername ,pcolour,pdate_of_birth, ppassword, pchatroomID):
		profile = Profile(email = pemail, level = plevel,username = pusername, colour = pcolour,date_of_birth = pdate_of_birth, password = ppassword, chatroomID = pchatroomID)
		db.session.add(profile)
		db.session.commit()
		return True
    
	def getUserWithEmail(email):
		return Profile.query.filter_by(email=email).first()

	def getUserDetails(uid):
		return db.session.query(Profile).get(uid)

	def deleteUserDetails(uid):
		Profile.query.filter_by(id=uid).delete()
		print("Deleted Profile with id " + str(uid))

	@staticmethod
	def auth(uid, key):
		first_var = Profile.query.filter_by(id=uid).first()
		if ( (first_var.id == uid) &  (first_var.password == key)):
			return True
		return False
	
db.create_all()
Profile.addProfile("a@b.c", 'Moderator', 'Name', 'Red', datetime.utcnow(), 'q', 3)
