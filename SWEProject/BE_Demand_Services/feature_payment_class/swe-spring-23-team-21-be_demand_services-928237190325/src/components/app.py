from flask import Flask, render_template, request, flash
import order, payment
from MS import mapquest

app = Flask(__name__)

@app.route('/')
def verify_payment():
     # Initialize Payment object, currently placeholder with dummy values
     # In the future will take in data from a form
    payment_obj = payment(0, 'Credit Card', 0, 50.00, 0, 00000000, None, 'Pending')
    flash(payment_obj.VerifyPayment())
    # Currently no templates to render for payment services, this return value is likely temporary
    return payment_obj.UpdateStatus()

@app.route('/', methods = ('GET','POST'))
def register_order():
    # Initialize Order object to pass values from order page form
    order_obj = order()
    if request.method == 'POST':
        pickup_addr = request.form['origin']
        dropoff_addr = request.form['destination']
        # Calls to MapQuest API to get lat/long from addresses
        ms_obj = mapquest()
        pickup_loc = ms_obj.convert_address_to_mapquest_geocoords(pickup_addr)
        dropoff_loc = ms_obj.convert_address_to_mapquest_geocoords(dropoff_addr)
        
        order_obj._pickUpLat = pickup_loc[0]
        order_obj._pickUpLong = pickup_loc[1]
        order_obj._dropOffLat = dropoff_loc[0]
        order_obj._dropOffLong = dropoff_loc[1]
        order_obj.place_order()
        return render_template('labsampleorder.html')
    else:
        return "Please fill out each item with your information."
    