import pymongo

def createChatrooms(name, creationDate, lastUpdated, image):
    '''
    print(">>>>1")
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    #db = client.chatrooms
    profile = mydb["chatrooms"]
    print(">>>>2")
    mydict = {"name": name, "creationDate": creationDate, "lastUpdated":lastUpdated,"image":image}
    print(">>>>>3")
    x = profile.insert_one(mydict)
    println(">>>>>4")
    print(x)
    '''
    myclient = pymongo.MongoClient(port=27017)
#    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mydatabase"]
    mycol = mydb["customers"]

    mydict = { "name": "John", "address": "Highway 37" }

    x = mycol.insert_one(mydict)
    print(x)

createChatrooms("Rusab", "019", "018", "image")



#def addToChatrooms():
