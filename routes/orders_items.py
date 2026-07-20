"""
Date: June 19, 2026
orders-items.py
Purpose: Routes for handling order-related operations in the Good Days Coffee application.

"""


from flask import Blueprint, request, render_template, redirect, session, url_for
from extensions import db
from models.order import Order
from models.menu_items import MenuItem
from models.user import User
from models.favorite_items import FavoriteItem


orders_bp = Blueprint('orders', __name__)



@orders_bp.route('/orders')
def get_all_orders():
    user_id = 1 
    
    order = Order.query.filter_by(user_id=user_id).all()
    
    return render_template('orders.html', orders=order)



@orders_bp.route('/orders/edit/<int:order_id>', methods=['GET', 'POST'])
def edit_order(order_id):
    order = Order.query.get_or_404(order_id)
    
    if request.method == 'POST':
        new_quantity = request.form.get('quantity')
        
        # Validate the new quantity items order status
        if order.status in ['pending', 'confirmed']:
            order.quantity = int(new_quantity)
            db.session.commit()
            return redirect(url_for('orders.get_all_orders'))
        else:
            # if the order is not in a state that allows editing, return an error messages
            return "Error: Cannot edit order with status '{}'".format(order.status), 400
    return render_template('edit_order.html', order=order)



# route for updating order status
@orders_bp.route('/orders/update_status/<int:order_id>', methods=['POST'])
def update_order_status(order_id):
    order = Order.query.get_or_404(order_id)
    
    new_order_status = request.form.get('status')
    # check if the new order status is valid and if the order is in a state that allows status updates
    if new_order_status in ['pending', 'confirmed', 'canceled', 'completed']:
        # update the new order status
        order.update_status(new_order_status)
        db.session.commit() # commit the changes to the database
        return redirect(url_for('orders.get_all_orders'))
    else:
        return "Error: Invalid order status", 400


@orders_bp.route('/orders/cancel/<int:order_id>', methods=['POST'])
def cancel_order(order_id):
    order = Order.query.get_or_404(order_id)

    if order.status in ['pending', 'confirmed']:
        order.update_status('canceled')
        db.session.commit()
        return redirect(url_for('orders.get_all_orders'))

    return "Error: Cannot cancel order with status '{}'".format(order.status), 400


@orders_bp.route('/orders/payment/<int:order_id>', methods=['POST'])
def payment(order_id):
    order = Order.query.get_or_404(order_id)

    if order.status == 'pending':
        order.update_status('completed')
        db.session.commit()
        return redirect(url_for('orders.get_all_orders'))

    return "Error: Cannot pay for order with status '{}'".format(order.status), 400
    
    
# route for adding to cart menu
@orders_bp.route('/add_to_cart/<int:menu_item_id>', methods=['POST'])
def add_to_cart(menu_item_id):
    """ 
    1. Check if the user is logged in
    2. get menu_item_id from form
    3. create order/order item with the menu item and quantity
    4. commit the order to the database
    5. redirect to the orders page
    """
    # check post request if the user is logged in 
    user_id = 1
    menu_item = MenuItem.query.get(menu_item_id)
    if not user_id:
        return redirect(url_for('auth.login')) # Redirect to the login page if user is not logged in
    
    
    if menu_item:
        # create a new order with the menu item and quantity cancel order status
        new_order = Order(user_id=user_id, menu_item_id=menu_item_id, quantity=1, status='pending')
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('orders.get_all_orders'))
    else:
        return "Error: Menu item not found", 404
    return redirect(url_for('menu.menu'))

# payment route
