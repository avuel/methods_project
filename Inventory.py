from Item import Item

class Inventory:
    # Constructor
    def __init__(self) -> None:
        self.__items = {}

    # Change how the Inventory is printed
    def __repr__(self) -> None:
        repr(self.__items)

    # Add item to Inventory
    def addItem(self, new_item: Item, stock: int) -> bool:
        new_name: str = new_item.getName()
        new_category: str = new_item.getCategory()
        for item in self.__items:
            if item.getName() == new_name:
                if item.getCategory() == new_category:
                    print(f"The item {new_name} of the category {new_category} is already in the inventory")
                    return None
        self.__items[new_item] = stock

    # Return an item (based on item name and category)
    def getItem(self, name: str, category: str) -> Item:
        for item in self.__items:
            if item.getName() == name:
                if item.getCategory() == category:
                    return item
        print(f"The item {item} of the category {category} is not in the inventory")
        return None
   
    def load_db(self) -> None:
        import sqlite3 as sql
        from sqlite3.dbapi2 import Connection, Cursor
        from Item import Item

        try:
            # Connect to the database and create a cursor
            conn: Connection = sql.connect('e-commerce.db')
            c: Cursor = conn.cursor()

            for item in self.__items:
                current_item: Item = item
                # Insert the item into our database (we do not need an itemID as it is automatically generated)
                query: str = f"INSERT INTO items (itemID, stock) VALUES (:itemID, :stock)"
                c.execute(query, {'itemID': current_item.getID(), 'stock': self.__items[item]})
        
        except sql.IntegrityError:
            # If we get an integrity error, print that we failed to insert the item
            print("Failed to insert an item into the inventory", end="\n\n")

        # Commit our changes and close the database
        conn.commit()
        conn.close()
            

def load_inventory() -> Inventory:
    from typing import Any
    from Item import get_items

    items: list[Any] = get_items()
    inventory: Inventory = Inventory()
    stock: int = 1
    for item in items:
        inventory.addItem(Item(item[0], item[1], item[2], item[3]), stock)
        stock: int = stock + 1

