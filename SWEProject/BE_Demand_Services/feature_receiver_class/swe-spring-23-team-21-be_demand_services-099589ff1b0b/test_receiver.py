import unittest

from unittest.mock import patch

from datetime import datetime

from dotenv import dotenv_values

from receiver import *

class TestReceiver(unittest.TestCase):

    @patch('receiver.dotenv_values')

    def test_init(self, mock_dotenv):

        mock_dotenv.return_value = {'USERNAME': 'user', 'PWD': 'password'}

        receiver = receiver_class()

        self.assertEqual(receiver._username, 'user')

        self.assertEqual(receiver._pwd, 'fakepassword')

        self.assertIsInstance(receiver._receiverID, int)

        self.assertGreaterEqual(receiver._receiverID, 100)

        self.assertLessEqual(receiver._receiverID, 10000)
    
        self.assertIsInstance(receiver._name, str)

        self.assertIsInstance(receiver._email, str)

        self.assertIsInstance(receiver._orderCode, int)
    

    def test_receiverID(self):

        receiver = receiver_class()

        self.assertIsNotNone(receiver.receiverID)
        
    def test_receiverName(self):

        receiver = receiver_class()
        self.assertEqual(receiver.receiverName, "")
        receiver.receiverName = "John"
        self.assertEqual(receiver.receiverName, "John")

    def test_receiverEmail(self):

        receiver = receiver_class()
        self.assertEqual(receiver.receiverEmail, "")
        receiver.receiverName = "John@email.com"
        self.assertEqual(receiver.receiverName, "John@email.com")
    

    def test_register_receiver(self):

        receiver = receiver_class()

        # Call the create_receiver method

        wentThrough = receiver.create_receiver()

        # Assert that the method returned a dictionary that is not empty

        assert len(receiver.create_receiver()) > 0, "Dictionary is empty"