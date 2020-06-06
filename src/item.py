class Item:
    def __init__(self, itemId, itemName):
        self.itemId = itemId
        self.itemName = itemName
    def __str__(self):
        return f'{self.itemName}'
    def get_itemName(self):
        return self.itemName
    def getItemId(self):
        return self.itemId
    
