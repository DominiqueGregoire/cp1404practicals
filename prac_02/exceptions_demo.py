"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
when the user inputs the word "two" instead of the number "2", when the user hits the enter without entering anything
and when the user inputs any other character eg ? % /
2. When will a ZeroDivisionError occur?
when the programs asks the user to input the denominator, if the user inputs the number "0", then a ZeroDivisionError
will occur.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
yes by changing denominator = int(input("Enter the denominator: ")) to denominator = int(input("Enter the denominator
(please note - denominator cannot be the number zero '0'): "))
"""

try:
    numerator = int(input("Enter the numerator: "))
    # change the code so that the user is aware to not input the number zero
    denominator = int(input("Enter the denominator (please note - denominator cannot be the number zero '0') : "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")






