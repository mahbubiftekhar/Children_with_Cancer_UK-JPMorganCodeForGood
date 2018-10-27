from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/profile.db'
db = SQLAlchemy(app)

class Profile(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(150), nullable = False)
	level = db.Column(db.String(150), nullable=False)
	username = db.Column(db.String(150), nullable=False)
	colour = db.Column(db.String(150), nullable=False)
	date_of_birth = db.Column(db.DateTime,nullable=False)
	password = db.Column(db.String(150), nullable=False) #This is stored in plaintext for now
	chatroomID = db.Column(db.Integer, nullable = False)

	def __repr__(self):
        	return '<User %r>' % self.email

	def addProfile(pemail, plevel,pusername ,pcolour,pdate_of_birth, ppassword, pchatroomID):
		profile = Profile(email = pemail, level = plevel,username = pusername, colour = pcolour,date_of_birth = pdate_of_birth, password = ppassword, chatroomID = pchatroomID)
		db.session.add(profile)
		db.session.commit()
		return True
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
#Functions tests
print(Profile.addProfile("dog@hotmail.com","Moderator","jpmorganrox","Red",datetime.utcnow(),"password",3))
print(Profile.addProfile("human@hotmail.com","Moderator","plzhiremeh","Red",datetime.utcnow(),"notpassword",5))
print(Profile.getUserDetails(1))
print(Profile.auth(1,"notpassword")) #Should return false
print(Profile.auth(1,"password"))
print(Profile.deleteUserDetails(1))




