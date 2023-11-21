from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_required
from ...models.university import University
from ...extensions import db

universities = Blueprint('universities', __name__, template_folder="templates")

@universities.route("/universities")
def list_universities():
    universities_list = University.query.order_by(University.short_name).all()
    return render_template("universities/universities.html", universities_list=universities_list)

@universities.route("/universities/add", methods=['GET', 'POST'])
@login_required
def add_university():
    if request.method == 'POST':
        session.clear()

        short_name = request.form.get('short_name')
        if short_name:
            session['short_name'] = short_name

        full_name = request.form.get('full_name')
        if full_name:
            session['full_name'] = full_name

        founding_date = request.form.get('founding_date')
        if founding_date:
            session['founding_date'] = founding_date

        if not (short_name and full_name and founding_date):
            flash("Not all fields are filled in")
            return redirect(url_for('universities.add_university'))

        university = University.query.filter_by(short_name=short_name).first()

        if university:
            flash(f"The university with short name {short_name} already exists")
            return redirect(url_for('universities.add_university'))
        
        new_university = University(short_name=short_name, full_name=full_name, founding_date=founding_date)
        db.session.add(new_university)
        db.session.commit()

        session.clear()
        return redirect(url_for('universities.list_universities'))

    return render_template("universities/add_university.html")


@universities.route("/universities/edit/<int:id>", methods=['GET', 'POST'])
@login_required
def edit_university(id):
    university_to_edit = University.query.get(id)

    if request.method == 'POST':
        session.clear()

        short_name = request.form.get('short_name')
        if short_name:
            session['short_name'] = short_name

        full_name = request.form.get('full_name')
        if full_name:
            session['full_name'] = full_name

        founding_date = request.form.get('founding_date')
        if founding_date:
            session['founding_date'] = founding_date

        if not (short_name and full_name and founding_date):
            flash("Not all fields are filled in")
            return redirect(f"/universities/edit/{id}")
        
        try:
            University.query.filter_by(id=id).update({"short_name": short_name, "full_name": full_name, "founding_date": founding_date})
            db.session.commit()
        except:
            flash(f"The university with short name {short_name} already exists")
            return redirect(f"/universities/edit/{id}")
        
        session.clear()
        return redirect(url_for('universities.list_universities'))

    return render_template("universities/edit_university.html", university=university_to_edit)


@universities.route("/universities/delete/<int:id>")
@login_required
def delete_university(id):
    University.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect(url_for('universities.list_universities'))