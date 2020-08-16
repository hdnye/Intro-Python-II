from room import Room
from player import Player
from item import Item, Light, Trimmer


"""
# First goal is to make items
# 
"""
# Declare all the rooms

# Dictionary of rooms mapping name to Room 
room = {
    "outside":  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    "foyer":    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    "overlook": Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    "narrow":   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    "treasure": Room("Treasure Chamber", """You"ve found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}



# Link rooms together




room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["overlook"].s_to = room["narrow"]


# create a dictionary of items
dictionary = {
    'item' : 'item object'
}

stuff = {
    'Candle' : Item('Candle', 'Lights the way'),
    'Flash' : Light('Flash', 'Shines brightly', True),
    'Clippers' : Item('Clippers', 'Gardening tool'),
    'Knife' : Trimmer('Knife', 'Stabby thing', True),
    'Sword' : Trimmer('Sword', 'Stabby thing', True)
    
}



items = {
    'candle' : Item('Candle', 'Lights the way'),
    'sword': Item('sword', 'It looks rusty. Don\'t get tetanus!'),
    'coin': Item('coin', 'Is that gold!! Oh no wait... it is silver.'),
    'knife': Item('knife', 'Ouch sharp!'),
    'bat': Item('bat', 'Don\'t know why you would take a live animal but ok.'),
    'glock': Item('glock', "A shiny glock lays on your path"),
    'Flash' : Light('Flash', 'Shines brightly', True),
    'Clippers' : Item('Clippers', 'Gardening tool'),
    'Knife' : Trimmer('Knife', 'Stabby thing', True),
    'Sword' : Trimmer('Sword', 'Stabby thing', True)
}

# Link items to rooms
room['foyer'].items = [items['sword'], items['coin'], items['candle'], items['Flash']]
room['overlook'].items = [items['knife']]
room['narrow'].items = [items['bat']]
room['outside'].items = [items['glock'], items['glock']]


#
# Main
#

# Make a new player object that is currently in the "outside" room.n

player1 = Player(room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True: 
    current_room = player1.current_room
    
    print("player1", player1.current_room.name) 
    print("player1", player1.current_room.description)
    
    # Print items in the room 
    
    print('The room contains the following items:', player1.current_room.items)
    user_input = input("Choose a direction to move in ('n', 's', 'e', 'w'): or get an item\n")    
    attribute = f"{user_input}_to"   
    
    # If the user enters a cardinal direction, attempt to move to the room there.
    
    if hasattr(current_room, attribute):
        player1.current_room = getattr(current_room, attribute)               
    
    
    elif 'take' in user_input or 'drop' in user_input:
        action = user_input.split()
        verb = action[0]
        noun = action[1]

        if verb == 'take':
            
            # if the verb is take
            # place the item in the players backpack
            # removve the item from the room
            player1.take(items[noun])
            player1.current_room.removed(items[noun])
            

    
        # if the verb is drop
        # remove the item in the players backpack
        # place the item in the room 
        
    # # If the user enters "q", quit the game.
    elif user_input == "q":
        break   

    elif user_input == "i":
        player1.inventory()
        
    # # Print an error message if the movement isn"t allowed
    else:
        print("That is not a valid direction, please choose again")
        continue

# original code block - works but not dry
    # if user_input == "n":
    #     if hassattr(current_room, "n_to"):
    #         player1.current_room = getattr(current_room, attribute)
    # if user_input == "s":
    #     if hasattr(current_room, "s_to"):
    #         player1.current_room = getattr(current_room, attribute)
    # if user_input == "e":
    #     if hasattr(current_room, "e_to"):
    #         player1.current_room = getattr(current_room, attribute)
    # if user_input == "w":
    #     if hasattr(current_room, "w_to"):
    #         player1.current_room = getattr(current_room, attribute)
 
 # PLAN
# 1) Create room class with name and description
# rooms are already linked
# 2) create a player object
# 3) figure out movement hasattr getattr