from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
from ...models.users import Users
from ...extensions import db

auth = Blueprint('auth', __name__, template_folder="templates")

@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.clear()

        login = request.form.get('login')
        if login:
            session['login'] = login

        password = request.form.get('password')
        remember = True if request.form.get('remember') else False
        if remember:
            session['remember'] = remember

        if not (login and password):
            flash("Not all fields are filled in")
            return redirect(url_for('auth.login'))
        
        user = Users.query.filter_by(login=login).first()

        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details and try again")
            return redirect(url_for('auth.login'))

        login_user(user, remember=remember)
        return redirect(url_for('main.index'))
    return render_template("auth/login.html")

@auth.route("/signup", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        session.clear()

        login = request.form.get('login')
        if login:
            session['login'] = login

        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')

        if not (login and password and confirm_password):
            flash("Not all fields are filled in")
            return redirect(url_for('auth.signup'))

        user = Users.query.filter_by(login=login).first()

        if user:
            flash("User with that login already exists", category="auth")
            return redirect(url_for('auth.signup'))
        
        if password != confirm_password:
            flash("Passwords are not the same")
            return redirect(url_for('auth.signup'))
        
        new_user = Users(login=login, password=generate_password_hash(password))

        db.session.add(new_user)
        db.session.commit()

        session.clear()
        return redirect(url_for('auth.login'))

    return render_template("auth/signup.html")


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))