class Chatroom():
    _id = 0
    def __init__(self):
        self.id = Chatroom._id + 1
        self.users = []
        self.messages = []

def auth(user, key):
    return True

def get_chatrooms():
    return []

def _get_free_chatroom(name):
    return Chatroom()

def get_free_chatrooms(chatrooms):
    return { name:_get_free_chatroom(name) for name in chatrooms }

def get_chatroom_by_id(id):
    return Chatroom()