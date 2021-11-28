class Inventory:
    #constructor
    def __init__(self, Itemname: str) -> None:
        self.Itemname = Itemname

    #Add item to Inventory
    def addItem(self, Itemname: str) ->None:
        if self.Itemname != Itemname:
            self.Itemname = Itemname
        else:
            print("Item Already in Inventory")

    #return an item(based on item name)
    def getItem(self, name) -> str:
        if self.Itemname == name:
            return self.__Itemname
        else:
            print("Item is not in Inventory")