from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    restaurant = db.Column(db.String(100), nullable=False)