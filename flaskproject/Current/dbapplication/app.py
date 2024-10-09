from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import psycopg2
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

conn = psycopg2.connect("dbname=flasktutorialdb user=postgres password=sheng1129 host=localhost")

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sheng1129@localhost:5432/flasktutorialdb'
    app.secret_key = 'SOME KEY'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    @login_manager.unauthorized_handler
    def unauthrized_callback():
        return redirect(url_for('index'))
    
    bcrypt = Bcrypt(app)

    from routes import register_routes
    register_routes(app, db, bcrypt)

    migrate = Migrate(app, db)

    return app
