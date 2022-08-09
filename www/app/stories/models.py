from app.db import db, BaseModelMixin

class Story(db.Model, BaseModelMixin):
  __tablename__ = 'stories'
  id = db.Column(db.Integer, primary_key=True)
  code = db.Column(db.String(10), nullable=False, unique=True)
  title = db.Column(db.String(50), nullable=False)
  description = db.Column(db.String(50), nullable=False, default = '')
  cover = db.Column(db.String(100), nullable=False)
  url = db.Column(db.String(100), nullable=False)
  created_at = db.Column(db.DateTime, default=db.func.now())
  updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
  
  def __init__(self, code, title, description, cover, url):
    self.code = code
    self.title = title
    self.description = description if description else ''
    self.cover = cover
    self.url = url
  
  def __str__(self):
    return 'Story %r' % self.title

  def __repr__(self):
    return '<Story %r>' % self.title