from ..extensions import db

class University(db.Model):
    short_name = db.Column(db.String(15), primary_key=True)
    full_name = db.Column(db.String(300), nullable=False)
    founding_date = db.Column(db.Date, nullable=False)