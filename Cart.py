from Item import Item
class Cart:
    # Constructor
    def __init__(self, username: str) -> None:
        self.__username: str = username
        self.__cart: dict = {}

    # Return a deepcopy of the list (python is weird return a deepcopy to be safe)
    def getCart(self) -> dict:
        from copy import deepcopy
        return deepcopy(self.__cart)

    # Add item to Cart
    def addItem(self, new_item: Item, quantity: int) -> None:
        # Since we deepcopy the dict when returning, objects are not the same so check the ID
        for row in self.__cart:
            item: Item = row
            if new_item.getID() == item.getID():
                self.__cart[item] = quantity
                insert_item(new_item.getName(), new_item.getCategory(), quantity, self.__username)
                get_cart()
                return None

        # Otherwise it is a new item (itemID not in cart) so add the item
        self.__cart[new_item] = quantity
        insert_item(new_item.getName(), new_item.getCategory(), quantity, self.__username)

    # Remove an item from the Cart
    def removeItem(self, name: str, category: str) -> bool:
        for row in self.__cart:
            item: Item = row
            if item.getName() == name:
                if item.getCategory() == category:
                    try:
                        del self.__cart[item]
                        remove_item(item.getID(), self.__username)
                        return True
                    except KeyError:
                        return False
        return False
                    

    # Return an item (based on item name and category)
    def getItem(self, name: str) -> 'list[Item]':
        items: list[Item] = []
        for row in self.__cart:
            item: Item = row
            if item.getName() == name:
                items.append(item)

        if len(items) == 0:
            return None
        
        return items

    # Get the quantity of an item (based on name and category)
    def getQuantity(self, name: str, category: str) -> int:
        for row in self.__cart:
            item: Item = row
            if item.getName() == name:
                if item.getCategory() == category:
                    return self.__cart[item]

        return None

    # Load the data from the cart table for the specified user
    def load(self):
        from Item import get_items
        from Inventory import get_inventory
        from typing import Any

        # Grab the cart, inventory, and item data
        cart: list[Any] = get_cart()
        inventory: list[Any] = get_inventory()
        items: list[Any] = get_items()

        # For each row in the cart, if the username in the row is the owner of this cart, check to make sure the itemID is valid and add it to the cart
        for row in cart:
            if row[1] == self.__username:
                for row2 in inventory:
                    if row[2] == row2[0]:
                        for row3 in items:
                            if row3[0] == row2[0]:
                                item = Item(row3[0], row3[1], row3[2], row3[3])
                                quantity: int = row[3]
                                self.addItem(item, quantity)
                                break


# Search for an item based on category and name
def search_item(itemID: int, username: str) -> 'list':
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor
    from typing import Any

    # Connect to the database and create a cursor
    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    # Grab all of the data where the itemID and username match
    query: str = "SELECT * FROM cart WHERE itemID=:itemID AND username=:username"
    c.execute(query, {'itemID': itemID, 'username': username})

    # Grab the rows and commmit all of our changes and close our connection
    tuples: list[Any] = c.fetchall()
    conn.commit()
    conn.close()

    # If we did not grab any rows, we did not find the item
    if len(tuples) == 0:
        return None

    # Return the rows we grabbed
    return tuples

# Insert an item into the cart table
def insert_item(name: str, category: str, quantity: int, username: str) -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor
    from Item import get_items
    from typing import Any

    # Connect to the database and create a cursor
    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    try: 
        # Get the list of items
        items: list[Any] = get_items()
        itemID: int = None

        # Grab the ID of of the item with the correct name and category
        for row in items:
            if row[1] == name:
                if row[3] == category:
                    itemID: int = row[0]

        # Check if the item is in the database
        tuples: list[Any] = search_item(itemID, username)

        # Search returns none if we did not find the item
        if tuples is not None:
            # If we found a row, we have to update it instead
            query: str = f"UPDATE cart SET quantity=:quantity WHERE username=:username"
            c.execute(query, {'quantity': quantity, 'username': username})
            conn.commit()
            conn.close()
            return None
        
        # Insert the item into our database (we do not need a cartID as it is automatically generated)
        query: str = f"INSERT INTO cart (username, itemID, quantity) VALUES (:username, :itemID, :quantity)"
        c.execute(query, {'username': username, 'itemID': itemID, 'quantity': quantity})
        
    except sql.IntegrityError:
        # If we get an integrity error, continue on
        ...

    # Commit our changes and close the database
    conn.commit()
    conn.close()


# Remove an item from the cart table
def remove_item(itemID: int, username: str) -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor
    from typing import Any

    # Connect to the database and create a cursor
    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    try: 
        # Check if the item is in the database
        tuples: list[Any] = search_item(itemID, username)

        # Search returns none if we did not find the item
        if tuples is None:
            # Commit our changes and close the database
            conn.commit()
            conn.close()
            return None

        # Delete all of the rows from the database where the item name and category match
        query: str = f"DELETE FROM cart WHERE itemID=:itemID AND username=:username"
        c.execute(query, {'itemID': itemID, 'username': username})
  
    except sql.IntegrityError:
        # If we get an integrity error, continue on
        ...

    # Commit our changes and close the database
    conn.commit()
    conn.close()


# Grab all of the rows from the cart table
def get_cart() -> list:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor
    from typing import Any

    # Connect to the database and create a cursor
    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    # Query to grab the data
    query: str = "SELECT * FROM cart"
    c.execute(query)

    # Grab the rows and commmit all of our changes and close our connection
    tuples: list[Any] = c.fetchall()
    conn.commit()
    conn.close()

    # Return the rows we grabbed
    return tuples
