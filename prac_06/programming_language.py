"""CP1404 Practical
This is a simple class for a programming language based mostly on the information
found at a Programming Language Comparison page.
For each language the following fields will be stored; typing(static/dynamic),
 reflection(True = yes, False = no) and year."""


class ProgrammingLanguage:

    def __init__(self, name='', typing='', reflection='', year=0):
        self.reflection = reflection
        self.name = name
        self.typing = typing
        self.year = year

    def __str__(self):
        return "{self.name}, {self.typing} Typing, Reflection={self.reflection}, First " \
               "appeared in {self.year}".format(self=self)

    def is_dynamic(self):
        return self.typing == 'Dynamic'


def run_tests():
    lang1 = ProgrammingLanguage()
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(lang1)
    print(python)

    """To ensure that the is_dynamic function returns get what is expected"""
    print('{} is_dynamic - Expected True. Got {}'.format(python.name, python.is_dynamic()))
    print('{} is_dynamic - Expected False. Got {}'.format(visual_basic.name, visual_basic.is_dynamic()))

    languages = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in languages:
        # print(language)
        if language.is_dynamic():
            print(language.name)


if __name__ == '__main__':
    run_tests()
