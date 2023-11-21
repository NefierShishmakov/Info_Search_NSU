from ..extensions import db

class University(db.Model):
    __tablename__ = 'university'

    id = db.Column(db.Integer, primary_key=True)
    short_name = db.Column(db.String(15), nullable=False, unique=True)
    full_name = db.Column(db.String(300), nullable=False, unique=True)
    founding_date = db.Column(db.Date, nullable=False)

    students = db.relationship('Student', back_populates='university', cascade='save-update, merge, delete', passive_deletes=True)