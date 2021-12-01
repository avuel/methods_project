class Item:
    def __init__(self, itemId: int, name: str, unitCost: float, category: str, stock: int) -> None:
        self.__itemID: int = None
        self.__name: str = name
        self.__unitCost: float = unitCost
        self.__category: str = category
        self.__stock: int = stock

    def getCategory(self) -> str:
        return self.__category

    def getUnitCost(self) -> float:
        return self.__unitCost

    def getStock(self) -> int:
        return self.__stock

    def setStock(self, stock: int) -> None:
        self.__stock = stock
        
