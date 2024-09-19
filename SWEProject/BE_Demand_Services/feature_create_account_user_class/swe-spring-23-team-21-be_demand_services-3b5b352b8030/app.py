# APP.PY FOR CREATE ACCOUNT PAGE

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv() 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    phone_number = db.Column(db.String(20), nullable=True)
    name = db.Column(db.String(120), nullable=True)
    service_type = db.Column(db.String(120), nullable=True) 

@app.route('/', methods=['POST', 'GET']) # Use "methods" instead of "method"
def create_account():
    if request.method == 'POST':
        # Getting data from request
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        phone_number = request.form.get('phone_number', None)
        name = request.form.get('name', None)
        service_type = request.form.get('service_type', None)

        # Creating user obj
        user = User(username=username, email=email, password=password,
                    phone_number=phone_number, name=name, service_type=service_type)

        try:
            # Add to DB
            db.session.add(user)
            db.session.commit()
            
            return redirect('/account-home') # direct to account home page
        except:
            return "Error: Couldn't create account"
        
    else:
        return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)