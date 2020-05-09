"""CP1404 prac_08
Taxi simulator program that includes a list of available taxis
for the user to choose from. The user can choose how far to drive
the taxi. The cost of the trip will be shown after each trip and added
to their bill."""

from prac_08.silver_service_taxi import SilverServiceTaxi
from prac_08.taxi import Taxi


def main():
    current_taxi = None
    bill_to_date = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    print('Lets Drive!')

    menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    while menu_choice != "q":
        if menu_choice == "c":
            display_available_taxis(taxis)
            chosen_taxi = int(input("Choose taxi: "))
            current_taxi = taxis[chosen_taxi]

        elif menu_choice == "d":
            current_taxi.start_fare()
            distance = float(input("Drive how far? "))
            current_taxi.drive(distance)
            print("Your {} trip cost you ${:.2f}".format(current_taxi.name, current_taxi.get_fare()))
            bill_to_date += current_taxi.get_fare()

        else:
            print("Invalid menu choice.")

        print("Bill to date: ${:.2f}".format(bill_to_date))
        menu_choice = input("q)uit, c)hoose taxi, d)rive\n>>> ").lower()

    if menu_choice == "q":
        print("Total trip cost: ${:.2f}".format(bill_to_date))
        print("Taxis are now:")
        display_available_taxis(taxis)


def display_available_taxis(taxis):
    """Print a list of available taxis for the user to choose from"""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(i, "- {}".format(taxi))


main()
