from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     """North of you, the cave mount beckons""", ['Spellbook']),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ['Sword', 'Spear']),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", []),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", []),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#
def try_direction(player, direction):
    attribute = direction + '_to'

    if hasattr(player.playerLocation, attribute):
        player.playerLocation = getattr(player.playerLocation, attribute)
    else:
        print("There is nothing in that direction!")

# Make a new player object that is currently in the 'outside' room.
player1 = Player('Loc', room['outside'], [])
#player1.playerItem = room['outside'].get_item()

#player1.addItem(room['foyer'].roomItem[0])
#room['foyer'].removeItem('Sword')

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print(player1.playerLocation)
    print(player1)
    command = input('\nCommand: ').split()

    #print('first letter of first word', command[0][0])
    
    # if command == get sword and there is sword in room then pick up sword
    # if command == drop sword and there is sword in inventory then drop sword

    #command = command[0].lower()
    if (command[0] == 'get' and len(command) == 2):
        if player1.playerLocation.checkItem(command[1]):
            itemName = player1.playerLocation.getItemName(command[1])
            player1.addItem(itemName)
            player1.playerLocation.removeItem(command[1])
        else:
            print('There is no item with that name in this room')
    if (command[0] == 'drop' and len(command) == 2):
        if player1.checkItem(command[1]):
            itemName = player1.getItemName(command[1])
            player1.playerLocation.addItem([itemName])
            player1.removeItem(itemName)
        else:
            print('There is no item with that name in the inventory')
        '''    itemName = player1.playerLocation.getItemName(command[1])
            player1.addItem(itemName)
            player1.playerLocation.removeItem(command[1])
        else:
            print('There is no item with that name in this room')
        '''
    movement = command[0][0].lower()
    if movement == 'q':
        break

    if movement == 'n':
        try_direction(player1, movement)
    elif movement == 's':
        try_direction(player1, movement)
    elif movement == 'e':
        try_direction(player1, movement)
    elif movement == 'w':
        try_direction(player1, movement)
    

#player1.addItem(room['foyer'].roomItem[0])
#room['foyer'].removeItem('Sword')