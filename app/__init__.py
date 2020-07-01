# Initialize Flask app
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)

# Setup config object

app.config.from_object(Config)

# Setup database and ORM

db = SQLAlchemy(app)

# Add db migrations

migrate = Migrate(app, db)


login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'

from app import routes, models
