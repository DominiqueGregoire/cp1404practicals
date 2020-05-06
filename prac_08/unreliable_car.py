"""CP1404 practical
Unreliable Car Class
"""

from prac_08.car import Car


class UnreliableCar(Car):
    """Specialised version of Car that includes reliability percentage"""

    def __init__(self, name, fuel, percent_reliable=0.0):
        """Initialise an UnreliableCar instance based on Car class"""
        super().__init__(name, fuel)
        self.initial_distance = 0
        self.percent_reliable = percent_reliable

    def __str__(self):
        """Return a string like a Car but with reliability."""
        return "{}, reliability {}%".format(super().__str__(), self.percent_reliable)

    def drive(self, distance):
        """Drive like parent Car but determine whether the car actually
        drove or not.  Generate a random number between 0 and 100. Car
        will only drive if random number is less than reliability. Car will
        return zero distance if random number is greater than or equal to
        reliability
        :returns distance_driven or 0
        """
        from random import randint
        random_number = randint(0, 100)

        print("random number is ", random_number)
        if random_number < self.percent_reliable:
            distance_driven = super().drive(distance)
            self.initial_distance += distance_driven
            return distance_driven
        else:
            distance_driven = 0
            return distance_driven
