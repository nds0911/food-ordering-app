from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Dish, Order_new

main = Blueprint('main', __name__)

@main.route('/')
def index():
    dishes = Dish.query.all()
    return render_template('index.html', dishes=dishes)

@main.route('/add_dish', methods=['GET', 'POST'])
def add_dish():
    if request.method == 'POST':
        name = request.form['name']
        restaurant = request.form['restaurant']
        new_dish = Dish(name=name, restaurant=restaurant)
        db.session.add(new_dish)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('add_dish.html')

@main.route('/place_order/<int:dish_id>', methods=['GET', 'POST'])
def place_order(dish_id):
    dish = Dish.query.get_or_404(dish_id)
    if request.method == 'POST':
        order_note = request.form['order_note']
        new_order = Order_new(order_note=order_note, dish=dish)
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('place_order.html', dish=dish)
