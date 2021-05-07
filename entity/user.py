from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable = False)
    user_name = db.Column(db.String(64), nullable = False)
    address = db.Column(db.String(128), index=True)
    image_url = db.Column(db.String(128), nullable=False)
    api_key = db.Column(db.String(64), unique=True, index=True)
