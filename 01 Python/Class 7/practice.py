# Heirarchial Inheritance
# car -> parent
# sports car -> child
# family car -> child

# Parent Class
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

# Child Class
class sports_car(car):
    def __init__(self, name : str, model:int, make:str, doors:int, roof:bool, spoiler:bool):
        super().__init__(name, model, make) # car.__init__(self, name, model, year) -> another way to initialize constructor
        self.doors = doors
        self.roof = roof
        self.spoiler = spoiler

    def info(self):
        return (f'{self.name} is a sports car designed by {self.make} in year {self.model} having {self.doors} doors.')

# Child Class
class family_car(car):
    def __init__(self, seats, doors, airbag):
        pass
    
cars = car("FXX", 2015, 'Ferrari')
ferrari = sports_car(2, True, True)
print(cars.model)