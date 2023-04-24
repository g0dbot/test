from App.models import Friendship
from App.database import db

"""
Friendship controllers
"""
def get_friendship(sender_id, receiver_id):
    friendship = Friendship.query.filter_by(sender_id=sender_id, receiver_id=receiver_id).first()
    if not friendship:
        friendship = Friendship.query.filter_by(sender_id=receiver_id, receiver_id=sender_id).first()
        if not friendship:
            return None
    return friendship

def get_friendship_status(sender_id, receiver_id):
    friendship = get_friendship(sender_id, receiver_id)

    if not friendship:
        return False
    else:
        return friendship.status()
    
def add_friend(sender_id, receiver_id):
    request = get_friendship(sender_id, receiver_id)

    if not request:
        new_add_request = Friendship(sender_id, receiver_id)
        db.session.add(new_add_request)
        db.session.commit()
        return new_add_request
    elif not request.status():
        request.confirm()
        db.session.commit()
    return request

def delete_friend(sender_id, receiver_id):
    request = get_friendship(sender_id, receiver_id)
    db.session.delete(request)
    db.session.commit()

def get_all_friendships():
    return Friendship.query.all()

def get_all_friendships_json():
    friendships = Friendship.query.all()
    if not friendships:
        return []
    friendships = [friendships.get_json() for friendship in friendships]
    return friendships
