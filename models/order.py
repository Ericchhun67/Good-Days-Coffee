""" 
Date: June 19, 2026
order.py
Purpose: Model for handling order-related operations in the Good Days Coffee application.

"""


from flask_sqlalchemy import SQLAlchemy
from extensions import db





class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    menu_item_id = db.Column(db.Integer, db.ForeignKey('menu_item.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    status = db.Column(db.String(20), nullable=False, default='pending')

    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    menu_item = db.relationship('MenuItem', backref=db.backref('orders', lazy=True))

    @property
    def total_price(self):
        return self.menu_item.price * self.quantity

    def update_status(self, new_status):
        self.status = new_status

    
    def __repr__(self):
        return f'<Order User: {self.user.username}, MenuItem: {self.menu_item.name}, Quantity: {self.quantity}, Status: {self.status}>'
    
 
  
        
    
  
        
        

    
    

    
    
