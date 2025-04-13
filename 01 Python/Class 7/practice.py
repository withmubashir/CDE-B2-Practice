# Heirarchial Inheritance
# car -> parent
# sports car -> child
# family car -> child

class car():
    # Class variables
    wheels = 4
    steering = 1
    headlights = 2
    backlights = 2

    # Constructor
    def __init__(self, name : str, model:int, make:str):
        self.name = name
        self.model = model
        self.make = make
        
    # Method with no attributes
    def drive(self):
        return 'Car is moving forward'

    #method with attributes
    def engine_capacity(self, cc : int):
        self.cc = cc

    # calculated methods
    def mileage(self, km : float, avg : float):
        mileage = km * avg
        return mileage

class sports_car(car):
    def __init__(self, doors:int, roof:bool, spoiler:bool):
        self.doors = doors
        self.roof = roof
        self.spoiler = spoiler

    def info(self):
        return (f'{self.name} is a sports car designed by {self.make} in year {self.model} having {self.doors} doors.')
    
cars = car("FXX", 2015, 'Ferrari')
