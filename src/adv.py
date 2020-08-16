from room import Room
from player import Player
from item import Item, Light, Trimmer

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

# Create dictionary of items
items = {
    'Candle': Light('Candle','Lights the way', True),
    'Flash': Light('Flash', 'Shines brightly', True),
    'Clippers': Trimmer('Clippers', 'Gardening tool', True),
    'Knife': Trimmer('Knife', 'Stabby thing', True)
}

# Link rooms together

room["outside"].n_to = room["foyer"]
room["foyer"].s_to = room["outside"]
room["foyer"].n_to = room["overlook"]
room["foyer"].e_to = room["narrow"]
room["overlook"].s_to = room["foyer"]
room["narrow"].w_to = room["foyer"]
room["narrow"].n_to = room["treasure"]
room["treasure"].s_to = room["narrow"]


room['outside'].items = [items['Candle']]
#
# Main
#

# Make a new player object that is currently in the "outside" room.n

Heather = Player(room["outside"])

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
while True: 
    current_room = Heather.current_room
    print("Heather", Heather.current_room.name) 
    print("Heather", Heather.current_room.description)

# Print items in the room 
    print('The room contains the following items:', current_room.items)   
    user_input = input("Choose a direction to move in ('n', 's', 'e', 'w') or get an item\n")    
    attribute = f"{user_input}_to"   

# # If the user enters "q", quit the game.
    if user_input == "q":
        break

    elif user_input == 'i':
        Heather.inventory()

# If the user enters a cardinal direction, attempt to move to the room there.
    if hasattr(current_room, attribute):
        Heather.current_room = getattr(current_room, attribute)     
   
    elif 'take' in user_input or 'drop' in user_input: 
        action = user_input.split()
        verb = action[0]
        noun = action[1]

        if verb == 'take':                
            # if the verb is take
            # removethe item in the players backpack
            # add item from the room
            Heather.current_room.remove(items[noun])
            Heather.take(items[noun])

        print(items[noun])


        if verb == 'drop':
            # if the verb is drop
            # place the item in the players backpack
            # remove item from the room
            Heather.current_room.append(items[noun])
            Heather.drop(items[noun])

        print(items[noun])

    # # Print an error message if the movement isn"t allowed.
    else:
        print("That is not a valid direction, please choose again")
        continue

 
# original code block - works but not dry
    # if user_input == "n":
    #     if hassattr(current_room, "n_to"):
    #         Heather.current_room = getattr(current_room, attribute)
    # if user_input == "s":
    #     if hasattr(current_room, "s_to"):
    #         Heather.current_room = getattr(current_room, attribute)
    # if user_input == "e":
    #     if hasattr(current_room, "e_to"):
    #         Heather.current_room = getattr(current_room, attribute)
    # if user_input == "w":
    #     if hasattr(current_room, "w_to"):
    #         Heather.current_room = getattr(current_room, attribute)
 
 # PLAN
# 1) Create room class with name and description
# rooms are already linked
# 2) create a player object
# 3) figure out movement hasattr getattr
