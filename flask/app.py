"""
This module runs the main Flask application.
"""

from flask import Flask #,render_template
# import mysql.connector
# import os

app = Flask(__name__)

@app.route('/')
def index():
    """Return a greeting from Flask."""
    return "Hello, Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
