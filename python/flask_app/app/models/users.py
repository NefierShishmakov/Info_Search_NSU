from flask_login import UserMixin
from ..extensions import db

class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(56), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)