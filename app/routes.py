from flask import Blueprint, jsonify

routes = Blueprint('routes', __name__)

@routes.route('/<username>')
def teste(username):
    response = {'koe': 'teste', 'user': username}
    return jsonify(response)
