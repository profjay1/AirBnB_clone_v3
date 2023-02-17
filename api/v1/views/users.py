#!/usr/bin/python3
'''Contains the users view for the API.'''
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route('/users', methods=['GET'], strict_slashes=False)
def users():
    """Retrieves the list of all User objects"""
    objs = storage.all(User)
    return jsonify([obj.to_dict() for obj in objs.values()])


@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def single_user(user_id):
    """Retrieves a User object"""
    obj = storage.get(User, user_id)
    if not obj:
        abort(404)
    return jsonify(obj.to_dict())
