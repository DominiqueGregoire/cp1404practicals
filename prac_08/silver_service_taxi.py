"""CP1404 practical
Silver Service Taxi Class
"""
from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes fanciness.
    Silver service taxis have a flagfall of $4.50 added to every
    fare."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness=0.0):
        """Initialise a SilverServiceTaxi instance based on Taxi class"""
        super().__init__(name, fuel)
        self.price_per_km = fanciness * self.price_per_km

    def __str__(self):
        """Return a string like a Taxi but with added flagfall."""
        return "{} plus flagfall of {}".format(super().__str__(), self.flagfall)

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.price_per_km * self.current_fare_distance + self.flagfall
