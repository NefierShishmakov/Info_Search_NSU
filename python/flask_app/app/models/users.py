from ..extensions import db

class Users(db.Model):
    login = db.Column(db.String(56), primary_key=True)
    password = db.Column(db.String(256), nullable=False)