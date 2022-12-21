from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import Migrate
from flask_login import LoginManager

db=SQLAlchemy()
DB_NAME = "website.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "hello"
    app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://root@localhost/website"
    db.init_app(app)
    migrate = Migrate()
    migrate.init_app(app,db)


    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User 

    with app.app_context(): # This is needed to create the database
        db.create_all()
        print('Created Database!')

    login_manager = LoginManager(app)
    login_manager.login_view = 'auth.login' # type: ignore
    login_manager.init_app(app)
    @login_manager.user_loader
    def load_user(email):
        user = User.query.filter_by(email=email).first()
        return user
        
    return app



