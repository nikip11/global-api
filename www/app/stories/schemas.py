from marshmallow import fields
from app.ext import ma

class StorySchema(ma.Schema):
  id = fields.Integer(dump_only=True)
  code = fields.String(required=True)
  title = fields.String(required=True)
  description = fields.String(required=False)
  cover = fields.String(required=True)
  url = fields.String(required=True)
  created_at = fields.DateTime(dump_only=True)
  updated_at = fields.DateTime(dump_only=True)
  
  
