from ..extensions import db

class Student(db.Model):
    __tablename__ = 'student'

    id = db.Column(db.Integer, primary_key=True)
    fio = db.Column(db.String(100), nullable=False, unique=True)
    birth_date = db.Column(db.Date, nullable=False)
    admission_year = db.Column(db.String(4), nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id', ondelete='CASCADE'), nullable=False, index=True)
    
    university = db.relationship("University", back_populates='students')