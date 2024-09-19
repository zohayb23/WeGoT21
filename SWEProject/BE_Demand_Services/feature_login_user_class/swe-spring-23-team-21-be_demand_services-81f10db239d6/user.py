import certifi
import bcrypt
import os
import random
from dotenv import dotenv_values
from datetime import datetime
import mysql.connector

class User:
    def __init__(self):
        # Gets the DB logins
        env_vars = dotenv_values(".env")
        self._username = env_vars.get("USERNAME")
        self._pwd = env_vars.get("PWD")


#DO NOT USE!!!! FOR TESTING PURPOSES
    def create_user(self, username, password):
        # Generate salt and hash password
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        
        user = {"username": username, "password": hashed }
        
        try:
            # Connect to the database
            connection = mysql.connector.connect(user=self._username, password=self._pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            # Execute a SELECT query to check if the username already exists
            query = "SELECT * FROM User WHERE username = %s"
            cursor.execute(query, (username,))

        # If the query returns any rows, the username already exists in the database
            if cursor.fetchone() is not None:
                cursor.close()
                connection.close()
                return True
            else:
                try:
                    # Insert the new user into the database
                    insert_query = "INSERT INTO User (username, password) VALUES (%s, %s)"
                    cursor.execute(insert_query, (username, hashed))
                    connection.commit()
                    cursor.close()
                    connection.close()
                    return True
                except mysql.connector.Error as e:
                    print("Unable to insert user into the database:", e)
                    cursor.close()
                    connection.close()
                    return False

        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)

    def reset_password(self, username, new_password):
        # Hash the new password
        hashed = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
        
        try:
            # Connect to the database
            connection = mysql.connector.connect(user=self._username, password=self._pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()

            # Execute an UPDATE query to set the new password for the given username
            query = "UPDATE User SET password = %s WHERE username = %s"
            cursor.execute(query, (hashed, username))

            # Commit the changes to the database
            connection.commit()

            # Close the cursor and connection
            cursor.close()
            connection.close()

            # Return True to indicate success
            return True
        
        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
            # Return False to indicate failure
            return False

    def validate_user(self, username, password):
        try:
            # Retrieve the hashed and salted password from the SQL database
            connection = mysql.connector.connect(user=self._username, password=self._pwd, host='104.236.2.101', database='WeGo', port='3306')
            cursor = connection.cursor()
            query = "SELECT password FROM User WHERE username = %s"
            cursor.execute(query, (username,))
            row = cursor.fetchone()

            if row is not None:
                # If the row exists, check if the provided password matches the stored hash
                try:
                    hashed_password = row[0]
                    if bcrypt.checkpw(password.encode('utf-8'), str(hashed_password).encode('utf-8')):
                        # If the password matches, return True to indicate success
                        cursor.close()
                        connection.close()
                        return True
                    else:
                        # If the password doesn't match, return False to indicate failure
                        cursor.close()
                        connection.close()
                        return False
                except ValueError:
                    # If the stored hash is invalid, return False to indicate failure
                    cursor.close()
                    connection.close()
                    return False
            else:
                # If no row was found, return False to indicate failure
                cursor.close()
                connection.close()
                return False

        except mysql.connector.Error as e:
            print("Unable to connect to the database:", e)
            # Return False to indicate failure
            return False


        
    def login_user(self, username, password):
        if self.validate_user(username, password):
            return True
        return False

    def logout_user(self):
        return True