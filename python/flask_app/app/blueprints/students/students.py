from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_required
from ...extensions import db
from ...models.student import Student
from ...models.university import University

students = Blueprint('students', __name__, template_folder="templates")

@students.route("/students")
def list_students():
    students_list = Student.query.order_by(Student.fio).all()
    return render_template("students/students.html", students_list=students_list)

@students.route("/students/add", methods=['GET', 'POST'])
@login_required
def add_student():
    universities = University.query.all()

    if request.method == 'POST':
        session.clear()

        fio = request.form.get('fio')
        if fio:
            session['fio'] = fio

        birth_date = request.form.get('birth_date')
        if birth_date:
            session['birth_date'] = birth_date

        admission_year = request.form.get('admission_year')
        if admission_year:
            session['admission_year'] = admission_year

        university_id = int(request.form.get('university_id'))
        if university_id:
            session['university_id'] = university_id

        if not (fio and birth_date and admission_year and university_id):
            flash("Not all fields are filled in")
            return redirect(url_for('students.add_student'))
        
        student = Student.query.filter_by(fio=fio).first()

        if student:
            flash(f"The student with {fio} already exists")
            return redirect(url_for('students.add_student'))
        
        try:
            int(admission_year)
        except ValueError:
            session.pop('admission_year')
            flash("The admission year must be integer and 4 characters in length")
            return redirect(url_for('students.add_student'))
        
        new_student = Student(fio=fio, birth_date=birth_date, admission_year=admission_year, university_id=university_id)
        db.session.add(new_student)
        db.session.commit()

        session.clear()
        return redirect(url_for('students.list_students'))
    
    return render_template("students/add_student.html", universities=universities)

@students.route("/students/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit_student(id):
    student_to_edit = Student.query.get(id)
    universities = University.query.all()

    if request.method == 'POST':
        session.clear()

        fio = request.form.get('fio')
        if fio:
            session['fio'] = fio

        birth_date = request.form.get('birth_date')
        if birth_date:
            session['birth_date'] = birth_date

        admission_year = request.form.get('admission_year')
        if admission_year:
            session['admission_year'] = admission_year

        university_id = int(request.form.get('university_id'))
        if university_id:
            session['university_id'] = university_id

        if not (fio and birth_date and admission_year and university_id):
            flash("Not all fields are filled in")
            return redirect(f"/students/edit/{id}")
        
        try:
            int(admission_year)
        except ValueError:
            session['admission_year'] = student_to_edit.admission_year
            flash("The admission year must be integer")
            return redirect(f"/students/edit/{id}")
        
        try:
            Student.query.filter_by(id=id).update({"fio": fio, "birth_date": birth_date, "admission_year": admission_year, "university_id": university_id})
            db.session.commit()
        except:
            flash(f"The student with {fio} already exists")
            return redirect(f"/students/edit/{id}")

        session.clear()
        return redirect(url_for('students.list_students'))
    
    return render_template("students/edit_student.html", student=student_to_edit, universities=universities)


@students.route("/students/delete/<int:id>")
@login_required
def delete_student(id):
    Student.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('students.list_students'))