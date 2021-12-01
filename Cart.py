#cart Class
class Cart:
    #constructor
    def __init__(self,username:str,cartId:int,productID:int,quantity:int,dateAdded)->None:
        self.username=username
        self.cartId=cartId
        self.productID=productID
        self.quantity=quantity
    #add card item
    def addCartitem(self,cartId:int)->None:
        self.cartId=cartId
    #update quantity
    def updateQuanity(self,quantity:int)->None:
        self.quantity=quantity
    #checkout
    def checkOut(self)->None:
        pass
