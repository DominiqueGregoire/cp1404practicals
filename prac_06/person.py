"""CP1404 prac-06 - practice 1
Initialise Person class to take first and last names and age
as fields"""


class Person:
    """Represent the Person object"""

    def __init__(self, first_name="", last_name="", age=0):
        """Initialise the person instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def __str__(self):
        """Return string formatting"""
        return "{self.first_name} {self.last_name} {self.age}".format(self=self)


def run_tests():
    p1 = Person("Jane", "Doe", 18)
    print(p1)


if __name__ == '__main__':
    run_tests()
