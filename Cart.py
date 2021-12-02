from Item import Item
import sqlite3

class CartList():
    def __init__(self, Username: str, cartId: int, itemId: Item, quantity: int) -> None:
        self.__Username: int = Username
        self.__cartId: int = cartId
        self.__itemId: Item = itemId
        self.__quantity: int = quantity
        
    def getCartID(self) -> int:
        return self.__cartId
        
    def getUsername(self) -> int:
        return self.__Username
        
    def getItemList(self) -> int:
        return self.__Username
        
    def updateQuantity(self,quantity: int) -> None:
        self.__quantity=quantity

#cart Class
class Cart:
    # Constructor for the Cart Class
    def __init__(self) -> None:
        self.__cartitems= []           
        
    # Change how the Cart is printed
    def __repr__(self) -> None:
        repr(self.__cartitems)
        
    # Add item to Cart
    def addItem(self, Username: str, cartId: int, itemId: Item, quantity: int) -> bool:
        self.__cartitems.append(CartList(Username,cartId,itemId,quantity))
        
    #update quantity
    def updateQuanity(self,Username: str,cartId: int,quantity:int)->None:
        for cartlist in self.__cartitems:
            if cartlist.getCartID() == cartId:
                cartlist.updateQuantity(quantity)
                
    #update quantity
    def removeItem(self,Username: str,cartId: int)->None:
        for cartlist in self.__cartitems:
            if cartlist.getCartID() == cartId:
                cartlist.remove(cartlist)
        
    #checkout
    def checkOut(self,Username: str)->Item:
        itemlist = []
        for cartlist in self.__cartitems:
            if cartlist.getUsername() == Username:
                itemlist.append(cartlist.getItemList())
