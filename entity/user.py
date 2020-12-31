from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable = False)
    address = db.Column(db.String(128), index=True)
    image_url = db.Column(db.String(128), nullable=False)
