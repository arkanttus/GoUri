from flask import Blueprint, make_response, jsonify
from ..app import Scrap

routes = Blueprint('routes', __name__)

@routes.route('/')
def teste():
   return Scrap.teste()

@routes.route('/scrap/<userId>', methods=['GET'])
def scrap(userId):
    return Scrap.scrap(userId)