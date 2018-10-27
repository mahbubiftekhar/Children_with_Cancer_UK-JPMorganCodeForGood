from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/knowledgebase.db'
db = SQLAlchemy(app)

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
#Functions tests
print(KnowledgeBase.addKnowledgeBase("The psychology of sid","A distrubed human being in need of medical attension ASAP"))
print(KnowledgeBase.getKnowledgeBaseInfo(1))
print(KnowledgeBase.deleteKnowledge(1))




