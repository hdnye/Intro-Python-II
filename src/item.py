# Items that could be found in rooms
    # Mirror
    # Chair
    # Goldust
    # Candle


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        
    def __str__(self):
        return f'{self.name} {self.description}'
    
    def __repr__(self):
        return self.name


class Light(Item):
    def __init__(self, name, description, lights):
        super().__init__(name, description)
        self.lights = lights
     

class Trimmer(Item):
    def __init__(self, name, description, cuts):
        super().__init__(name, description)
        self.cuts = cuts


