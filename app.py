""" 
app.py
date: may 31, 2026
purpose: This file serves as the main entry point for the Good Days Coffee.
it initializes the flask application, sets up the database connection, 
and registers the various blueprints for handling different routes and 
functionalities.
"""



from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config, developmentConfig
from extensions import db
from routes.auth import auth_bp
from routes.pages import pages_bp
from routes.menu_page import menu_bp
from routes.favorite_item_page import favorite_bp
from routes.orders_items import orders_bp

app = Flask(__name__) # Initialize the Flask application
app.config.from_object(Config) # Load configuration settings from the Config
# settings

app.config.from_object(developmentConfig) # Load development-specific configuration settings,
# such as enabling debug mode 


# Start of the app function
def create_app() -> None:
    db.init_app(app) # Initialize the database with the flask app
    # Register blueprints for different routes and functionalities
    app.register_blueprint(pages_bp) 
    app.register_blueprint(auth_bp)
    app.register_blueprint(menu_bp)
    app.register_blueprint(favorite_bp)
    app.register_blueprint(orders_bp)

    # Create database tables if they don't exist
    with app.app_context():
        # Import models to ensure they are registered with SQLAlchemy before
        # creating tables
        from models.user import User
        from models.menu_items import MenuItem
        from models.order import Order
        from models.favorite_items import FavoriteItem
        db.create_all() # Create database tables based on the defined models
        
        
    # Return the initialized
    return app


# Run the application in debug mode when this script is executed directly
if __name__ == '__main__':
    app = create_app() # call the create_app function
    app.run(debug=True) # Start the flask development server with debug mode enabled
