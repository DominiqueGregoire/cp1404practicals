"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac_06.car import Car


def main():
    """Demo test code to show how to use Car class.
    Create a new Car object called 'limo'"""

    my_car = Car('my_car', 180)
    my_car.drive(30)
    limo = Car('limo', 100)  # limo initialised at 100 units of fuel
    limo.add_fuel(20)  # 20 units of fuel added to limo
    limo.drive(115)   # limo driven 115km
    print("fuel =", my_car.fuel)
    print("fuel =", limo.fuel)
    print("odo =", my_car.odometer)
    print("odo =", limo.odometer)
    print(my_car)
    print(limo)

    print("{} {}, {}".format(my_car.name, my_car.fuel, my_car.odometer))
    print("{self.name} {self.fuel}, {self.odometer}".format(self=my_car))
    print("{self.name} {self.fuel}, {self.odometer}".format(self=limo))


main()
