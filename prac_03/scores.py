"""Asks user for a number n of scores to be generated.
n random  numbers are generated and are put through the get_user_score
function. The scores along with their results are written to the newly
created results.txt file"""

import random


def main():

    results_file = open('results.txt', 'w')

    number_of_scores = int(input('How many scores: '))

    random_score = random.randint(0, 100)

    for result in range(number_of_scores):
        result = get_user_score(random_score)
        print("{} is {}".format(random_score, result), file=results_file)
        random_score = random.randint(0, 100)

    results_file.close()


"""this function returns the result of the random score passed into the 
function"""


def get_user_score(score):
    if 90 <= score <= 100:
        return "Excellent"
    elif 50 <= score < 90:
        return "Passable"
    elif 50 > score >= 0:
        return "Bad"
    else:
        return "Invalid score"


main()

# """This is a bit of extra code to check the contents of the results.txt file
# created above"""
# my_file = open('results.txt', 'r')
# for line in my_file:
#     print(line)
# my_file.close()
