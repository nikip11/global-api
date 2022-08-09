from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import create_access_token, create_refresh_token
from flask_jwt_extended import get_jwt_identity, create_access_token, create_refresh_token, jwt_required
from flask_jwt_extended import unset_jwt_cookies
from app.common.error_handling import ObjectNotFound
from .schemas import UserSchema
from  .models import User
    
user_schema = UserSchema()

class UserResource(Resource):
    
    @jwt_required()
    def get(self, id):
        user = User.query.get_or_404(id)
        if user is None:
          raise ObjectNotFound('User not found')
        return user_schema.dump(user)

    @jwt_required()
    def put(self, id):
        user = User.query.get_or_404(id)
        user_schema.load(request.json, instance=user)
        return user_schema.dump(user)

    @jwt_required()
    def delete(self, id):
        user = User.query.get_or_404(id)
        user.delete()
        return '', 204

class UserListResource(Resource):

    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        print(current_user)
        users = User.query.all()
        return user_schema.dump(users, many=True)

    @jwt_required()
    def post(self):
        data = request.get_json()
        user_dict = user_schema.load(data)
        user = User(**user_dict)
        user.save()
        return user_schema.dump(user), 201

class LoginResource(Resource):
    
        def post(self):
            data = request.get_json()
            user = User.query.filter_by(email=data['email']).first()
            if user is None:
                raise ObjectNotFound('User not found')
            if not user.check_password(data['password']):
                raise ObjectNotFound('Password is incorrect')
            access_token = create_access_token(identity=user_schema.dump(user))
            refresh_token = create_refresh_token(identity=user_schema.dump(user))
            return jsonify({"token": access_token, "refresh_token": refresh_token, "user": user_schema.dump(user)})

class LogoutResource(Resource):

    @jwt_required()
    def get(self):
        response = jsonify({'message':"Successfully Logged Out"}) 
        unset_jwt_cookies(response)
        return response