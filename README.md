Good Days Coffee

Good Days Coffee is a Flask coffee shop web app built as a learning project. It includes menu browsing, category filtering, user authentication, favorites, orders/cart actions, contact feedback, and a locations map page.

## Features

- Home, About, Contact, Menu, Orders, Favorites, Login, and Register pages
- Menu items stored in SQLite with Flask-SQLAlchemy
- Menu category filters for coffee, tea, lemonade, breakfast, and lunch
- Menu item images loaded from the `static/img` folder
- Add to Cart flow for creating test orders
- Edit, cancel, update status, and simple payment actions for orders
- Favorites page with add/remove favorite actions
- Register, login, logout, and profile routes
- Contact feedback form saved to the database
- Locations page with a Leaflet/OpenStreetMap map and `/api/locations` endpoint
- Docker setup for running the app in a container

## Tech Stack

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Jinja templates
- HTML/CSS/JavaScript
- Leaflet/OpenStreetMap
- Docker

## Project Structure

```text
coffeebucks/
├── app.py
├── config.py
├── extensions.py
├── models/
│   ├── favorite_items.py
│   ├── feedback.py
│   ├── menu_items.py
│   ├── order.py
│   └── user.py
├── routes/
│   ├── auth.py
│   ├── favorite_item_page.py
│   ├── menu_page.py
│   ├── orders_items.py
│   └── pages.py
├── static/
│   ├── img/
│   └── styles.css
├── templates/
├── requirements.txt
├── Dockerfile
└── compose.yaml
```

## Getting Started

Clone the repository:

```bash
git clone https://github.com/Ericchhun67/coffeebucks.git
cd coffeebucks
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the app:

```bash
python3 app.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000
```

## Docker

Build and run with Docker Compose:

```bash
docker compose up --build
```

Then open:

```text
http://127.0.0.1:5000
```

## Database

This project uses SQLite through Flask-SQLAlchemy.

The database is created in the `instance/` folder. Tables are created with:

```python
db.create_all()
```

Menu items were added using database seeding and Flask shell practice.

Example seed pattern:

```python
for item in menu_lunch:
    existing_item = MenuItem.query.filter_by(name=item["name"]).first()

    if not existing_item:
        db.session.add(MenuItem(**item))

db.session.commit()
```

## Learning Notes

This project is still a learning project, so a few parts are intentionally simple:

- Orders and favorites currently use a test `user_id = 1` in some routes.
- The cart/payment flow is a beginner version, not a real payment processor.
- Some data is seeded manually while learning Flask-SQLAlchemy.
- Authentication is being built with Flask sessions.

## Future Improvements

- Connect orders and favorites to the logged-in user session
- Improve profile dropdown behavior
- Add real cart quantities and drink sizes
- Add better form validation and flash messages
- Add admin tools for adding menu items without using Flask shell
- Improve responsive styling
- Add tests
