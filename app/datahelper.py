from Badges import Badges
from Chatroom import Chatroom
from ChatroomMessages import ChatroomMessages
from Friends import Friends
from KnowledgeBase import KnowledgeBase
from Messages import Messages
from Profile import Profile
from UserBadges import UserBadges

from collections import defaultdict
from datetime import datetime

chatrooms = defaultdict(list)

def auth(email, key):
    user = Profile.getUserWithEmail(email)
    if user == None:
        return None
    if user.password != key:
        return None
    return user

def get_chatrooms():
    return Chatroom.getAllTypes()

def _get_free_chatroom(chattype):
    candidates = chatrooms[chattype]
    if candidates:
        for candidate in candidates:
            if len(getattr(candidate, 'users', 0)) < 15:
                return candidate
    chatroom = Chatroom.addNewChatroom(f'{chattype}', datetime.utcnow(), datetime.utcnow(), 'Red', chattype)
    chatroom.users = []
    chatrooms[chattype].append(chatroom)
    return chatroom

def get_free_chatrooms(chatrooms):
    return { name:_get_free_chatroom(name) for name in chatrooms }

def get_chatroom_by_id(id):
    return Chatroom.getChatroomById(id)

def add_user(name, email, password, date, address):
    Profile.addProfile(email, 'Child', name, 'Red', datetime.utcnow(), password, 0)


#Chatroom.addNewChatroom('Leukemia', datetime.now(), datetime.now(), "WOWO", "Leukemia")
#Chatroom.addNewChatroom('Leukemia', datetime.now(), datetime.now(), "WOWO", "Leukemia1")
#Chatroom.addNewChatroom('Leukemia', datetime.now(), datetime.now(), "WOWO", "Leukemia2")
