from app.db import db, BaseModelMixin

class User(db.Model, BaseModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    
    def __str__(self):
        return 'User %r' % self.name
    
    def __repr__(self):
        return '<User %r>' % self.name