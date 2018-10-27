from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/userbadges.db'
db = SQLAlchemy(app)

class UserBadges(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	uid = db.Column(db.Integer, nullable = False)
	badgesID = db.Column(db.Integer, nullable = False)

	def addUserBadges(buid, bbadgesID):
		user_badge = UserBadges(uid = buid, badgesID = bbadgesID)
		db.session.add(user_badge)
		db.session.commit()
		return True
	
db.create_all()
#Functions tests
print(UserBadges.addUserBadges(1,4))




