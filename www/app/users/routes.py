from flask import Blueprint
from flask_restful import Api
from .resources import UserResource, UserListResource

users_blueprint = Blueprint('users', __name__)

api = Api(users_blueprint)

api.add_resource(UserResource, '/users/<int:id>')

api.add_resource(UserListResource, '/users')
