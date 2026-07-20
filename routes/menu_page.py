""" 
Date: June-5-2026
menu_page.py
Purpose: Route for the menu page of the Good Days Coffee.

"""


from flask import Blueprint, render_template
from extensions import db
from models.menu_items import MenuItem
from routes.orders_items import orders_bp

# Blueprint for handling menu page routes
menu_bp = Blueprint('menu', __name__)




# Route for the menu page
@menu_bp.route('/menu')
def menu():
    # Fetch all menu items from the database
    menu_items = MenuItem.query.all()
    # render the menu template and pass the menu items to be displayed on the page
    return render_template('menu.html', menu_items=menu_items)






