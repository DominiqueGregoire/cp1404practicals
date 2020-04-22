"""CP1404
Initialise the guitar class, fields will include name, year and cost.
"""

YEAR = 2020  # set the current year as a constant


class Guitar:

    def __init__(self, name='', year=0, cost=0.0):
        """initialise the guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """return string formatting"""
        return "{self.name} ({self.year}) : ${self.cost:.2f}".format(self=self)

    def get_age(self):
        """return the age of the guitar"""
        return YEAR - self.year

    def is_vintage(self):
        """return true if the guitar is vintage
        a guitar is considered vintage if it's age is
        equal to or over 50 years old"""
        return self.get_age() >= 50


def run_tests():
    g1 = Guitar('Gibson L-5 CES', 1922, 16035.40)
    g2 = Guitar('Another Guitar', 2013)
    print(g1)
    print(g2)
    print('{} get_age() - Expected 98. Got {}'.format(g1.name, g1.get_age()))
    print('{} get_age() - Expected 7. Got {}'.format(g2.name, g2.get_age()))
    print('{} is_vintage() - Expected True. Got {}'.format(g1.name, g1.is_vintage()))
    print('{} is_vintage() - Expected False. Got {}'.format(g2.name, g2.is_vintage()))


if __name__ == '__main__':
    run_tests()
