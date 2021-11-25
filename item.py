# Item Class
class Item:
    # Constructor for the Item Class
    def __init__(self, itemId: int, name: str, unitCost: float, category: str, stock: int) -> None:
        self.__itemID: int = None
        self.__name: str = name
        self.__unitCost: float = unitCost
        self.__category: str = category
        self.__stock: int = stock

    # Get the Category of an Item
    def getCategory(self) -> str:
        return self.__category

    # Get the Unit Cost of an Item
    def getUnitCost(self) -> float:
        return self.__unitCost

    # Get the Stock of an Item
    def getStock(self) -> int:
        return self.__stock

    # Set the Stock of an Item
    def setStock(self, stock: int) -> None:
        self.__stock = stock
