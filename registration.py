# Date: 21/03/2024
# File Name: app.py
# Author Name: M. Venkateswarl

# Import Flask and OS Python modules
from flask import Flask, render_template, request, redirect, url_for
import os

# Create Flask application
app = Flask(__name__)

# Home page route
@app.route("/")
def home():
    return render_template("Registration.html")

# Register route (GET & POST)
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        # Here you can store user data in a database or file
        # (Example: print data)
        print(name, email, password)

        return render_template("Success.html")

    return redirect(url_for("home"))

# Main execution
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)