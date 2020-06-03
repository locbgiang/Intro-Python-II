# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player(Room):
    def __init__(self, playerName, location, info ):
        self.playerName = playerName
        super().__init__(location, info)