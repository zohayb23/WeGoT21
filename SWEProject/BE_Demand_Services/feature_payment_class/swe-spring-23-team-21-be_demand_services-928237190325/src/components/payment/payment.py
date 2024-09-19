from sqlalchemy import Column, Integer, Double, String, ForeignKey, DateTime, func
# import mysql.connector #Waiting for payment services integration
# import os, requests
# from dotenv import dotenv_values #Will be included once an API has been chosen along with os/ requests

# This class is subject to change to accommodate the needs of the payment service provider's API
# Structure of the table and constructor are also subject to change to work well with FE forms
# Login credentials from a .env file to be included for Database interaction, and API key for payment API access
class Payment():
    __tablename__ = 'payment'

# Table structure of payment entity in MySQL Database
    paymentID = Column(Integer, primary_key=True)
    paymentMethod = Column(String(20))
    orderID = Column(Integer, ForeignKey('orderID'))
    paymentAmount = Column(Double)
    userID = Column(Integer, ForeignKey('userID'))
    cardNum = Column(Integer)
    paymentDatetime = Column(DateTime(timezone=True), default=func.now())
    paymentStatus = Column(String(10))

# Basic constructor, subject to change as scope of payment services is explored
    def __init__(self, paymentID, paymentMethod, orderID, paymentAmount, userID, cardNum, paymentDatetime, paymentStatus):
        # To be included with dotenv & os import when payment API 
        # self.api_key = os.environ.get(<API_KEY_NAME>) #<-- TODO: Replace placeholder name
        # env = dotenv_values('.env')
        # self._username = env.get('USERNAME')
        # self._pwd = env.get('PWD')
        
        self.paymentID = paymentID
        self.paymentMethod = paymentMethod
        self.orderID = orderID
        self.paymentAmount = paymentAmount
        self.userID = userID
        self.cardNum = cardNum
        self.paymentDateTime = paymentDatetime
        self.paymentStatus = paymentStatus

# setter methods
    def set_paymentID(self, paymentID):
        self.paymentID = paymentID

    def set_paymentMethod(self, paymentMethod):
        self.paymentMethod = paymentMethod

    def set_orderID(self, orderID):
        self.orderID = orderID

    def set_paymentAmount(self, paymentAmount):
        self.paymentAmount = paymentAmount

    def set_userID(self, userID):
        self.userID = userID

    def set_cardNum(self, cardNum):
        self.cardNum = cardNum

    def set_paymentDatetime(self, paymentDatetime):
        self.paymentDatetime = paymentDatetime

    def set_paymentStatus(self, paymentStatus):
        self.paymentStatus = paymentStatus

# setter methods
    def get_paymentID(self):
        return self.paymentID

    def get_paymentMethod(self):
        return self.paymentMethod

    def get_orderID(self):
        return self.orderID

    def get_paymentAmount(self):
        return self.paymentAmount

    def get_userID(self):
        return self.userID

    def get_cardNum(self):
        return self.cardNum

    def get_paymentDatetime(self):
        return self.paymentDatetime

    def get_paymentStatus(self):
        return self.paymentStatus

# DB interaction methods: Currently return dummy values to verify basic functionality
# These methods will be redefined once payment services API is integrated
    def VerifyPayment(self):
        return True

    def UpdateStatus(self):
        self.set_paymentStatus('Processed')
        return True

#Base.metadata.create_all(engine) # Reserved