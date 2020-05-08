"""CP1404 practicals
Tests for Taxi"""
from prac_08.taxi import Taxi


def run_tests():
    """Test Taxi class"""
    taxi1 = Taxi("Prius 1", 100)
    print(taxi1)
    taxi1.drive(4)
    print(taxi1.__str__())
    print("cost of trip should be 4 * {} = 4.92 rounded up should be 4.90 "
          "got {:.2f}".format(taxi1.price_per_km, taxi1.get_fare()))
    taxi1.start_fare()
    print(taxi1.__str__())
    taxi1.drive(100)
    print(taxi1.__str__())




run_tests()
