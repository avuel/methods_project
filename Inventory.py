from Item import Item, get_items

class Inventory:
    # Constructor
    def __init__(self) -> None:
        self.__items = {}

    def getInv(self):
        from copy import deepcopy
        return deepcopy(self.__items)

    # Add item to Inventory
    def addItem(self, new_item: Item, stock: int) -> bool:
        new_name: str = new_item.getName()
        new_category: str = new_item.getCategory()
        for row in self.__items:
            item: Item = row
            if item.getName() == new_name:
                if item.getCategory() == new_category:
                    return None
        self.__items[new_item] = stock

    # Return an item (based on item name and category)
    def getItem(self, name: str) -> 'list[Item]':
        items: list[Item] = []
        for item in self.__items:
            if item.getName() == name:
                items.append(item)

        if len(items) == 0:
            return None
        
        return items

    def load(self):
        from typing import Any
        from Item import get_items
        items: list[Any] = get_items()
        inventory: list[Any] = get_inventory()
        for row in inventory:
            for row2 in items:
                if row[0] == row2[0]:
                    item = Item(row2[0], row2[1], row2[2], row2[3])
                    stock: int = row[1]
                    self.addItem(item, stock)

def load_db() -> None:
        import sqlite3 as sql
        from sqlite3.dbapi2 import Connection, Cursor
        from typing import Any

        try:
            # Connect to the database and create a cursor
            conn: Connection = sql.connect('e-commerce.db')
            c: Cursor = conn.cursor()
            items: list[Any] = get_items()
            stock: int = 1

            for item in items:
                # Insert the item into our database (we do not need an itemID as it is automatically generated)
                query: str = f"INSERT INTO inventory (itemID, stock) VALUES (:itemID, :stock)"
                c.execute(query, {'itemID': item[0], 'stock': stock})
                stock: int = stock * 5
        
        except sql.IntegrityError:
            # If we get an integrity error, continue on
            ...

        # Commit our changes and close the database
        conn.commit()
        conn.close()

# Insert an item into the items table
def insert_item(name: str, category: str, unitCost: float) -> None:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor


    # Connect to the database and create a cursor
    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    try: 
        # Insert the item into our database (we do not need an itemID as it is automatically generated)
        query: str = f"INSERT INTO inventory (itemID, stock) VALUES (:itemID, :stock)"
        c.execute(query, {'name': name, 'unitCost': unitCost, 'category': category})
  
    except sql.IntegrityError:
        # If we get an integrity error, continue on
        ...

    # Commit our changes and close the database
    conn.commit()
    conn.close()


# Grab all of the rows from the inventory table
def get_inventory() -> list:
    import sqlite3 as sql
    from sqlite3.dbapi2 import Connection, Cursor
    from typing import Any

    # Connect to the database and create a cursor
    conn: Connection = sql.connect('e-commerce.db')
    c: Cursor = conn.cursor()

    query: str = "SELECT * FROM inventory"
    c.execute(query)

    # Grab the rows and commmit all of our changes and close our connection
    tuples: list[Any] = c.fetchall()
    conn.commit()
    conn.close()

    # Return the rows we grabbed
    return tuples
