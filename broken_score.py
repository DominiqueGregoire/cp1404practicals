"""
CP1404/CP5632 - Practical
Broken program to determine score status.
Once fixed this will allow a user to input
a score and print out the result
"""


def main():
    score = float(input("Enter score: "))

    result = get_user_score(score)
    print("{}\t {}".format(score, result))


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
