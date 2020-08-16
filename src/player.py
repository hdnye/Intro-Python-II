# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, current_room):
        self.current_room = current_room
        self.backpack = []
   
    def take(self, item):
        self.backpack.append(item)
    
    def drop(self, item):
        self.backpack.remove(item)
  
    def inventory(self):
        print('Inventory:', self.backpack)
        print('\n')


    