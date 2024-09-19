from flask import Flask, render_template, request, session, redirect, url_for, jsonify
import requests
import unittest
from unittest.mock import patch
from order import Order
from datetime import datetime
from demandWeGo import app
import random

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_index_redirect(self):
        with app.test_client() as client:
            # create a session with a test username
            with client.session_transaction() as session:
                session['username'] = 'testuser'
            
            # send GET request to '/'
            response = client.get('/')
            
            # assert that the response redirects to dashboard
            assert response.status_code == 302
            
            # remove the session
            with client.session_transaction() as session:
                session.pop('username', None)
                
            # send GET request to '/'
            response = client.get('/')
            
            # assert that the response renders the login.html template
            assert response.status_code == 200


    def test_home(self):
        response = self.client.get("/home")
        self.assertEqual(response.status_code, 200)

    def test_services(self):
        response = self.client.get("/services")
        self.assertEqual(response.status_code, 200)

    def test_login_successful(self):
        with patch('demandWeGo.user.login_user', return_value=True):
            response = self.client.post('/login', data=dict(
                username="test",
                password="test123"
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_login_unsuccessful(self):
        with patch('demandWeGo.user.login_user', return_value=False):
            response = self.client.post('/login', data=dict(
                username="testuser",
                password="wrongpassword"
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_dashboard_with_username_in_session(self):
        with self.client as client:
            with client.session_transaction() as sess:
                sess['username'] = 'test'
            response = self.client.get("/dashboard")
            self.assertEqual(response.status_code, 200)

    def test_dashboard_without_username_in_session(self):
        response = self.client.get("/dashboard", follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        with self.client as client:
            with client.session_transaction() as sess:
                sess['username'] = 'test'
            response = self.client.get("/logout", follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_register_successful(self):
        with patch('demandWeGo.user.create_user', return_value=True):
            random_number = random.randint(0, 30)
            username_test = 'testuser' + str(random_number)
            response = self.client.post('/register', data=dict(
                username= username_test,
                password="test123",
                email= None,
                number=None
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_register_unsuccessful(self):
        with patch('demandWeGo.user.user_already_exists', return_value=True):
            response = self.client.post('/register', data=dict(
                username="test",
                password="test123",
            ), follow_redirects=True)
            self.assertEqual(response.status_code, 200)

    def test_order_page_loads(self):
        with self.client as client:
            with client.session_transaction() as sess:
                sess['username'] = 'test'
            response = self.client.get("/order")
            self.assertEqual(response.status_code, 200)

    def test_order_success(self):
        # Test successful order placement
        data = {
            'origin': 'New York, NY',
            'destination': 'San Francisco, CA',
            'dateDelivery': '2023-05-01'
        }
        response = self.client.post('/order', data=data)
        self.assertEqual(response.status_code, 200)

    def test_order_failure(self):
        # Test failed order placement
        data = {
            'origin': 'New York, NY',
            'destination': '',
            'dateDelivery': '2023-05-01'
        }
        response = self.client.post('/order', data=data)
        self.assertEqual(response.status_code, 200)

    def test_map_route(self):
        with app.test_request_context('/mapRoute'):
            # Set up a fake session with username and orderId
            with self.client.session_transaction() as session:
                session['username'] = 'test_user'
                session['orderId'] = 12345
            
            # Make a GET request to /mapRoute
            response = self.client.get('/mapRoute')

            # Check that the response is successful (200 status code)
            self.assertEqual(response.status_code, 200)

    def test_track_order(self):
        # Set up a fake session with username and orderId
            with self.client.session_transaction() as session:
                session['username'] = 'test'
                session['orderId'] = 3

            # Set up a mock order ID
            order_id = '3'

            # Make a GET request to the route with the mock order ID
            response = self.client.get(f'/track_order/{order_id}')

            # Check that the response code is 200
            self.assertEqual(response.status_code, 200)

    def test_tracking_get(self):
        # Set up session with username and orderId
        with self.client.session_transaction() as session:
            session['username'] = 'test'
            session['orderId'] = 12
        # Make GET request to tracking endpoint
        response = self.client.get('/tracking')
        # Assert that the response status code is 200
        assert response.status_code == 200

    def test_tracking_get_with_order(self):
        # Set up session with username and orderId
        with self.client.session_transaction() as session:
            session['username'] = 'test'
            session['orderId'] = 12
        # Mock Order object to return test order details
        with patch.object(Order, 'get_order_details', return_value={'pickupAddress': 'Test Pickup Address', 'deliveryAddress': 'Test Delivery Address', 'orderStatus': '', 
                                                                    'orderPlaced': datetime(2013, 10, 31, 18, 23, 29, 227)}):
            # Make GET request to tracking endpoint
            response = self.client.get('/tracking')
            # Assert that the response status code is 200
            assert response.status_code == 200

    def test_tracking_get_with_no_order(self):
        # Set up session with username and orderId
        with self.client.session_transaction() as session:
            session['username'] = 'testuser'
            session['orderId'] = 1
        # Mock Order object to return empty order details
        with patch.object(Order, 'get_order_details', return_value={}):
            # Make GET request to tracking endpoint
            response = self.client.get('/tracking')
            # Assert that the response status code is 200
            assert response.status_code == 200
            # Assert that the response contains the no order details message
            assert b'No order details for this order.' in response.data
    
    def test_reset_password_success(self):
        with self.client.session_transaction() as session:
            session['username'] = 'test_user'
            form_data = {'new_password': 'new_password123'}
            response = self.client.post('/reset_password', data=form_data)
            self.assertIn(b'Password reset successfully', response.data)
            
if __name__ == '__main__':
    unittest.main()
