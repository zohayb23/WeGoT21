
from dotenv import dotenv_values
import mysql.connector


class receiver_class:
    
    def __init__(self, receiverID, receiverName, receiverEmail, orderCode):
        env_vars = dotenv_values(".env")
        self._username = env_vars.get("USERNAME")
        self.pwd = env_vars.get("PWD")

        self.receiverID = receiverID
        self._receiverName = receiverName
        self._receiverEmail = receiverEmail
        self._orderCode = orderCode

        self.__create_receiver()

    def create_receiver(self, receiverName, receiverEmail):
        try:
            connection = mysql.connector.connect(user=self._username, password=self.pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            query = "INSERT INTO Receiver (receiverID, receiverName, receiverEmail) VALUES (%s, %s, %s, %s)"
            values = (None, self._receiverName, self._receiverEmail)

            cursor.execute(query, values)

            connection.commit()
            cursor.close()
            connection.close()

            self._receiverID = cursor.lastrowid

            return self._receiverID
        
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
            self._receiverID = None
            return self._receiverID


    def getReceiverID(self, receiverID):
        try:
            connection = mysql.connector.connect(user=self._username, password=self.pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            query = "SELECT receiverID FROM Receiver WHERE receiverID = %s"
            values = (receiverID)

            cursor.execute(query, values)

            result = cursor.fetchone()
            if result:
                return result[0]
            
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
            return 0
    
    def getReceiverName(self, receiverID):
        try:
            connection = mysql.connector.connect(user=self._username, password=self.pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            query = "SELECT receiverName FROM Receiver WHERE receiverID = %s"
            values = (receiverID)

            cursor.execute(query, values)

            result = cursor.fetchone()
            if result:
                return result[0]
            
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
            return 0
        

    def getReceiverEmail(self, receiverID):
        try:
            connection = mysql.connector.connect(user=self._username, password=self.pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            query = "SELECT receiverEmail FROM Receiver WHERE receiverID = %s"
            values = (receiverID)

            cursor.execute(query, values)

            result = cursor.fetchone()
            if result:
                return result[0]
            
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
            return 0    
        

    def getOrderCode(self, orderID):
        try:
            connection = mysql.connector.connect(user=self._username, password=self.pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            query = "SELECT orderCode FROM Order WHERE orderID = %s"
            values = (orderID)

            cursor.execute(query, values)

            result = cursor.fetchone()
            if result:
                return result[0]
            
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
            return 0    

    # def getFullReceiver(self, receiverID, orderID):
    #     try:
    #         connection = mysql.connector.connect(user=self._username, password=self.pwd, host='104.236.2.101', database='WeGo', port='3306')
    #         cursor = connection.cursor()

    #         query = "SELECT receiverID, receiverName, receiverEmail, orderCode FROM Receiver, Order WHERE receiverID = %s AND orderID = %s"
    #         values = (receiverID, orderID)

    #         cursor.execute(query, values)

    #         result = cursor.fetchone()
    #         if result:
    #             return result[0]
            
    #     except mysql.connector.Error as e:
    #         print("Unable to connect to the database:", e)
    #         return 0

    def getReceiverInfo(self, receiverID):
        try:
            connection = mysql.connector.connect(user=self._username, password=self.pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            query = "SELECT * FROM Receiver, Order WHERE receiverID = %s"
            values = (receiverID)

            cursor.execute(query, values)

            result = cursor.fetchone()
            if result:
                return result[0]
            
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
            return 0
        
    def verifyCode(self, receiverCode, orderID):
        
        matches = False
        orderCode = getOderCode(orderID)

        if (receiverCode == orderCode):
            matches = True

        return matches
    
    @property
    def receiverDesc(self, receiverID):
        
        receiverName = self._getReceiverName()
        receiverEmail = self._getReceiverEmail()

        self._receiverDesc = "Here is the orders receiver info: " + receiverID.get('receiverID') + receiverName.get('receiverName') + receiverEmail.get('receiverEmail')

        connection = mysql.connector.connect(user=self._username, password=self.pwd, host='104.236.2.101', database='WeGo', port='3306')
        cursor = connection.cursor()

        query = "ISERT INTO Receiver (receiverID, receiverName, receiverEmail) VALUES (%s, %s, %s)"
        values = (self._receiverID, self._receiverName, self._receiverEmail)

        cursor.execute(query, values)

        connection.commit()
        cursor.close()
        connection.close()

        return self._receiverDesc

    @property 
    def receiverName(self, receiverID):
        return self._receiverName

    @property
    def receiverEmail(self, receiverID):
        return self._receiverEmail
