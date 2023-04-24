from App.models import *
from App.database import db

"""
Location controllers
"""

def add_location_log(user_id, latitude, longitude, logtext):
    new_log = LocationLog(user_id, latitude, longitude, logtext)
    db.session.add(new_log)
    db.session.commit()
    return new_log

def get_location_log(location_id):
    location_log = LocationLog.query.filter_by(id=location_id).first()
    if not location_log:
        return None
    return location_log

def get_all_location_logs():
    return LocationLog.query.all()

def get_all_location_logs_json(location_id):
    location_logs = get_all_location_logs()

    if not location_logs:
        return []
    location_logs = [location_logs.get_json() for location_log in location_logs]
    return location_logs

def delete_location_log(location_id):
    location_log = get_location_log(location_id)
    if location_log:
        db.session.delete(location_log)
        db.session.commit()