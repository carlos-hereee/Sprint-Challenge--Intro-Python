# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.


class GroundVehicle():
    def __init__(self, name,  num_wheels=4):
        # change it so the num_wheels defaults to 4 if not specified
        # self.num_wheels = num_wheels
        self.num_wheels = num_wheels
        self.name = name

    # Todo add method drive() that returns "vroooom".
    def drive(self):
        return f'vroooom'


g = GroundVehicle('ground unit')
print('\nnumber of wheels is 4', g.num_wheels)
print('\nground unit goes', g.drive())

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"


# Todo # Subclass Motorcycle from GroundVehicle.
class Motorcycle(GroundVehicle):
    # #of wheels to 2
    def __init__(self, name,  num_wheels=2):
        super().__init__(num_wheels)
        self.name = name

    # Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

    def drive(self):
        return f'BRAAAP'


m = Motorcycle('motorcycle')
print('\nmotercycle # of wheels is 2', m.num_wheels)
print('\nmotercycle goes', m.drive())

vehicles = [
    GroundVehicle('ground unit'),
    GroundVehicle('ground unit'),
    Motorcycle('motorcycle'),
    GroundVehicle('ground unit'),
    Motorcycle('motorcycle'),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO

for vehicle in vehicles:
    print(f'\n and this {vehicle.name} goes', vehicle.drive())
