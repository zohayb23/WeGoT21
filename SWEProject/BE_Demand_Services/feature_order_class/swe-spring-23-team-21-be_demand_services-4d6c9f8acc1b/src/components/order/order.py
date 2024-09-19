import os
import random
from dotenv import dotenv_values
from datetime import datetime
import mysql.connector

class Order:
    
    def __init__(self, order_id=None):
        # Gets the DB logins
        env_vars = dotenv_values(".env")
        self._username = env_vars.get("USERNAME")
        self._pwd = env_vars.get("PWD")
        exists = True

        #Set order details
        if order_id is None:
            while exists == True:
                self._orderID = random.randint(100, 10000)
                #check if the order ID already exists
                exists = self.check_if_orderId_exists()
        else:
            self._orderID = order_id

        self._orderDatetime = datetime.now()

        self._orderStatus = "Processing"

        self._orderCode = random.randint(1000, 9999)
        self._isRegistered = False
        self._pickUpLat = 0.0
        self._pickUpLong = 0.0
        self._dropOffLat = 0.0
        self._dropOffLong = 0.0

        #Cost is a random number for now
        self._totalCost = (random.randint(10, 99) * 1.3)


    def check_if_orderId_exists(self):
        try:
            # Connect to the database
            connection = mysql.connector.connect(user=self._username, password=self._pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            # Execute a SELECT query to check if the order ID already exists
            query = "SELECT * FROM Order WHERE orderID = %s"
            cursor.execute(query, (self._orderID,))

            # If the query returns any rows, the order ID already exists in the database
            if cursor.fetchone() is not None:
                cursor.close()
                connection.close()
                return True
        
            else:
                cursor.close()
                connection.close()
                return False
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
    
    def place_order(self):  
        # call register order to save order details in DB
        wentThrough = self.__register_order()

        if wentThrough == True:
            # Return a dictionary of all order details
            return {"orderID": self._orderID, "orderDatetime": self._orderDatetime, "orderStatus": self._orderStatus, "orderCode": self._orderCode, "pickUpLat": self._pickUpLat, "pickUpLong": self._pickUpLong, "dropOffLat": self._dropOffLat, "dropOffLong": self._dropOffLong, "totalCost": self._totalCost}
        else:
            return {}



    #Registers the order in the DB: note: __ is for private methods, please do not access externally
    def __register_order(self): 
        try:
            # Connect to the database
            connection = mysql.connector.connect(user=self._username, password=self._pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            # Prepare the INSERT statement: EDIT THIS WHEN ER DIAGRAM IS FINALIZED
            query = "INSERT INTO Order (orderID, orderDatetime, orderStatus, orderCode, orderTotalCost, pickupLat, pickupLong, dropoffLat, dropoffLong) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self._orderID, self._orderDatetime, self._orderStatus, self._orderCode, self._totalCost, self._pickUpLat, self._pickUpLong, self._dropOffLat, self._dropOffLong)

            # Execute the INSERT statement
            cursor.execute(query, values)

            # Commit the changes and close the connection
            connection.commit()
            cursor.close()
            connection.close()

            self._isRegistered = True
            
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
        
        return self._isRegistered


    #Getter and setters (if appropriate):
    @property
    def orderID(self):
        return self._orderID

    @property
    def orderDatetime(self):
        return self._orderDatetime
    
    @property
    def orderStatus(self):
        return self._orderStatus
    
    @orderStatus.setter
    def orderStatus(self, value):
        self._orderStatus = value

    @property
    def orderCode(self):
        return self._orderCode
    
    @property
    def totalCost(self):
        return self._totalCost
    
    @property
    def pickUpLat(self):
        return self._pickUpLat
    
    @pickUpLat.setter
    def pickUpLat(self, value):
        self._pickUpLat = value

    @property
    def pickUpLong(self):
        return self._pickUpLong
    
    @pickUpLong.setter
    def pickUpLong(self, value):
        self._pickUpLong = value
    
    @property
    def dropOffLat(self):
        return self._dropOffLat
    
    @dropOffLat.setter
    def dropOffLat(self, value):
        self._dropOffLat = value

    @property
    def dropOffLong(self):
        return self._dropOffLong
    
    @dropOffLong.setter
    def dropOffLong(self, value):
        self._dropOffLong = value