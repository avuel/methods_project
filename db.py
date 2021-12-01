import sqlite3


def createDB():
    # Create a connection to the database
    connect = sqlite3.connect("e-commerce.db")
    cur = connect.cursor()

    # Create the database if it does not exist
    cur.execute("CREATE TABLE IF NOT EXISTS Customer (username text, password text, address text, city text, "
                "state text, zip text, paymentInfo text)")

    # Commit the changes and close the connection
    connect.commit()
    connect.close()
