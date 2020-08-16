# Implement a class to hold room information. This should have name and
# description attributes.
# The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
# which point to the room in that respective direction.


from item import Item

class Room: 
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to: Room = None
        self.s_to: Room = None
        self.e_to: Room = None
        self.w_to: Room = None
        self.items: [] 

    def remove(self, item):
        self.items.remove(item)
    
    def append(self, item):
        self.items.append(item)

