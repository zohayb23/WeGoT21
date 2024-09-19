from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import os
import requests
import json
from dotenv import dotenv_values
from datetime import datetime
from user import User
from order import Order
from flask_cors import CORS

from dotenv import load_dotenv

app = Flask(__name__, template_folder="templates")
app.secret_key = os.environ.get("SECRET_KEY")
CORS(app)

load_dotenv()

# Create a User object with the required parameters
user = User()


@app.route("/")
def index():
    if session.get("username"):
        return redirect(url_for('dashboard'))
    else:
        return render_template("home.html")

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/services")
def services():
    return render_template("services.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    if username == None:
        return render_template("login.html", error="")
    
    if user.login_user(username, password):
        session["username"] = username
        # Order history
        orders = user.get_all_orders_by_userID(username)
        #My Account details
        email = user.get_user_email(session["username"])
        if email == None:
            email = ''
        else:
            try:
                email = email[0]  # get first element of tuple
            except:
                email = ''
        phone = user.get_user_phone(session["username"])
        if phone == None:
            phone = ''
        else:
            try:
                phone = phone[0]  # get first element of tuple
            except:
                phone = ''
        if orders == None:
            orders = ['', '', '', '', '']
        return render_template("dashboard.html", username=session["username"], orders=orders, email=email, phone=phone)
    else:
        return render_template("login.html", error="Username and/or password incorrect")

@app.route("/dashboard")
def dashboard():
    if session.get("username"):
        #remove orderID from session
        session.pop("orderId", None)

        # Order history
        username = session.get("username")
        orders = user.get_all_orders_by_userID(username)
       
        #My Account details
        email = user.get_user_email(session["username"])
        if email == None:
            email = ''
        else:
            try:
                email = email[0]  # get first element of tuple
            except:
                email = ''
        phone = user.get_user_phone(session["username"])
        if phone == None:
            phone = ''
        else:
            try:
                phone = phone[0]  # get first element of tuple
            except:
                phone = ''
        if orders == None:
            orders = ['', '', '', '', '']
        return render_template("dashboard.html", username=session["username"], orders=orders, email=email, phone=phone)
    return redirect(url_for("index"))

#Logout user
@app.route("/logout", methods=["POST", "GET"])
def logout():
    #remove orderID and username from session
    session.pop("orderId", None)
    session.pop("username", None)
    return render_template("home.html")

#Register a new user
@app.route('/register', methods=["POST", "GET"])
def register():
    message =  ""
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        email = request.form.get("email")
        phone = request.form.get("number")

        # Check if the username already exists
        if user.user_already_exists(username) == True:
            message = 'Username already exists, please choose another username'
        else:
            # Create the new user
            user.create_user(username, password, email, phone)
            if user.create_user(username, password, email, phone):
                #redirect to Dashboard
                session["username"] = username
                return redirect(url_for("dashboard"))
            else:
                 message = 'One of the fields is wrong, please try again'

    return render_template('register.html', error=message)

#reset Pwd
@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    # Get the username and new password from the request
    username = session.get("username")
    new_password = request.form.get('new_password')
        
    try:
        user.reset_password(username, new_password)
        # Return a success message to the user
        return render_template("reset_password.html", message = 'Password reset successfully.')

    except:
        # Return an error message to the user
        return render_template("reset_password.html", message = '')
    


#Place an order
@app.route("/order", methods=["POST", "GET"])
def order():
    message = ''
    if request.method == "GET":
        return render_template("order.html", message = message)
    if request.method == "POST":
        origin = request.form.get('origin')
        dest = request.form.get('destination')
        dateDelivery = request.form.get('dateDelivery')
        username = session.get("username")
        if not origin or not dest:
            message = 'Please enter a valid origin and destination'
            return render_template("order.html", message=message)
        if not dateDelivery:
            message = 'Please enter a date'
            return render_template("order.html", message=message)
        if origin is not None and dest is not None:
            #Get mapkey
            api_key = os.environ.get('MAPQUEST_API_KEY')

            #Convert pickup address to coordinates
            url = f'http://www.mapquestapi.com/geocoding/v1/address?key={api_key}&location={origin}'
            response = requests.get(url)
            data = json.loads(response.text)
            if data['results'] and data['results'][0]['locations']:
                pulat = data['results'][0]['locations'][0]['latLng']['lat']
                pulng = data['results'][0]['locations'][0]['latLng']['lng']
            else:
                pulat = 0
                pulng = 0

            #Convert delivery address to coordinates
            url = f'http://www.mapquestapi.com/geocoding/v1/address?key={api_key}&location={dest}'
            response = requests.get(url)
            data = json.loads(response.text)
            if data['results'] and data['results'][0]['locations']:
                dellat = data['results'][0]['locations'][0]['latLng']['lat']
                dellng = data['results'][0]['locations'][0]['latLng']['lng']
            else:
                dellat = 0
                dellng = 0

            # Create an instance of the Order class
            order = Order(username)
            #Set P.Up add & lat and long
            order.pickUpLat = pulat
            order.pickUpLong = pulng
            order.pickupAddress = origin

            #Set Delivery add & lat and long
            order.dropOffLat = dellat
            order.dropOffLong = dellng
            order.deliveryAddress = dest

            #Set order delivery 
            order.orderDeliveryDate = dateDelivery

            #Register order
            placeorder = order.place_order()
            if placeorder == {}:
                message = 'Something went wrong and the order was not placed. Please try again.'
                return render_template("order.html", message = message, username = username)
            else:
                orderId = order.order_Id
                session['orderId'] = orderId
                order = Order(username)
                order_dict = order.get_order_details(orderId)
                # Define the data to send
                data = {
	                "dropoff_location": dest,
	                "pickup_location": origin,
	                "order_id": orderId
                }
                # Send the data to the supply-side Flask app
                try:
                    response = requests.post('https://swesupply2023team21.xyz/request', json=data)
                    #leaving for debugging
                    vehicle_data = response.json()
                    vehicle_id = vehicle_data['vehicle_id']
                    #Render tracking page
                    return render_template("tracking.html", orderId=orderId, order=order_dict)
                except:
                    message = 'Your order was placed, but no vehicles are available at this time. Please be patient or contact our support for more details.'
                    return render_template("order.html", message = message)
    return render_template("order.html", message = message)

#Track new order after placing
@app.route('/tracking', methods=["POST", "GET"])
def tracking():
    #Get username and orderId from session 
    username = session.get("username")
    orderId = session.get("orderId")
    order = Order(username)
    order_dict = order.get_order_details(orderId)
    
    # Return a dict with the order details
    if order_dict != {}:
        return render_template("tracking.html", orderId=orderId, order=order_dict)
    else:
        #date is hard coded to avoid 'out of range year' or 'nonetype' error
        order_dict = {'pickupAddress': '', 'deliveryAddress': '', 'orderStatus': '','orderPlaced': datetime(2013, 10, 31, 18, 23, 29, 227)}
        return render_template("tracking.html", orderId=orderId, order = order_dict, message = 'No order details for this order.')

@app.route('/track_order/<order_id>', methods=['GET', 'POST'])
def track_order(order_id):
    username = session.get("username")
    session["orderId"] = order_id
    # Use the order ID to look up the order details in the database
    order = Order(username)
    order_dict = order.get_order_details(order_id)
    # Return a dict with the order details
    if order_dict != {}:
        return render_template("tracking.html", orderId=order_id, order=order_dict)
    else:
        #date is hard coded to avoid 'out of range year' or 'nonetype' error
        order_dict = {'pickupAddress': '', 'deliveryAddress': '', 'orderStatus': '','orderPlaced': datetime(2013, 10, 31, 18, 23, 29, 227)}
        return render_template("tracking.html", orderId=order_id, order = order_dict, message = 'No order details for this order.')


#gets route between the pickup (origin) and dropoff (destination)
#CAllED BY: route.js
@app.route('/mapRoute', methods=['GET','POST'])
def mapRoute():
    if request.method == "GET":
        env_vars = dotenv_values(".env")
        apiKey= env_vars.get("MAPQUEST_API_KEY")

        #Get username and orderId from session 
        username = session.get("username")
        orderId = session.get("orderId")
        order = Order(username)
        order_dict = order.get_order_details(orderId)

        #Get origin and destination from dictionary
        if order_dict != {}:
            origin = order_dict.get('pickupAddress')
            dest = order_dict.get('deliveryAddress')

        else:
            origin = ''
            dest=''
        # Return the origin adn dest as a JSON response
        return jsonify({'origin': origin, 'dest':dest})
    return False

#API kei retrieval
@app.route('/api/mapquest_key')
def mapquest_key():
    # returns API Key when called
    env_vars = dotenv_values(".env")
    apiKey= env_vars.get("MAPQUEST_API_KEY")
    return {'key':apiKey}

if __name__ == "__main__":
    app.run(host='0.0.0.0')
