from flask import Flask, render_template, request, flash
from werkzeug.exceptions import abort

from receiver import *
from user import *

app = Flask(__name__)


#This method will get all receiver info (Name and Email) with a corresponding ID, if said ID does not excist we abort the query
def get_receiver(receiver_id):
    
    receiver_info = getReceiverInfo(receiver_id)

    if receiver_info is None:
        abort(404)
    return receiver_info

## Methods get_receiverName and get_receiverEmail are commented out, but created in case they become needed

# def get_receiverName(receiver_id):
#     receiver_Name = getReceiverName(receiver_id)

#     if receiver_Name is None:
#         abort(404)
#     return receiver_Name

# def get_receiverEmail(receiver_id):
#     receiver_Email = getReceiverEmail(receiver_id)

#     if receiver_Email is None:
#         abort(404)
#     return receiver_Email

# @app.route('/<int:receiver_id')
# def receiver_info(receiver_id):
#     receiver_info = get_receiver(receiver_id)
#     return render_template('order.html', receiver_info=receiver_info)



# This method will allow for the creation of a new Receiver in our SQL Database by calling a funcion in the receiver_py.py
# The receiver will be populated with an automatically generated ID and the Name and Email will be collected from a form on the HTML order page
@app.route('/order', methods = ('GET', 'POST'))
def create_receiver():
    if request.method == 'POST':
        receiverName = request.form['Receiver Name']
        receiverEmail = request.form['Receiver Email']

    if not receiverName:
        flash('Receiver Name is required!')
    
    if not receiverEmail:
        flash('Receiver Email is required!')
    
    else:
        create_receiver(receiverName, receiverEmail)
    
    return render_template('Order.html')



@app.route('/Account', methods = ('GET', 'POST'))
def create_receiver():
    if request.method == 'POST':
        username = request.form['Username']
        password = request.form['User Password']
        name = request.form['User Name']
        email = request.form['User Email']
        phone = request.form['User Phone']

    if not username:
        flash('Username is required!')
    
    if not password:
        flash('Password is required!')

    if not name:
        flash('Name is required!')
    
    if not email:
        flash('Email is required!')

    if not phone:
        flash('Phone is required!')
    
    else:
        register(username, password, email, phone, name)
    
    return render_template('Account.html')