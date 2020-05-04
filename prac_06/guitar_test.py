"""CP1404
This is a testing file for testing the Guitar class.
guitar1 and guitar2 are two objects to test display, get_age
and is_vintage method functions.
"""

from prac_06.guitar import Guitar


def main():
    guitar1 = Guitar('Gibson L-5 CES', 1922, 16035.40)
    guitar2 = Guitar('Another Guitar', 2013)
    print(guitar1)
    print(guitar2)
    print('{} get_age() - Expected 98. Got {}'.format(guitar1.name, guitar1.get_age()))
    print('{} get_age() - Expected 7. Got {}'.format(guitar2.name, guitar2.get_age()))
    print('{} is_vintage() - Expected True. Got {}'.format(guitar1.name, guitar1.is_vintage()))
    print('{} is_vintage() - Expected False. Got {}'.format(guitar2.name, guitar2.is_vintage()))


main()
