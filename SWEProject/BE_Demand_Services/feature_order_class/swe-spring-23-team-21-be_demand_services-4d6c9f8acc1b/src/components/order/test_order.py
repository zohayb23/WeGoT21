import unittest
from unittest.mock import patch
from datetime import datetime
from dotenv import dotenv_values
from order import Order

class TestOrder(unittest.TestCase):

    @patch('order.dotenv_values')
    def test_init(self, mock_dotenv):
        mock_dotenv.return_value = {'USERNAME': 'user', 'PWD': 'fakepassword'}
        order = Order()
        self.assertEqual(order._username, 'user')
        self.assertEqual(order._pwd, 'fakepassword')
        self.assertIsInstance(order._orderID, int)
        self.assertIsInstance(order._orderDatetime, datetime)
        self.assertGreaterEqual(order.orderID, 100)
        self.assertLessEqual(order.orderID, 10000)
        self.assertIsInstance(order._orderCode, int)
        self.assertIsInstance(order._pickUpLat, float)
        self.assertIsInstance(order._pickUpLong, float)
        self.assertIsInstance(order._dropOffLat, float)
        self.assertIsInstance(order._dropOffLong, float)
        self.assertIsInstance(order._totalCost, float)
    
    def test_orderID(self):
        order = Order()
        self.assertIsNotNone(order.orderID)

    def test_order_status(self):
        order = Order()
        self.assertEqual(order.orderStatus, "Processing")
        order.orderStatus = "Cancelled"
        self.assertEqual(order.orderStatus, "Cancelled")

    def test_pickUp_Lat(self):
        order = Order()
        self.assertEqual(order.pickUpLat, 0.0)
        order.pickUpLat = 123.45
        self.assertEqual(order.pickUpLat, 123.45)

    def test_pickUp_Long(self):
        order = Order()
        self.assertEqual(order.pickUpLong, 0.0)
        order.pickUpLong = 123.45
        self.assertEqual(order.pickUpLong, 123.45)
    
    def test_dropOff_Lat(self):
        order = Order()
        self.assertEqual(order.dropOffLat, 0.0)
        order.dropOffLat = 123.45
        self.assertEqual(order.dropOffLat, 123.45)

    def test_dropOff_Long(self):
        order = Order()
        self.assertEqual(order.dropOffLong, 0.0)
        order.dropOffLong = 123.45
        self.assertEqual(order.dropOffLong, 123.45)
    
    def test_register_order(self):
        order = Order()
        # Call the register_order method
        wentThrough = order.place_order()

        # Assert that the method returned a dictionary that is not empty
        assert len(order.place_order()) > 0, "Dictionary is empty"