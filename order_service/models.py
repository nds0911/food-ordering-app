from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    dish_id = db.Column(db.Integer, db.ForeignKey('dish.id'), nullable=False)
    order_note = db.Column(db.Text, nullable=False)
    dish = db.relationship('Dish', backref=db.backref('orders', lazy=True))