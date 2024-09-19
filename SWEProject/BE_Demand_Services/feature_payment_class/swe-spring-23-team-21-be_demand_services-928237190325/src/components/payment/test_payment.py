import unittest
import time
from sqlalchemy import DateTime, func
from payment import Payment

class paymentTestCase(unittest.TestCase):

    def test_getters(self):
        # Initialization of test Payment object, this line is repeated in every test case
        payment_test = Payment(0, 'Credit Card', 0, 50.00, 0, 00000000, None, 'Pending')
        # Initialize a variable holding the current DateTime and set the test object's DateTime to it
        # Using func.now() in an assertEqual call would cause a fail because func.now() would be called after initial_time is set, thus they would be unequal
        initial_time = func.now()
        payment_test.set_paymentDatetime(initial_time)
        self.assertEqual(payment_test.get_paymentID(), 0)
        self.assertEqual(payment_test.get_paymentMethod(), 'Credit Card')
        self.assertEqual(payment_test.get_orderID(), 0)
        self.assertEqual(payment_test.get_paymentAmount(), 50.00)
        self.assertEqual(payment_test.get_userID(), 0)
        self.assertEqual(payment_test.get_cardNum(), 00000000)
        self.assertEqual(payment_test.get_paymentDatetime(), initial_time)
        self.assertEqual(payment_test.get_paymentStatus(), 'Pending')

    def test_setters(self):
        payment_test = Payment(0, 'Credit Card', 0, 50.00, 0, 00000000, None, 'Pending')
        time.sleep(3) # Used to have a significant change in paymentDateTime for testing
        new_time = func.now()

        # Each setter method is called immediately before their assertion for organization
        payment_test.set_paymentID(1)
        self.assertEqual(payment_test.paymentID, 1)

        payment_test.set_paymentMethod('Debit Card')
        self.assertEqual(payment_test.paymentMethod, 'Debit Card')

        payment_test.set_orderID(1)
        self.assertEqual(payment_test.orderID, 1)

        payment_test.set_paymentAmount(25.00)
        self.assertEqual(payment_test.paymentAmount, 25.00)

        payment_test.set_cardNum(11111111)
        self.assertEqual(payment_test.cardNum, 11111111)

        payment_test.set_paymentDatetime(new_time)
        self.assertEqual(payment_test.paymentDatetime, new_time)

        payment_test.set_paymentStatus('Received')
        self.assertEqual(payment_test.paymentStatus, 'Received')

    def test_verify_and_update(self):
        payment_test = Payment(0, 'Credit Card', 0, 50.00, 0, 00000000, None, 'Pending')
        self.assertEqual(payment_test.VerifyPayment(), True)
        payment_test.UpdateStatus()
        self.assertEqual(payment_test.paymentStatus, 'Processed')

if __name__ == '__main__':
    unittest.main()
