from datetime import datetime
from app import database as db

class KnowledgeBase(db.Model):
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	title = db.Column(db.String(150), nullable = False)
	describe = db.Column(db.String(1000), nullable=False)



	def addKnowledgeBase(ktitle, kdescribe):
		kb = KnowledgeBase( title = ktitle,describe= kdescribe)
		db.session.add(kb)
		db.session.commit()
		return True
	def getKnowledgeBaseInfo(kid):
		return db.session.query(KnowledgeBase).get(kid)
	def deleteKnowledge(kid):
		KnowledgeBase.query.filter_by(id=kid).delete()
		print("Deleted Knowledge Base with id " + str(kid))

	
db.create_all()




