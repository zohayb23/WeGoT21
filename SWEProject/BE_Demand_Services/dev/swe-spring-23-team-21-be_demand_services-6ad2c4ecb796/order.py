import os
import random
from dotenv import dotenv_values
from datetime import datetime
import mysql.connector

class Order:
    def __init__(self, user=None):
        # Gets the DB logins
        env_vars = dotenv_values(".env")
        self._username = env_vars.get("USERNAME")
        self._pwd = env_vars.get("PWD")
        self._user = user
        self._orderPlaced = datetime.now()

        self._orderStatus = "Processing"
        self._pickupAddress = ''
        self._deliveryAddress = ''
        self._orderCode = random.randint(1000, 9999)
        self._isRegistered = False
        self._pickUpLat = 0.0
        self._pickUpLong = 0.0
        self._dropOffLat = 0.0
        self._dropOffLong = 0.0
        self._orderDeliveryDate = datetime.now()
        #Cost is a random number for now
        self._totalCost = (random.randint(10, 99) * 1.3)


    def check_if_orderId_exists(self):
        try:
            # Connect to the database
            connection = mysql.connector.connect(user=self._username, password=self._pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            # Execute a SELECT query to check if the order ID already exists
            query = "SELECT * FROM Orders WHERE orderID = %s"
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
            return {"orderPlaced": self._orderPlaced, "orderDeliveryDate": self._orderDeliveryDate, "orderStatus": self._orderStatus, "orderCode": self._orderCode, "pickUpLat": self._pickUpLat, "pickUpLong": self._pickUpLong, "dropOffLat": self._dropOffLat, "dropOffLong": self._dropOffLong, "totalCost": self._totalCost}
        else:
            return {}



    #Registers the order in the DB: note: __ is for private methods, please do not access externally
    def __register_order(self): 
        try:
            print(self._user)
            # Connect to the database
            connection = mysql.connector.connect(user=self._username, password=self._pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            # Prepare the INSERT statement: EDIT THIS WHEN ER DIAGRAM IS FINALIZED
            sql = "SELECT userID FROM User WHERE username = %s"
            cursor.execute(sql, (self._user,))
            result = cursor.fetchone()
            if result is not None:
                userID = result[0]
            else:
            # handle the case where no matching rows were found
                userID = None
            
            print(userID)

            # Prepare the INSERT statement: EDIT THIS WHEN ER DIAGRAM IS FINALIZED
            query="INSERT INTO Orders (userID, orderStatus, deliveryAddress, pickupAddress, orderPlaced, orderDeliveryDate, orderTotalCost, orderCode, pickupLat, pickupLong, dropoffLat, dropoffLong) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (userID, self._orderStatus, self._deliveryAddress, self._pickupAddress, self._orderPlaced, self._orderDeliveryDate, self._totalCost, self._orderCode,  
                      self._pickUpLat, self._pickUpLong, self._dropOffLat, self._dropOffLong)
            
            # Execute the INSERT statement
            cursor.execute(query, values)

            # Get the ID of the newly inserted row
            self._order_Id = cursor.lastrowid

            # Commit the changes and close the connection
            connection.commit()
            cursor.close()
            connection.close()

            self._isRegistered = True
            
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
        
        return self._isRegistered
        

    def get_order_details(self, orderId): 
        if orderId != None:
            try:
                # Connect to the database
                connection = mysql.connector.connect(user=self._username, password=self._pwd, host='104.236.2.101', database='WeGo', port='3306')
                cursor = connection.cursor()
                # Execute a SELECT query to retrieve order details
                query = "SELECT * FROM Orders WHERE orderID = %s"
                cursor.execute(query, (orderId,))

                # Fetch the result as a dictionary
                row = cursor.fetchone()
                if row is not None:
                    cols = [column[0] for column in cursor.description]
                    order_dict = dict(zip(cols, row))
                else:
                    order_dict = {}
                    
                # Commit the changes and close the connection
                connection.commit()
                cursor.close()
                connection.close()

                return order_dict
            
            except mysql.connector.Error as e:
                print("Unable to connect to the database:", e)
                return {}


    #Getter and setters (if appropriate):
    @property
    def order_Id(self):
        return self._order_Id
    
    @property
    def username(self):
        return self._user

    @property
    def orderPlaced(self):
        return self._orderPlaced
    
    @property
    def orderDeliveryDate(self):
        return self._orderDeliveryDate
    
    @orderDeliveryDate.setter
    def orderDeliveryDate(self, value):
        self._orderDeliveryDate = value
    
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
    def pickupAddress(self):
        return self._pickupAddress
    
    @pickupAddress.setter
    def pickupAddress(self, value):
        self._pickupAddress = value
    
    @property
    def deliveryAddress(self):
        return self._deliveryAddress
    
    @deliveryAddress.setter
    def deliveryAddress(self, value):
        self._deliveryAddress = value

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