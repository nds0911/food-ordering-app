from flask import Blueprint, request, jsonify
from models import db, Dish

main = Blueprint('main', __name__)

@main.route('/dishes', methods=['GET'])
def get_dishes():
    dishes = Dish.query.all()
    return jsonify([{'id': dish.id, 'name': dish.name, 'restaurant': dish.restaurant} for dish in dishes])

@main.route('/dishes', methods=['POST'])
def add_dish():
    data = request.get_json()
    new_dish = Dish(name=data['name'], restaurant=data['restaurant'])
    db.session.add(new_dish)
    db.session.commit()
    return jsonify({'message': 'Dish added successfully'}), 201
