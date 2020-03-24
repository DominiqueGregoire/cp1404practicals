"""asks the user how many "quick picks" they wish to generate. The program then generates that
many lines of output. Each line consists of 6 random numbers between 1 and 45.
pseudocode
get number of quick picks
create a list to hold each quick pick line
generate a random no x 6 to make the line
print the line
repeat this x number of quick picks"""

from random import randint

NUMBERS_PER_LINE = 6
MAXIMUM = 45
MINIMUM = 1


def main():
    amount = int(input("How many quick picks? "))

    while amount < 0:                         # check for invalid amount of quick picks
        print("Invalid amount")
        amount = int(input("How many quick picks? "))

    for i in range(amount):
        quick_pick_lines = []
        for number in range(NUMBERS_PER_LINE):    # create a list of 6 random numbers between 1 and 45
            number = randint(MINIMUM, MAXIMUM)
            if number in quick_pick_lines:
                number = randint(MINIMUM, MAXIMUM)
            quick_pick_lines.append(number)

        # print(quick_pick_lines)
        quick_pick_lines.sort()
        # print(quick_pick_lines)
        # quick_pick_lines = [str(number) for number in quick_pick_lines]
        # print(quick_pick_lines)
        # print(' '.join(quick_pick_lines))
        print(' '.join('{:2}'.format(number) for number in quick_pick_lines))










main()
