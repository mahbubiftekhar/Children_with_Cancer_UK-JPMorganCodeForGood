from datetime import datetime
from app import database as db

class Badges(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	badgeName = db.Column(db.String(150), nullable = False)
	description = db.Column(db.String(1150), nullable=False)

	def addBadges(bbadgeName, bdescription):
		badges = Badges(badgeName = bbadgeName, description = bdescription)

		db.session.add(badges)
		db.session.commit()
		return True
	def getBadge(bid):
		return db.session.query(Badges).get(bid)
	
db.create_all()




