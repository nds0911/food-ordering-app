from flask import Blueprint, request, jsonify
from models import db, Order

main = Blueprint('main', __name__)

@main.route('/orders', methods=['GET'])
def get_orders():
    orders = Order.query.all()
    return jsonify([{'id': order.id, 'dish_id': order.dish_id, 'order_note': order.order_note} for order in orders])

@main.route('/orders', methods=['POST'])
def add_order():
    data = request.get_json()
    new_order = Order(dish_id=data['dish_id'], order_note=data['order_note'])
    db.session.add(new_order)
    db.session.commit()
    return jsonify({'message': 'Order added successfully'}), 201
