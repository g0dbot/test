from App.database import db
from flask import jsonify
from datetime import datetime

"""
Location Models
"""
class Location(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"Location(user_id={self.user_id}, id={self.id}, latitude={self.latitude}, longitude={self.longitude}, date_created={self.date_created})"

    def to_json(self):
        return {
            'user_id': self.user_id,
            'id': self.id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'date_created': self.date_created.isoformat()
        }

    def __init__(self, user_id, latitude, longitude):
        self.user_id = user_id
        self.latitude = latitude
        self.longitude = longitude
        self.date_created = datetime.utcnow()


class LocationLog(Location):
    logtext = db.Column(db.String(180), nullable=True)

    def __repr__(self):
        return f"LocationLog(user_id={self.user_id}, id={self.id}, latitude={self.latitude}, longitude={self.longitude}, date_created={self.date_created}, logtext={self.logtext})"

    def to_json(self):
        json = super().to_json()
        json['logtext'] = self.logtext
        return json

    def __init__(self, user_id, latitude, longitude, logtext):
        super().__init__(user_id, latitude, longitude)
        self.logtext = logtext


class LocationHome(Location):
    is_home = db.Column(db.Boolean, nullable=False)

    def __repr__(self):
        return f"LocationHome(user_id={self.user_id}, id={self.id}, latitude={self.latitude}, longitude={self.longitude}, date_created={self.date_created}, is_home={self.is_home})"

    def to_json(self):
        json = super().to_json()
        json['is_home'] = self.is_home
        return json

    def __init__(self, user_id, latitude, longitude, is_home):
        super().__init__(user_id, latitude, longitude)
        self.is_home = is_home


class LocationCurrent(Location):
    def __repr__(self):
        return f"LocationCurrent(user_id={self.user_id}, id={self.id}, latitude={self.latitude}, longitude={self.longitude}, date_created={self.date_created})"

    def to_json(self):
        return super().to_json()

    def __init__(self, user_id, latitude, longitude):
        super().__init__(user_id, latitude, longitude)