*Scope*

This module contains a class called Order which represents an order made by a customer. The Order class has attributes such as orderID, orderDatetime, orderStatus, orderCode, totalCost, pickUpLat, pickUpLong, dropOffLat and dropOffLong. It also has methods to check if the orderID already exists, place an order, and register the order in the database.
Dependencies

This module has the following libraries:

    dotenv
    mysql.connector
    datetime
    os
    random

*Installation*

To install the required dependencies, run the following command:

    pip install python-dotenv mysql-connector-python

*Usage*

To use the Order class, first import it:

    python: from order import Order

To create an instance of the Order class:

    python: order = Order()

To place an order:

    order.place_order()

To set the orderStatus attribute:

    order.orderStatus = "Delivered"

To get the orderID attribute:

    orderID = order.orderID

*Files*

order.py: A separate module that defines the Order class.
test_order.py: unit tests

*Testing*

This module has unit tests passing.