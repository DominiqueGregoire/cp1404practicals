"""CP1404 prac_08
Taxi simulator program that includes a list of available taxis
for the user to choose from. The user can choose how far to drive
the taxi. The cost of the trip will be shown after each trip and added
to their bill."""

from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


def main():
    current_taxi = None

    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print('Lets Drive!')

    menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()
    # print(menu_choice)

    while menu_choice != "q":
        if menu_choice == "c":
            choose_a_taxi(taxis)
        elif menu_choice == "d":
            pass
        else:
            print("Invalid menu choice.")
        menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()


def choose_a_taxi(taxis):
    """Print a list of available taxis for the user to choose from"""
    for i, taxi in enumerate(taxis):
        print(i, "- {}".format(taxi))


main()
