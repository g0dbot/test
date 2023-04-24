from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from flask_login import login_required
from App.models import db
from App.controllers import add_location_log, get_all_location_logs_json

location_views = Blueprint('index_views', __name__, template_folder='../templates')

@location_views.route('/location', methods=['POST'])
@login_required
def location_logging():
    data = request.json
    message = add_location_log(data)
