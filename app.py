from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from configs.config import Configuration
from secretKeys import secret_key
from flask_migrate import Migrate
app = Flask(__name__)
app.config.from_object(Configuration)
app.secret_key = secret_key
db = SQLAlchemy(app)
