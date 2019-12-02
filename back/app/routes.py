from flask import Blueprint, make_response, jsonify, request
from ..app import Scrap

routes = Blueprint('routes', __name__)

@routes.route('/')
def teste():
   return Scrap.teste()

@routes.route('/scrap', methods=['POST'])
def scrap():
   users = request.get_json()
   print('users :' , users)
   return Scrap.scrap(users)