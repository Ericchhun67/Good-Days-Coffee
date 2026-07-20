""" 
Date: june-5-2026
Purpose: this file defines the routes for the main pages of the Good Days coffee


"""



from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db
from models.feedback import Feedback
from models.user import User

# Blueprint for handling page routes
pages_bp = Blueprint('pages', __name__)

STORE_LOCATIONS = [
    {
        "name": "Good Days Coffee - Hayward",
        "address": "25800 Carlos Bee Blvd, Hayward, CA 94542",
        "lat": 37.6572,
        "lng": -122.0569,
        "hours": "Mon-Fri 7:00 AM - 6:00 PM"
    },
    {
        "name": "Good Days Coffee - Downtown",
        "address": "102 Main Street, Hayward, CA 94541",
        "lat": 37.6688,
        "lng": -122.0808,
        "hours": "Daily 7:00 AM - 8:00 PM"
    },
    {
        "name": "Good Days Coffee - Union City",
        "address": "321 Alvarado Niles Road, Union City, CA 94587",
        "lat": 37.5934,
        "lng": -122.0439,
        "hours": "Daily 8:00 AM - 7:00 PM"
    }
]

# Route for the home page
@pages_bp.route('/')
def index() -> str:
    return render_template('index.html')

# Route for the contact page
@pages_bp.route('/contact')
def contact() -> str:
    return render_template('contact.html')

# Route for the submit feedback form
@pages_bp.route('/submit-feedback', methods=['POST'])
def submit_feedback() -> str:
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # get the feedback data and save it to the database
    feedback = Feedback(name=name, email=email, message=message)
    feedback.save_feedback()
    return redirect(url_for('pages.contact'))


# Route for the about page
@pages_bp.route('/about')
def about() -> str:
    return render_template('about.html')

@pages_bp.route('/locations')
def locations() -> str:
    return render_template('locations.html')


@pages_bp.route('/api/locations')
def locations_api():
    return {"locations": STORE_LOCATIONS}
