from flask_sqlalchemy import SQLAlchemy
from extensions import db


class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique=True, nullable=False)
    description = db.Column(db.String(500), nullable=True)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50), nullable=False)  # e.g., 'Coffee', 'Tea', 'Pastry'
    image_filename = db.Column(db.String(250), nullable=True)  # URL for the menu item image
    
    def __repr__(self):
        return f'<MenuItem {self.name}>'
    
    
    
    def menu_item_details(self):
        return f'name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}, Category: {self.category}, Image: {self.image_filename}' 
    
    
    
    