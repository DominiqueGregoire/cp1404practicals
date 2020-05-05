"""CP1404 practicals
Tests for Taxi"""
from prac_08.taxi import Taxi


def run_tests():
    """Test Taxi class"""
    taxi1 = Taxi("Prius 1", 100)
    taxi1.drive(40)
    print(taxi1.__str__())
    taxi1.start_fare()
    print(taxi1.__str__())
    taxi1.drive(100)
    print(taxi1.__str__())


run_tests()
