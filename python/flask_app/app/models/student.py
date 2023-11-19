from ..extensions import db

class Student(db.Model):
    fio = db.Column(db.String(100), primary_key=True)
    birth_date = db.Column(db.Date, nullable=False)
    admission_year = db.Column(db.String(4), nullable=False)
    univ_short_name = db.Column(db.String(15), db.ForeignKey("university.short_name"), nullable=False)
    university = db.relationship("University", backref=db.backref('student', lazy=True))