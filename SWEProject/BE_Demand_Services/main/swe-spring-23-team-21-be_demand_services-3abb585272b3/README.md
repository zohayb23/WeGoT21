# Main Branch

## Purpose
The main branch represents the latest stable release of the project. Code that is on the main branch should be well-tested and ready for deployment. It is the branch that should be used for production releases.
This repository contains all Back End files needed for the TaaS platform project's demand-side services, such as logging in the plug-in user, reviewing services, creating and tracking orders, and so on

---

# Features
### Create Account
- Contains a flask app.py file allowing the user to create an account
### Delivery Class
- Contains the delivery class and unit tests for handling information on a vehicle delivery
### Login
- Contains a flask app.py file allowing the user to login and logout. Dependent on the user class
### Order Class
- Contains the order class and unit tests for handling information about a user's plug-in service order
### Payment Class
- Contains a preliminary payment class and unit tests for handling user payment information, will be expanded to interact with a payment services API when incorporated into the project scope
### Receiver Class
- Contains a flask app.py file allowing the creation and querying of the MySQL database for receiver information, a receiver class and unit tests for handling information about the recipient of a user's ordered delivery
### Track Order
- Contains a flask app.py file allowing the user to track the route of the vehicle assigned to the user's ordered delivery
### Update Class
- Contains the update class and unit tests for updating a user's ordered delivery details
### User All Features
- Contains a flask app.py file allowing the user to fully interact with account features, such as dashboard, create order, track order, and more. Dependent on the order and user classes
### User Class
- Contains the user class and unit tests for the creation, verification, and recipient setup for the user. Dependent on the receiver class
### Vehicle Demand Class
- Contains the vehicle class and unit tests for the creation and querying of vehicles stored in the MySQL database
### Order Tracking
- Contains a flask app.py file allowing the functionality of the track order page, connects with MapQuest to gather map data. Dependent on the order and user classes
### Vehicle Request With Order
- Contains a flask app.y file allowing a user's order to call the Supply-Side Vehicle Request API to assign a vehicle to an order

---

# Usage
## Before pushing commits or merging to main
- Only well-tested and stable code should be merged into the main branch.
- The main branch must be approved by the QA before any changes are made.
- Release tags should be created from the main branch to track specific releases.
- Perform the steps listed under **Integration Testing** prior to merging into the main branch
- **Refer to dev branch** for testing dimensions and benchmarks of feature branches

## Integration Testing
1. Clone the repository to your local machine following the instructions provided under **Cloning the main branch**
2. Merge branches on LOCAL repository, DO NOT PUSH the merged changes unless functionality is verified!
3. Run all unit tests for class files in the merged branch
4. Verify intended functionality: Ensure no part of the code breaks another

## Documentation
1. Back End Python files have comments describing the code
2. Comments should guide the reader towards intended functionality without them having to read through the code
3. Documentation for passing test cases is uploaded to Team 21's Google Drive

## Cloning the main branch
1. git clone [repository URL]
2. cd [repository name]
3. git checkout main
4. From there, you can work on the project, make changes, and push commits to the main branch.  However, it's important to note that code on the main branch should be stable and well-tested, so use it for production releases.

## Dependencies
### Flask, Flask-SQLAlchemy
- The back end uses flask app files for front end integration, it is needed to render front end templates and process user input
- This module is needed for the back end to interact with the relational MySQL database

Install:

		python3 -m pip install flask
	
Imports:
	
		from flask import Flask, jsonify, request, session, redirect, url_for, render_template, flash

---

## Contributors
- Jason Klipple (API integration, Back End Developer, & White box Tester)
- Anne Cuzeau (API integration, Back End Developer, & White box Tester)
- Gerardo Arguello (Database Integration, Back End Developer & White box Tester)
- Kayla Harris (Back End Developer & White box Tester)
- Zohayb Bhatti (Back End Developer & White box Tester)
- Eric Rodriguez (Back End Developer & White box Tester)
- Jacob Domingeuz (Back End Developer & White box Tester)
