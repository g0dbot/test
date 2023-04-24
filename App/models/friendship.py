from App.database import db
from flask import jsonify
from datetime import datetime

"""
Friendship Models
"""

class Friendship(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sender_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    receiver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    are_friends = db.Column(db.Boolean, default=False)

    def __init__(self, sender_id, receiver_id):
        self.receiver_id = receiver_id
        self.sender_id = sender_id
        self.are_friends = False

    def __repr__(self):
        return f"Friendship(id={self.id}, sender_id={self.sender_id}, receiver_id={self.receiver_id}, are_friends={self.are_friends})"

    def to_json(self):
        return {
            'id': self.id,
            'sender_id': self.sender_id,
            'receiver_id': self.receiver_id,
            'are_friends': self.are_friends
        }

    def status(self):
        return self.are_friends

    def confirm(self):
        self.are_friends = True
