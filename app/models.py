from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)  

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name =  db.Column(db.String(64), index=True, unique=True, nullable=False)
    number =  db.Column(db.Integer, unique=True, nullable=False)
    qtt =  db.Column(db.Integer)
    responsavel = db.Column(db.String(64))
    retornar = db.Column(db.Boolean)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return '<Item {}>'.format(self.name) 

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    Item_id = db.Column(db.Integer, db.ForeignKey('item.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

