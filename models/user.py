""" 
Date: June-7-2026
Purpose: the user.py
users model database table for the login and registration system of the 
Good Days coffee website.

"""

from flask_sqlalchemy import SQLAlchemy
from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

# User model for the database, representing users of the website
class User(db.Model):
    # id: unique identifier for each user, primary key in the database
    id = db.Column(db.Integer, primary_key=True)
    # Username: unique username for each user, cannot be null
    username = db.Column(db.String(150), unique=True, nullable=False)
    # Email: unique email address for each user, cannot be null
    email = db.Column(db.String(150), unique=True, nullable=False)
    # Password: hashed password for each user, cannot be null
    password = db.Column(db.String(256), nullable=False)
    
    

    def __repr__(self):
        return f'<User {self.username}>'
    

    def user_info(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }
        
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
        
    def check_password(self, password):
        # check if the provided password matches the stored hashed password
        if not self.password:
            return False
        return check_password_hash(self.password, password)
    
    
    def update_email(self, new_email):
        self.email = new_email
        db.session.commit()
        return self.email
    
    def update_username(self, new_username):
        # check if the new username is already taken by another user
        existing_user = User.query.filter_by(username=new_username).first()
        if existing_user and existing_user.id != self.id:
            raise ValueError("Username already taken. Please choose another.")
        self.username = new_username
        db.session.commit()
        return self.username
    
        
    
