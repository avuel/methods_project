# Create all the tables
def createDB():
    create_customer_table()
    create_items_table()
    create_inventory_table()
    create_orders_table()
    create_cart_table()

# Create the customer table for the database
def create_customer_table():
    import sqlite3

    # Create a connection to the database
    connect = sqlite3.connect('e-commerce.db')
    cur = connect.cursor()

    # Create the database if it does not exist
    cur.execute("""CREATE TABLE IF NOT EXISTS Customer (
                username TEXT UNIQUE PRIMARY KEY,
                password TEXT,
                address TEXT,
                city TEXT, 
                state text, 
                zip text, 
                paymentInfo text);
                """)

    # Commit the changes and close the connection
    connect.commit()
    connect.close()

# Create the order table for the database
def create_orders_table():
    import sqlite3
    # Create a connection to the database
    connect = sqlite3.connect('e-commerce.db')
    cur = connect.cursor()

    # Create the database if it does not exist
    cur.execute("""CREATE TABLE IF NOT EXISTS Orders (
                orderID INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                total TEXT,
                address TEXT,
                FOREIGN KEY(username) REFERENCES Customer(username));
                """)

    # Commit the changes and close the connection
    connect.commit()
    connect.close()

def create_items_table() -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor

    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    try:
        query: str = ('CREATE TABLE IF NOT EXISTS items ('
                            'itemID      INTEGER    NOT NULL    PRIMARY KEY AUTOINCREMENT,'
                            'name        TEXT       NOT NULL,'
                            'unitCost    REAL       NOT NULL,'
                            'category    TEXT       NOT NULL'
                        ')')
        c.execute(query)

    except sql.OperationalError:
        ...

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
        ...

    conn.commit()
    conn.close()

# Create the inventory table for the database
def create_inventory_table() -> None:
    import sqlite3
    # Create a connection to the database
    connect = sqlite3.connect('e-commerce.db')
    c = connect.cursor()

    # Create the database if it does not exist
    query: str = ('CREATE TABLE IF NOT EXISTS inventory ('
                            'itemID     INTEGER    NOT NULL     PRIMARY KEY,'
                            'stock      INTEGER    NOT NULL,'
                            'FOREIGN KEY(itemID) REFERENCES items(itemID)'
                        ');')
    c.execute(query)

    # Commit the changes and close the connection
    connect.commit()
    connect.close()
    
# Create the Cart Table for the database
def create_cart_table() -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor

    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    # Create the database if it does not exist
    query: str = ('CREATE TABLE IF NOT EXISTS cart ('
                            'cartID     INTEGER    NOT NULL     PRIMARY KEY AUTOINCREMENT,'
                            'username   TEXT       NOT NULL,'
                            'itemID     INTEGER    NOT NULL,'
                            'quantity   INTEGER    NOT NULL,'
                            'FOREIGN KEY(username) REFERENCES Customer(username),'
                            'FOREIGN KEY(itemID) REFERENCES items(itemID)'
                        ');')
                        
    c.execute(query)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()
