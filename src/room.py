# Implement a class to hold room roomDescrmation. This should have name and
# description attributes.
from item import Item
class Room:
    def __init__(self, roomName, roomDesc, roomItem):
        self.roomName = roomName
        self.roomDesc = roomDesc
        self.roomItem = self.init_item(roomItem)
    def __str__(self):
        output = f'{self.roomName}: {self.roomDesc}\n Containing item: '
        for d in self.roomItem:
            output += d.get_itemName() + '. '
        return output

    def init_item(self, roomItem):
        instances = []
        for i, d in enumerate(roomItem):
            instances.append(Item(i,d))
        return instances
    def removeItem(self, deleteItem):
        for d in self.roomItem:
            if d.get_itemName().lower() == deleteItem.lower():
                self.roomItem.remove(d)
    def addItem(self, addingItem):
        for i, d in enumerate(addingItem):
            self.roomItem.append(Item(i, d))
        #return instances
    def checkItem(self, checkingItem):
        exist = False
        for d in self.roomItem:
            if str(d.get_itemName()).lower() == str(checkingItem).lower():
                exist = True
        return exist
    def getItemId(self, inputItem):
        for d in self.roomItem:
            if str(d.get_itemName()).lower() == str(inputItem).lower():
                id = d.getItemId()
                return id
    def getItemName(self, inputItem):
        for d in self.roomItem:
            if str(d.get_itemName()).lower() == str(inputItem).lower():
                name = d.get_itemName()
                return name
        #print('self.roomItem is ',self.roomItem)
        #print('delete item is ', deleteItem)
        #self.roomItem.remove(deleteItem)
