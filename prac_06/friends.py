"""CP1404 prac-06 - practice 1
This is a simple program that will store a list of friends' full names and ages
and display them neatly in a table for a user. The program will ask the user for
the first name, last name and age and will continue until the user enters a blank
name, after which the program will print their friends' details.
"""
from prac_06.person import Person


def main():
    print('My List of Friends')

    friends = []

    first_name = input("First Name: ")
    while first_name != "":
        last_name = (input("Last Name: "))
        age = int(input("Age: "))
        print('{} {}, {} added'.format(first_name, last_name, age))
        friends.append(Person(first_name, last_name, age))
        first_name = input("Name: ")

    print("These are my friends: ")

    for friend in friends:
        print(" {} {}, {} years old".format(friend.first_name, friend.last_name, friend.age))
