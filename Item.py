# Item Class
class Item:
    # Constructor for the Item Class
    def __init__(self, itemId: int, name: str, unitCost: float, category: str) -> None:
        self.__itemID: int = itemId
        self.__name: str = name
        self.__unitCost: float = unitCost
        self.__category: str = category

    # Change how our object is printed
    def __repr__(self) -> str:
        return (f"ID: {self.__itemID}\nName: {self.__name}\nCost per Item: {self.__unitCost:.2f}\nCategory: {self.__category}\n")

    # Get the ID of an Item
    def getID(self) -> int:
        return self.__itemID

    # Get the Name of an Item
    def getName(self) -> str:
        return self.__name

    # Get the Category of an Item
    def getCategory(self) -> str:
        return self.__category

    # Get the Unit Cost of an Item
    def getUnitCost(self) -> float:
        return self.__unitCost


# Search for an item based on category and name
def search_item(name: str, category: str) -> 'list':
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor
    from typing import Any

    # Connect to the database and create a cursor
    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    # Grab all of the data where the item name and category match
    query: str = "SELECT * FROM items WHERE name=:name AND category=:category"
    c.execute(query, {'name': name, 'category': category})

    # Grab the rows and commmit all of our changes and close our connection
    tuples: list[Any] = c.fetchall()
    conn.commit()
    conn.close()

    # If we did not grab any rows, we did not find the item
    if len(tuples) == 0:
        return None

    # Return the rows we grabbed
    return tuples


# Insert an item into the items table (WAS ONLY USED TO INITIALLY PUT DATA INTO THE DB, NOT USED ANYMORE)
def insert_item(name: str, category: str, unitCost: float) -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor
    from typing import Any

    # Connect to the database and create a cursor
    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    try: 
        # Check if the item is in the database
        tuples: list[Any] = search_item(name, category)

        # Search returns none if we did not find the item
        if tuples is not None:
            # Commit our changes and close the database
            conn.commit()
            conn.close()
            return None

        # Insert the item into our database (we do not need an itemID as it is automatically generated)
        query: str = f"INSERT INTO items (name, unitCost, category) VALUES (:name, :unitCost, :category)"
        c.execute(query, {'name': name, 'unitCost': unitCost, 'category': category})
  
    except sql.IntegrityError:
        # If we get an integrity error, continue on
        ...

    # Commit our changes and close the database
    conn.commit()
    conn.close()


# Remove an item from the items table
def remove_item(name: str, category: str) -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor
    from typing import Any

    # Connect to the database and create a cursor
    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    try: 
        # Check if the item is in the database
        tuples: list[Any] = search_item(name, category)

        # Search returns none if we did not find the item
        if tuples is None:
            # Commit our changes and close the database
            conn.commit()
            conn.close()
            return None

        # Delete all of the rows from the database where the item name and category match
        query: str = f"DELETE FROM items WHERE name=:name AND category=:category"
        c.execute(query, {'name': name, 'category': category})
  
    except sql.IntegrityError:
        # If we get an integrity error, continue on
        ...

    # Commit our changes and close the database
    conn.commit()
    conn.close()

    
# Grab all of the rows from the items table
def get_items() -> list:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor
    from typing import Any

    # Connect to the database and create a cursor
    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    query: str = "SELECT * FROM items"
    c.execute(query)

    # Grab the rows and commmit all of our changes and close our connection
    tuples: list[Any] = c.fetchall()
    conn.commit()
    conn.close()

    # Return the rows we grabbed
    return tuples
