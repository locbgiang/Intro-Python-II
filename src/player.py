# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item
class Player:
    def __init__(self, playerName, playerLocation, playerItem):
        self.playerName = playerName
        self.playerLocation = playerLocation
        self.playerItem = playerItem
    def __str__(self):
        output = f'{self.playerName} has item: '
        for d in self.playerItem:
            output += d + '. '
        return output
    def addItem(self, newItem):
        self.playerItem.append(newItem)
    def removeItem(self, removingItem):
        self.playerItem.remove(removingItem)
    def checkItem(self, checkingItem):
        exist = False
        for d in self.playerItem:
            if str(d).lower() == str(checkingItem).lower():
                exist = True
        return exist
    def getItemName(self, inputItem):
        for d in self.playerItem:
            if str(d).lower() == str(inputItem).lower():
                name = d
                return name