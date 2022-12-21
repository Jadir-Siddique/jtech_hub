from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime

class User(db.Model, UserMixin): # type: ignore  
    __tablename__ = 'user'
    name = db.Column(db.String(150)) 
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True)
    password = db.Column(db.String(150))
    phone = db.Column(db.Integer)

    def get_id(self):
        return (self.email)

class Product(db.Model):  # type: ignore  
    id = db.Column(db.Integer, primary_key = True)
    price = db.Column(db.Integer)
    description = db.Column(db.String(1000))
    stock = db.Column(db.Integer)


class Cart(db.Model):  # type: ignore  
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)
    user = db.relationship('User')
    product = db.relationship('Product')

class Order(db.Model): # type: ignore  
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer)
    user = db.relationship('User')
    product = db.relationship('Product')
    date = db.Column(db.DateTime(timezone=True), default=func.now())
