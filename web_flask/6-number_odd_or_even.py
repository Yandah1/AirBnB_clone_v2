#!/usr/bin/python3
"""This script that starts a Flask web application"""
from flask import Flask


# Create an instance of the Flask class
app = Flask(__name__)
app.url_map.strict_slashes = False


# Define a route for the root path ("/")
@app.route('/')
def hello_hbnb():
    """display “Hello HBNB!" """
    return 'Hello HBNB!'


# Route for "/hbnb"
@app.route('/hbnb')
def display_hbnb():
    """ display hbnb page """
    return 'HBNB'


# Route for "/c/text"
@app.route('/c/<text>')
def c_text(text):
    """ replace underscore _ symbols with a space"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


# Route for "/python/<text>"
@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_text(text):
    """display “Python ”, followed by the value of the text"""
    text = text.replace('_', ' ')
    return 'python {}'.format(text)


# Route for "/number/<n>"
@app.route('/number/<int:n>')
def dislay_number(n):
    """display “n is a number”"""
    return '{} is a number'.format(n)


# Route for "/number_template/<n>"
@app.route('/number_template/<int:n>')
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template('5-number.html', n)


# Route for /number_odd_or_even/<n>
@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ display if number odd or even"""
    return render_template('6-number_odd_or_even.html', n=n, odd_even=('odd' if n % 2 != 0 else 'even'))


# Check if the script is executed directly (not imported as a module)
if __name__ == '__main__':
    """ Run the app on 0.0.0.0 and port 5000"""
    app.run(host='0.0.0.0', port=5000)
