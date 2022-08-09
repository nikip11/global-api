
from flask import request
from flask_restful import Resource
from app.common.error_handling import ObjectNotFound
from .schemas import StorySchema
from .models import Story

story_schema = StorySchema()

class StoryListResource(Resource):

    def get(self):
        stories = Story.query.all()
        return story_schema.dump(stories, many=True)

    def post(self):
        data = request.get_json()
        story_dict = story_schema.load(data)
        story = Story(**story_dict)
        story.save()
        return story_schema.dump(story), 201

class StoryResource(Resource):

    def get(self, id):
        story = Story.query.get_or_404(id)
        if story is None:
            raise ObjectNotFound('Story not found')
        return story_schema.dump(story)

    def put(self, id):
        story = Story.query.get_or_404(id)
        story_schema.load(request.json, instance=story)
        return story_schema.dump(story)

    def delete(self, id):
        story = Story.query.get_or_404(id)
        story.delete()
        return '', 204