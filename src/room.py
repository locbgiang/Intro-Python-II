# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, location, info):
        self.location = location
        self.info = info
    def __str__(self):
        return f'You are currently in room {self.location}, {self.info}'