"""CP1404 prac-06 - practice 2
This is a car driving simulator program that uses the Car class.
The user is given a menu with drive, refuel or quit as options.
The simulator ends when the user chooses quit.
Fuel is initialised at 100units.
"""

from prac_06.car import Car


def main():
    MENU = "Menu:\nd) drive\nr) refuel\nq) quit"
    print("Let's Drive!")
    # my_car = input("Enter your car name: ")
    my_car = "The Bomb"
    my_car = Car(my_car, 100)
    print(my_car)

    # print(MENU)
    # choice = input("Enter your choice: ").lower()
    # while choice != "q":
    #     if choice == "d":
    #         drive_car(my_car)
    #     else:
    #         print("Invalid choice")
    #     print(MENU)
    #     choice = input("Enter your choice: ").lower()

    # def drive_car(car):
    distance = int(input("How many km do you wish to drive? "))
    print("The car drove {}km".format(my_car.drive(distance)))
    distance_left = my_car.odometer - distance
    distance_left = my_car.odometer
    print("distance = 20: expect distance to be 80 got {}".format(distance_left))
    print("odometer should be 80, got {}".format(my_car.odometer))


# def fuel_remaining(car, distance):
#     fuel = car.fuel - distance
#     return fuel

main()
