"""CP1404 practicals
Tests for Taxi"""
from prac_08.silver_service_taxi import SilverServiceTaxi


def run_tests():
    """Test Taxi class"""
    hummer = SilverServiceTaxi("Hummer", 200, 4)
    print(hummer)
    sstaxi1 = SilverServiceTaxi("sstaxi 1", 100, 2)
    sstaxi1.drive(18)
    print("price per km should be 2.46 got {}".format(sstaxi1.price_per_km))
    print("Fanciness of 2, price per km should be 2.46 got {}".format(sstaxi1.price_per_km))
    print("flagfall should be 4.50 got {:.2f}".format(sstaxi1.flagfall))
    print("fare should be 48.78 got {:.2f}".format(sstaxi1.get_fare()))


run_tests()
