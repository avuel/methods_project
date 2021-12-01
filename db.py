import sqlite3

def createDB():
    # Create a connection to the database
    connect = sqlite3.connect('e-commerce.db')
    cur = connect.cursor()

    # Create the database if it does not exist
    cur.execute("CREATE TABLE IF NOT EXISTS Customer (username text, password text, address text, city text, "
                "state text, zip text, paymentInfo text)")

    # Commit the changes and close the connection
    connect.commit()
    connect.close()

def build_items_table() -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor, OperationalError
    from typing import Any

    try:
        conn: Connection = sql.connect('e-commerce.db')
        c: Cursor = conn.cursor()

        query: str = ('CREATE TABLE IF NOT EXISTS items ('
                            'itemID      INTEGER    NOT NULL    PRIMARY KEY AUTOINCREMENT,'
                            'name        TEXT       NOT NULL    UNIQUE,'
                            'unitCost    REAL       NOT NULL,'
                            'category    TEXT       NOT NULL,'
                            'stock       INTEGER    NOT NULL'
                        ')')
        c.execute(query)
        conn.commit()
        conn.close()

    except sql.OperationalError:
        print('Failed to create items table')

def delete_items_table() -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor, OperationalError
    from typing import Any

    try:
        conn: Connection = sql.connect('e-commerce.db')
        c: Cursor = conn.cursor()
        query: str = "DROP TABLE items"
        c.execute(query)
        conn.commit()
        conn.close()

    except sql.OperationalError:
        print('Failed to delete items table')