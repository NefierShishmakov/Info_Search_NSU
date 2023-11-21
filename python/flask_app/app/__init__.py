from flask import Flask
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect

def create_app():
    app = Flask(__name__)
    app.config.from_prefixed_env()

    from .extensions import db, migrate
    db.init_app(app)
    migrate.init_app(app, db)

    csrf = CSRFProtect()
    csrf.init_app(app)

    from .blueprints.main.main import main as main_blue_print
    app.register_blueprint(main_blue_print)

    from .blueprints.auth.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .blueprints.students.students import students as students_blueprint
    app.register_blueprint(students_blueprint)

    from .blueprints.universities.universities import universities as universities_blueprint
    app.register_blueprint(universities_blueprint)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models.users import Users

    @login_manager.user_loader
    def load_user(id):
        return Users.query.get(id)

    return app