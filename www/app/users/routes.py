from flask import Blueprint
from flask_restful import Api
from .resources import UserResource, UserListResource
from .resources import LoginResource, LogoutResource

users_blueprint = Blueprint('users', __name__)
api = Api(users_blueprint)

api.add_resource(UserResource, '/users/<int:id>')
api.add_resource(UserListResource, '/users')
api.add_resource(LoginResource, '/login')
api.add_resource(LogoutResource, '/logout')
