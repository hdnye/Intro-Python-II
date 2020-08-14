from room import Room
from player import Player
from item import Item

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
room["treasure"].s_to = room["narrow"]


room['outside'].item.append(Item('Knife:', 'Used to cutting or stabbing'))
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
    print('The room contains the following items:')
    for item in current_room.items:
        print(item)
    user_input = input("Choose a direction to move in ('n', 's', 'e', 'w'): or get an item\n")    
    attribute = f"{user_input}_to"   
# If the user enters a cardinal direction, attempt to move to the room there.
    if hasattr(current_room, attribute):
        player1.current_room = getattr(current_room, attribute)               
    # # Print an error message if the movement isn"t allowed.
    else:
        print("That is not a valid direction, please choose again")
        continue
# # If the user enters "q", quit the game.
    if user_input == "q":
            break   

# original code block
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