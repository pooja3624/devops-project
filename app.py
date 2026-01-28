# Task 1: Demo Flask Application
# Date: 21/03/2024
# File Name: app.py
# Author Name: M. Venkateswarl

# Import Flask and OS Python modules
from flask import Flask, render_template
import os

# Create the application object by calling Flask constructor
app = Flask(__name__)

# Map the URL request to the response
@app.route('/')
def home():
    """
    Generate HTML response to the user
    from the templates folder
    """
    return render_template('index.html')

# Control and start the execution of the application
# using __name__ dunder method which always has
# the fixed value "__main__"
if __name__ == "__main__":

    # Get the port number of the web server (default: 5000)
    port = int(os.environ.get('PORT', 5000))

    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=port)