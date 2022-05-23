from pickle import TRUE
from sqlalchemy import true
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model,UserMixin):
    id =db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(150),unique=True)
    password=db.Column(db.String(150))
    name=db.Column(db.String(150),unique=TRUE)
    regno=db.Column(db.Integer,unique=True)
    phno=db.Column(db.String(15))
    city=db.column(db.String(25))
    books=db.relationship('Book')
    
    


class Book(db.Model):
    id =db.Column(db.Integer,primary_key=True)
    bookname=db.Column(db.String(40))
    author=db.Column(db.String(40))
    edition=db.Column(db.String(40))
    genre=db.Column(db.String(40))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
