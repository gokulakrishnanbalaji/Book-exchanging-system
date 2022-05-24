from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager


db=SQLAlchemy()
DB_NAME="database.db"



def create_app():
    app=Flask(__name__)
    app.config['SECRET_KEY']='kjbncbvoiwhjapoj jng'

    #app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] ='postgres://cfmbjmrkxwwikh:cc5c9658779a94f180dd471c39d459b79f44f09c1852c48384bbff6988fe615c@ec2-54-204-56-171.compute-1.amazonaws.com:5432/dcs1i9m790t2jo'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views,url_prefix='/')
    app.register_blueprint(auth,url_prefix='/')

    from .models import User, Book
    create_database(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('Created Database!')

