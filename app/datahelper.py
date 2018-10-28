from Badges import Badges
from Chatroom import Chatroom
from ChatroomMessages import ChatroomMessages
from Friends import Friends
from KnowledgeBase import KnowledgeBase
from Messages import Messages
from Profile import Profile
from UserBadges import UserBadges

from collections import defaultdict
import datetime

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

def _get_free_chatroom(chatttpe):
    candidates = chatrooms[chattype]
    if candidates:
        for candidate in candidates:
            if len(candidate.users) < 15:
                return candidate
    i = len(candidates)
    chatroom = Chatroom(f'{chattype}_{i}', datetime.utcnow(), 'dummy_colour', chattype)
    chatrooms[chattype].append(chatroom)
    return chatroom

def get_free_chatrooms(chatrooms):
    return { name:_get_free_chatroom(name) for name in chatrooms }

def get_chatroom_by_id(id):
    return Chatroom.getChatroomById(id)

def add_user(name, email, password, date, address):
    
