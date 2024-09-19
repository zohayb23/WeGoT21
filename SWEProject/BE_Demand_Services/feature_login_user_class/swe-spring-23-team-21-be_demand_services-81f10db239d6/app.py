from flask import Flask, render_template, request, session, redirect, url_for
import os
from user import User
from dotenv import load_dotenv

app = Flask(__name__, template_folder="templates")
app.secret_key = os.environ.get("SECRET_KEY")

load_dotenv()

# Create a User object with the required parameters
user = User()

@app.route("/")
def index():
    if session.get("username"):
        return redirect(url_for("dashboard"))
    
    else:
        return render_template("login.html")
    return render_template("home.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if user.login_user(username, password):
        session["username"] = username
        return redirect(url_for("dashboard"))

    return render_template("home.html", error="Invalid credentials.")

@app.route("/dashboard")
def dashboard():
    if session.get("username"):
        return render_template("dashboard.html", username=session["username"])
    return redirect(url_for("index"))

@app.route("/logout", methods=["POST", "GET"])
def logout():
    session.pop("username", None)
    return render_template("home.html")

#DO NOT USE!!!! FOR TESTING PURPOSES ONLY
@app.route('/register', methods=['GET'])
def register():
    username = 'test'
    password = 'test123'

    # Check if the username already exists
    if user.create_user(username, password):
        message = 'Username already exists'
    else:
        # Create the new user
        user.create_user(username, password)
        message = 'User created successfully'

    return render_template('dashboard.html', message=message)

if __name__ == "__main__":
    app.run(debug=True)
