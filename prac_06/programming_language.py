"""CP1404 Practical
This is a simple class for a programming language based mostly on the information
found at a Programming Language Comparison page.
For each language the following fields will be stored; typing(static/dynamic),
 reflection(True = yes, False = no) and year."""


class ProgrammingLanguage:

    def __init__(self, typing, reflection, name='', year=0):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        if self.typing == 'dynamic':
            return True
