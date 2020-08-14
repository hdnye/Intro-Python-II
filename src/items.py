# Items that could be found in rooms
    # Mirror
    # Chair
    # Goldust
    # Candle


class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Light(Items):
    def __init__(self, name, description, lights):
        super().__init__(name, description)
        self.lights = lights
     
candle = Light('Candle', 'Lights the way', True)
flashlight = Light('Flash')

class Trimmer(Items):
    def __init__(self, name, description, cuts):
        super().__init__(name, description)
        self.cuts = cuts

trimmer = Trimmer('Trimmer', 'Gardening tool', True)

