# To the GroundVehicle class, add method drive() that returns "vroooom".
#
# Also change it so the num_wheels defaults to 4 if not specified when the
# object is constructed.


class GroundVehicle():
    def __init__(self,  num_wheels=4):
        # change it so the num_wheels defaults to 4 if not specified
        # self.num_wheels = num_wheels
        self.num_wheels = num_wheels

    # Todo add method drive() that returns "vroooom".
    def drive(self):
        return f'vroooom'


print('\nnumber of wheels is 4', GroundVehicle().num_wheels)
print('\nground unit goes', GroundVehicle().drive())

# Subclass Motorcycle from GroundVehicle.
#
# Make it so when you instantiate a Motorcycle, it automatically sets the number
# of wheels to 2 by passing that to the constructor of its superclass.
#
# Override the drive() method in Motorcycle so that it returns "BRAAAP!!"


# Todo # Subclass Motorcycle from GroundVehicle.
class Motorcycle(GroundVehicle):
    # #of wheels to 2
    def __init__(self,  num_wheels=2):
        super().__init__(num_wheels)

    # Override the drive() method in Motorcycle so that it returns "BRAAAP!!"

    def drive(self):
        return f'BRAAAP!!'


print('\nmotercycle # of wheels is 2', Motorcycle().num_wheels)
print('\nmotercycle goes', Motorcycle().drive())

vehicles = [
    GroundVehicle(),
    GroundVehicle(),
    Motorcycle(),
    GroundVehicle(),
    Motorcycle(),
]

# Go through the vehicles list and print the result of calling drive() on each.

# TODO

for vehicle in vehicles:
    print(f'\n and this vehicle goes', vehicle.drive())
