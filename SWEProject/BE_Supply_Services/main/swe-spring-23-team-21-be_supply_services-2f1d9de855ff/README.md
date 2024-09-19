# Main Branch

## Purpose
The main branch represents the latest stable release of the project. Code that is on the main branch should be well-tested and ready for deployment. It is the branch that should be used for production releases.
This repository contains all Back End files needed for the TaaS platform project's supply-side services, such as logging in the Fleet Manager, viewing vehicle and fleet data, viewing and setting vehicle flags, and so on

---

# Features
### Fleet Manager Login
- Contains the user class that will store the account data of the Fleet Manager, and interact with the database for logging in, creating accounts, and resetting passwords
### Supply-Side Object Classes
- Contains flag, fleet, manager, plugin, recording, and vehicle classes with associate unit tests. Contains a flask app.py file for rendering templates from Supply Front End and processing user data on those pages

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
### PyMongo
- This module is needed for the back end to interact with the non-relational MongoDB database

Install:
	
		python3 -m pip install pymongo
	
Imports:
	
		from pymongo import MongoClient
		from pymongo.errors import DuplicateKeyError
	
### Flask
- The back end uses flask app files for front end integration, it is needed to render front end templates and process user input

Install:

		python3 -m pip install flask
	
Imports:
	
		from flask import Flask, jsonify, request, session, redirect, url_for, render_template, flash

---

## Contributors
- Jason Klipple (Database integration & API Developer)
- Anne Cuzeau (Remote environment hosting & API integration)
- Gerardo Arguello (Back End Developer & White box Tester)
- Zohayb Bhatti (Back End Developer & White box Tester)
