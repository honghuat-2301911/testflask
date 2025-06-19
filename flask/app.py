"""
This module runs the main Flask application.
"""

from flask import Flask, render_template
import os

app = Flask(__name__, template_folder='../templates')


@app.route('/')
def index():
    """Render the index.html template."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
