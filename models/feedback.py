""" 

Date: June-21, 2026

"""

from flask_sqlalchemy import SQLAlchemy
from extensions import db



class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f'<Feedback from {self.name} ({self.email})>'
    
    def feedback_info(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'message': self.message
        }
        
    def save_feedback(self):
        # Save the feedback to the database because the feedback is a new entry,
        # we need to add it to the session before committing the changes to the database
        db.session.add(self)
        db.session.commit() # Commit the changes to the database to save the new feedback entry
        
    
    
