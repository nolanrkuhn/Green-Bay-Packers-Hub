import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from config import Config

load_dotenv()
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
csrf = CSRFProtect()
migrate = Migrate()

login_manager.login_view = 'auth.login'  
login_manager.login_message_category = 'info'  


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.routes.home import home_bp
        from app.routes.auth import auth_bp
        from app.routes.players import players_bp
        from app.routes.stats import stats_bp
        from app.routes.favorites import favorites_bp

        app.register_blueprint(home_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(players_bp)
        app.register_blueprint(stats_bp)
        app.register_blueprint(favorites_bp)

    return app

@login_manager.user_loader
def load_user(user_id):

    from app.models import User
    return User.query.get(int(user_id))


