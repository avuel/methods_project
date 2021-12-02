# Create the customer table for the database
def create_customer_table():
    import sqlite3

    # Create a connection to the database
    connect = sqlite3.connect('e-commerce.db')
    cur = connect.cursor()

    # Create the database if it does not exist
    cur.execute("CREATE TABLE IF NOT EXISTS Customer ("
                "username TEXT UNIQUE PRIMARY KEY,"
                "password TEXT,"
                "address TEXT,"
                "city TEXT, "
                "state text, zip text, paymentInfo text)"
                )

    # Commit the changes and close the connection
    connect.commit()
    connect.close()

# Create the order table for the database
def create_order_table():
    import sqlite3
    # Create a connection to the database
    connect = sqlite3.connect('e-commerce.db')
    cur = connect.cursor()

    # Create the database if it does not exist
    cur.execute("CREATE TABLE IF NOT EXISTS Orders ("
                "orderID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
                "username TEXT FOREIGN KEY,"
                "total TEXT,"
                "address TEST)"
                )

    # Commit the changes and close the connection
    connect.commit()
    connect.close()

def build_items_table() -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor

    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    try:
        query: str = ('CREATE TABLE IF NOT EXISTS items ('
                            'itemID      INTEGER    NOT NULL    PRIMARY KEY AUTOINCREMENT,'
                            'name        TEXT       NOT NULL    UNIQUE,'
                            'unitCost    REAL       NOT NULL,'
                            'category    TEXT       NOT NULL,'
                            'stock       INTEGER    NOT NULL'
                        ')')
        c.execute(query)

    except sql.OperationalError:
        print('Failed to create items table')

    conn.commit()
    conn.close()

def delete_items_table() -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor

    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    try:
        query: str = "DROP TABLE items"
        c.execute(query)

    except sql.OperationalError:
        print('Failed to delete items table')

    conn.commit()
    conn.close()

# Create the order table for the database
def create_Inventory_table():
    import sqlite3
    # Create a connection to the database
    connect = sqlite3.connect('e-commerce.db')
    cur = connect.cursor()

    # Create the database if it does not exist
    cur.execute("CREATE TABLE IF NOT EXISTS Orders ("
                "itemID INTEGER NOT NULL,"
                "stock INTEGER,"
                "Foregin Key (itemID) REFERENCES items(itemID))"
                )

    # Commit the changes and close the connection
    connect.commit()
    connect.close()