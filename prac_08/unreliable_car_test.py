"""CP1404 practicals
Tests for Unreliable Car"""
from prac_08.unreliable_car import UnreliableCar


def run_tests():
    """Test UnreliableCar class"""
    unreliable0 = UnreliableCar("", 0, 0.0)
    print(unreliable0.__str__())
    unreliable1 = UnreliableCar("Da bomb", 100, 50.0)
    print(unreliable1.__str__())
    unreliable1.drive(40)
    print(unreliable1.__str__())
    unreliable1.drive(20)
    print(unreliable1.__str__())


run_tests()
