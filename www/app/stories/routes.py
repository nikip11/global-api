from flask import Blueprint
from flask_restful import Api
from .resources import StoryResource, StoryListResource

stories_blueprint = Blueprint('stories', __name__)
api = Api(stories_blueprint)

api.add_resource(StoryResource, '/stories/<int:id>')
api.add_resource(StoryListResource, '/stories')