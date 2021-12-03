from db import *
import sqlite3

class Customer:

    # Parameterized constructor
    def __init__(self, username, password):

        self.__username = username
        self.__password = password
        self.__address = ""
        self.__city = ""
        self.__state = ""
        self.__zipCode = ""
        self.__paymentInfo = ""

    # * These are the getters and setters for the Customer class *

    # Set the user's username
    def setUsername(self, username):
        # Establish connection with the db and create a cursor
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()

        # Update the database to reflect the changes
        cur.execute("UPDATE Customer SET username=? WHERE username=?", (username, self.__username))
        cur.execute("UPDATE cart SET username=? WHERE username=?", (username, self.__username))
        cur.execute("UPDATE Orders SET username=? WHERE username=?", (username, self.__username))

        # Commit the changes and close the connection
        connect.commit()
        connect.close()

        self.__username = username

    # Set the user's password
    def setPassword(self, password):
        # Establish connection with the db and create a cursor
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()

        # Update the database to reflect the changes
        cur.execute("UPDATE Customer SET password=? WHERE username=?", (password, self.__username))

        # Commit the changes and close the connection
        connect.commit()
        connect.close()

        # Set the object's data to the passed-in value
        self.__password = password

    # Set the user's address
    def setAddress(self, address):
        # Establish connection with the db and create a cursor
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()

        # Update the database to reflect the changes
        cur.execute("UPDATE Customer SET address=? WHERE username=?", (address, self.__username))
        
        # Commit the changes and close the connection
        connect.commit()
        connect.close()

        # Set the object's data to the passed-in value
        self.__address = address

    # Set the user's city
    def setCity(self, city):
        # Establish connection with the db and create a cursor
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()

        # Update the database to reflect the changes
        cur.execute("UPDATE Customer SET city=? WHERE username=?", (city, self.__username))

        # Commit the changes and close the connection
        connect.commit()
        connect.close()

        # Set the object's data to the passed-in value
        self.__city = city

    # Set the user's state
    def setState(self, state):
        # Establish connection with the db and create a cursor
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()

        # Update the database to reflect the changes
        cur.execute("UPDATE Customer SET state=? WHERE username=?", (state, self.__username))

        # Commit the changes and close the connection
        connect.commit()
        connect.close()

        # Set the object's data to the passed-in value
        self.__state = state

    # Set the user's zipCode
    def setZip(self, zipCode):
        # Establish connection with the db and create a cursor
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()

        # Update the database to reflect the changes
        cur.execute("UPDATE Customer SET zip=? WHERE username=?", (zipCode, self.__username))

        # Commit the changes and close the connection
        connect.commit()
        connect.close()

        # Set the object's data to the passed-in value
        self.__zipCode = zipCode

    # Set the user's payment info
    def setPaymentInfo(self, paymentInfo):
        # Establish connection with the db and create a cursor
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()

        # Update the database to reflect the changes
        cur.execute("UPDATE Customer SET paymentInfo=? WHERE username=?", (paymentInfo, self.__username))

        # Commit the changes and close the connection
        connect.commit()
        connect.close()

        # Set the object's data to the passed-in value
        self.__paymentInfo = paymentInfo

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getAddress(self):

        if self.__address == "":
            return ""
        else:
            fullAddress = f"{self.__address} {self.__city}, {self.__state} {self.__zipCode}"
            return fullAddress

    def getPaymentInfo(self):
        return self.__paymentInfo

    # * These are the getters and setters for the Customer class *

    # This functions checks if the user entered valid credentials and returns the result
    def login(self):
        from Item import insert_item
        from Inventory import load_db
        # Create a connection to the db and make a cursor
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()
        # create the db
        createDB()
        # Try to get the user from the table
        cur.execute("SELECT * FROM Customer WHERE username=? AND password=?", (self.__username, self.__password))
        row = cur.fetchone()

        # If the length of name is 0 the data was not in the db, set the flag to false, otherwise set it to true
        if row is None:
            validated = False
        else:
            validated = True 

            if len(row) > 2:
                if row[2] is not None:
                    self.__address = row[2]
                if row[3] is not None:
                    self.__city = row[3]  
                if row[4] is not None:
                    self.__state = row[4]
                if row[5] is not None:  
                    self.__zipCode = row[5] 
                if len(row) > 6:
                    if row[6] is not None:
                        self.__paymentInfo = row[6]

        return validated

    # This function allows the user to create a set of login credentials in the database
    def create_account(self):
        # Create a connection to the db and make a cursor
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()
        # create the db
        createDB()

        # Try to get the user from the table, on success set the flag to true
        cur.execute("SELECT * FROM Customer WHERE username=?", (self.__username,))
        row = cur.fetchall()

        # If row contains data the username already exists, set the flag to false
        if len(row) == 0:
            not_taken = True
        else:
            not_taken = False

        # If the username is not taken, push the data back and commit the changes
        if not_taken is True:
            cur.execute("INSERT INTO Customer VALUES (?, ?, ?, ?, ?, ?, ?)", (self.__username, self.__password, None, None, None, None, None,))

            # Commit the changes and close the connection
            connect.commit()
            result = True
        else:
            result = False

        # Close the connection and return the result
        connect.close()
        return result

    # Allows a user to delete their account
    def delete_account(self):
        # Create a connection to the database
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()

        # Attempt to delete the user from the db
        cur.execute("DELETE FROM Customer WHERE username=?", (self.__username,))

        # Commit the changes and close the connection
        connect.commit()
        connect.close()

        return

        # Return a user's order history
    def getOrderHistory(self):
        # Create the connection and the cursor
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()
        
        cur.execute("""SELECT * FROM Orders WHERE username=?""", (self.__username, ))
        orders = cur.fetchall()

        return orders
