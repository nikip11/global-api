from flask import request
from flask_restful import Resource
from app.common.error_handling import ObjectNotFound
from .schemas import UserSchema
from .models import User

user_schema = UserSchema()

class UserResource(Resource):

    def get(self, id):
        user = User.query.get_or_404(id)
        if user is None:
          raise ObjectNotFound('User not found')
        return user_schema.dump(user)

    def post(self):
        data = request.get_json()
        user_dict = user_schema.load(data)
        user = User(**user_dict)
        user.save()
        return user_schema.dump(user), 201

    def put(self, id):
        user = User.query.get_or_404(id)
        user_schema.load(request.json, instance=user)
        return user_schema.dump(user)

    def delete(self, id):
        user = User.query.get_or_404(id)
        user.delete()
        return '', 204

class UserListResource(Resource):

    def get(self):
        users = User.query.all()
        return user_schema.dump(users, many=True)

    def post(self):
        data = request.get_json()
        user_dict = user_schema.load(data)
        user = User(**user_dict)
        user.save()
        return user_schema.dump(user), 201