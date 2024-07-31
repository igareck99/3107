from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.config import Configuration
from config.secretKeys import secret_key
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(Configuration)
app.secret_key = secret_key
db = SQLAlchemy(app)
migrate = Migrate(app, db)
