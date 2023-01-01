from flask import Flask

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


#db = SQLAlchemy()

app = Flask(__name__)

from .views import admin_bp
app.register_blueprint(admin_bp)

#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

#db.init_app(app)