
#Scope
This is a simple Flask app that allows users to authenticate and access a dashboard. The app uses a User class from a separate module to handle user-related functionality such as user validation and user creation.
*Create user method for testing purposes only*
*Templates for testing purposes only*

#Requirements

    Flask
    Python 3.x

#Libraries: 
    certifi
    bcrypt
    os
    random
    dotenv
    datetime import datetime
    mysql-connector-python

#Usage

    The app has a homepage where the user can enter their credentials to login.
    The user is redirected to a dashboard page after successful authentication.
    The user can log out of the app by clicking on the logout button in the dashboard.
    The user can register using a separate /register endpoint (for testing purposes only).
    The app checks for duplicate usernames during registration and prevents their creation.


#Files

    app.py: The main Flask app.
    user.py: A separate module that defines the User class.
    templates: A directory containing HTML templates for the app.
    static: A directory containing static assets for the app.