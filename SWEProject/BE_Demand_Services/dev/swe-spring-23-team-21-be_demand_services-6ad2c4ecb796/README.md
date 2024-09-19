# Dev Branch

## Purpose
The dev branch is where active development takes place. This is the branch where features are added, bugs are fixed, and new code is written. It is a living branch that is constantly evolving as development work progresses.
Back End class files, associated unit tests, and flask app files will be initially pushed to an appropriate feature branch.
Once QA has certified the passing of all white box tests, a pull request can be opened for branching code to be merged into dev.

---

# Testing Criteria
Below is a list of requirements for code to satisfy before it can move on from dev:

## Unit Tests
1. Back End code passes all White Box unit test cases
2. Unit test code coverage is at least 80%
3. Test cases cover interactions between items from different branches, rather than each piece individually

## How to Test
1. Follow the instructions under **Copy code** in the **Usage** section to clone the repository to your local machine
2. Checkout the feature branch for the code you intend to test
3. Open the code file and its unit test file in VS Code (or similar Python IDE)
4. If it is not already installed, install the Coverage module to gather unit test code coverage metrics
Install with:
		
		python3 -m pip install coverage

5. In the terminal, execute the following commands:

		coverage run [filename.py]
		coverage report -m

This will report the coverage metrics, ensure coverage is at least 80%


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
To use the dev branch, clone the repository and switch to the dev branch using the following commands:

## Copy code
1. git clone [repository URL]
2. cd [repository name]
3. git checkout dev
4. From there, you can work on the project, make changes, and push commits to the dev branch. However, it's important to note that code on the dev branch may be in an unstable or unfinished state, so use it at your own risk.

## Merging into Dev
Before merging code into the dev branch, create a feature branch and open a pull request so that other team members can review the changes.
You must be passing all tests sent to you by the QA before pushing to the dev branch.
Please avoid pushing directly to the dev branch unless you have a very good reason to do so.
The dev branch is often used as the basis for creating release branches or tags, so it's important to keep it in good shape.

---

## Contributors
- Jason Klipple (API integration, Back End Developer, & White box Tester)
- Anne Cuzeau (API integration, Back End Developer, & White box Tester)
- Gerardo Arguello (Database Integration, Back End Developer & White box Tester)
- Kayla Harris (Back End Developer & White box Tester)
- Zohayb Bhatti (Back End Developer & White box Tester)
- Eric Rodriguez (Back End Developer & White box Tester)
- Jacob Domingeuz (Back End Developer & White box Tester)