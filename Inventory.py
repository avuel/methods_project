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
   
