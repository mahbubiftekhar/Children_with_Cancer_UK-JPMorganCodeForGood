import sqlite3
import datetime

def create_chatroom(name, creationDate, lastUpdatedBy,color, chattype):
	conn = sqlite3.connect('Chatroom.db')
 
	c = conn.cursor()
 
	
	c.execute('''
          CREATE TABLE IF NOT EXISTS Chatroom
          (cid INTEGER PRIMARY KEY, name VARCHAR(250), creationDate VARCHAR(250), lastUpdatedBy VARCHAR(250),
           color varchar(250), chattype VARCHAR(250))
          ''')
	c.execute('''INSERT INTO Chatroom(cid, name, creationDate, lastUpdatedBy, color,chattype) VALUES(?,?,?,?,?,?)''', (None,name, creationDate,lastUpdatedBy,color, chattype))
	conn.commit()
	c.execute("SELECT * FROM Chatroom")
	rows = c.fetchall()
	for row in rows:
		print(row)
	conn.commit()
	conn.close()

create_chatroom("Mahbub","NO", "NO", "color", "basic")
