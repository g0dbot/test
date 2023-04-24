from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db
from flask import jsonify
from datetime import datetime


friends = db.Table('friends',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('friendship_id', db.Integer, db.ForeignKey('friendship.id'))
)

"""
User Models
"""
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    #for picture
    pic_url = db.Column(db.String(120), default='#')
    panic_mode = db.Column(db.Boolean, default=False)

    #for friend requests
    friendships = db.relationship('Friendship', secondary=friends, backref='users')

    #for location logs
    location_logs = db.relationship('LocationLog', backref='user', cascade='all, delete-orphan')
    current_location = db.relationship('LocationCurrent', uselist=False, backref='user', cascade='all, delete-orphan')
    home_location = db.relationship('LocationHome', uselist=False, backref='user', cascade='all, delete-orphan')

    def __init__(self, username, password, pic_url):
        self.username = username
        self.pic_url = pic_url
        self.panic_mode = False
        self.set_password(password)

    def __repr__(self):
        return f"User(id={self.id}, username='{self.username}', pic_url='{self.pic_url}')"

    def get_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'pic_url': self.pic_url
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def panic(self):
        self.panic_mode = True
    
    def safe(self):
        self.panic_mode = False