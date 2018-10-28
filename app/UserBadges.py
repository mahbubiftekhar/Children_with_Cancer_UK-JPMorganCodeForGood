from datetime import datetime
from app import database as db

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




