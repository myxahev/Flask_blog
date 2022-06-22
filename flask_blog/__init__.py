from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_blog.config import Config
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()
bcrypt = Bcrypt()

def create_app():
    print(__name__)
    app = Flask(__name__)

    from flask_blog.main.routes import main
    from flask_blog.users.routes import users

    app.register_blueprint(main)
    app.config.from_object(Config)
    login_manager.init_app(app)
    bcrypt.init_app(app)
    app.register_blueprint(users)

    return app

