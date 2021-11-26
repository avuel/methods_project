from db import *

class Customer:

    def __init__(self, username, password):

        self.__username = username
        self.__password = password
        self.__address = ""
        self.__city = ""
        self.__state = ""
        self.__zip = ""
        self.__paymentInfo = ""
        self.__orderHistory = []

    def setAddress(self, address):
        self.__address = address

    def setCity(self, city):
        self.__city = city

    def setZip(self, zip):
        self.__zip = zip

    def setPaymentInfo(self, paymentInfo):
        self.__paymentInfo = paymentInfo

    def sedOrderHistory(self, orderHistory):
        self.__orderHistory = orderHistory

    def login(self):
        # Create a connection to the db and make a cursor
        connect = sqlite3.connect("e-commerce.db")
        cur = connect.cursor()
        # create the db
        createDB()

        # Try to get the user from the table
        cur.execute("SELECT username FROM Customer WHERE username=? AND password=?", (self.__username, self.__password))
        row = cur.fetchall()

        # If the length of name is 0 the data was not in the db, set the flag to false, otherwise set it to true
        if len(row) == 0:
            validated = False
        else:
            validated = True

        # If either test was false recursively call login
        if validated is False or validated is False:
            result = False
        else:
            result = True

        return result

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
            cur.execute(
                "INSERT INTO Customer VALUES ('" + self.__username + "', " + "'" + self.__password + "', " + "'NULL', 'NULL', 'NULL', 'NULL', 'NULL')")
            connect.commit()
            result = True
        else:
            result = False

        # Close the connection and return the result
        connect.close()
        return result
