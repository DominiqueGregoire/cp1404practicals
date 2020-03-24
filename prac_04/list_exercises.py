"""Will ask user to input 5 numbers which will be stored in a list. Some
basic list operations will be performed on the numbers"""


def main():
    numbers = []

    for num in range(5):
        num = int(input("Number: "))
        numbers.append(num)

    print('The first number is {}'.format(numbers[0]))
    print('The last number is {}'.format(numbers[-1]))
    print('The smallest number is {}'.format(min(numbers)))
    print('The largest number is {}'.format(max(numbers)))
    print('The average of the numbers is {}'.format(sum(numbers) / len(numbers)))

    """part 2:
    Security checker added"""

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
             'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
             'StartServer', 'bob']

    name = input("Enter username: ")
    if name in usernames:
        print("Access granted")
    else:
        print("Access denied")


main()
