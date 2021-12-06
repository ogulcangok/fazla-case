from flask import Flask
from flask_cors import CORS
from flask_gzip import Gzip
from flask_login import LoginManager
from app.models import *

from app.config import Config
from app.api import api_bp
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView



def create_app():
    app = Flask(__name__)
    CORS(app)
    Gzip(app)
    app.secret_key = "super_secret_key"
    login = LoginManager(app)
    app.config.from_object(Config)
    db.init_app(app)
    db.create_all(app=app)
    admin = Admin(app,name="Admin Panel",template_mode="bootstrap3")
    admin.add_view(ModelView(User,db.session))
    admin.add_view(ModelView(Product, db.session))
    admin.add_view(ModelView(Shop, db.session))
    admin.add_view(ModelView(SearchLogs, db.session))
    @login.user_loader
    def user_loader(user_id):
        return User.query.filter_by(id=user_id).first()

    app.register_blueprint(api_bp)
    return app
