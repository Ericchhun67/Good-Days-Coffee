""" Favorite Menu Routes
this module contains the routes for the favorite menu feature of the CoffeeBucks application.



"""

from flask import Blueprint, render_template, request, redirect, url_for, session
from extensions import db
from models import User, FavoriteMenuItem



favorite_menu_bp = Blueprint('favorite_menu', __name__)



@favorite_menu_bp.route('/favorite_menu', methods=['GET', 'POST'])
def favorite_menu():
    pass