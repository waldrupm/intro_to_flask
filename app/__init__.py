# Initialize Flask app
from flask import Flask
app = Flask(__name__)

# Setup config object
from config import Config
app.config.from_object(Config)

# Setup database and ORM
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

# Add db migrations
from flask_migrate import Migrate
migrate = Migrate(app, db)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from app import routes, models