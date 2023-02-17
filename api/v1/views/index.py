#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """
    Returns a JSON response containing the status of the API.

    HTTP Method:
      - GET

    Returns:
      - A JSON object with a single "status" key set to "OK".

    Example:
      ```
      >>> import requests
      >>> response = requests.get('http://localhost:5000/api/v1/status')
      >>> response.json()
      {'status': 'OK'}
      ```
    """
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    Returns a JSON response containing the count of all objects by class.

    HTTP Method:
      - GET

    Returns:
      - A JSON object with keys for each class name and values for the count of objects of that class.

    Example:
      ```
      >>> import requests
      >>> response = requests.get('http://localhost:5000/api/v1/stats')
      >>> response.json()
      {
          'amenities': 10,
          'cities': 5,
          'places': 20,
          'reviews': 15,
          'states': 2,
          'users': 100
      }
      ```
    """
    if request.method == 'GET':
        response = {}
        PLURALS = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in PLURALS.items():
            response[value] = storage.count(key)
        return jsonify(response)

