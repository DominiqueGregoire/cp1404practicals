"""CP1404
This program uses a list to store all of the user's guitars.
The user will be asked for the name, year and cost of the guitar.
The user will keep inputting until they enter a blank name, after which
the program will print the guitar details.
"""

from prac_06.guitar import Guitar


def main():
    print('My guitars!')

    guitars = []

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: "))
        print('{} ({}) : ${:.2f} added'.format(name, year, cost))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ")

    # guitars.append(Guitar("Gibson L5- CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    print("These are my guitars: ")

    for i, guitar in enumerate(guitars, 1):
        if guitar.is_vintage():
            vintage_string = "(vintage)"
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}{}".format(i, guitar.name, guitar.year, guitar.cost,
                                                                      vintage_string))
        else:
            print("Guitar {}: {:>20} ({}), worth ${:10,.2f}".format(i, guitar.name, guitar.year, guitar.cost))


main()
