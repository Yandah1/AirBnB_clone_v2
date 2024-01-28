#!/usr/bin/python3
"""Starts a Flask web application.
    /hbnb: HBnB home page.
"""
from models import storage
from flask import Flask
from flask import render_template
from models.state import State


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display a page similar to the AirBnB clone project."""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return render_template("100-hbnb.html",
                           states=states, amenities=amenities, places=places)


@app.teardown_appcontext
def teardown(exc):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
