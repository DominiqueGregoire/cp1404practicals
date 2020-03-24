"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random

MAX_INCREASE = 0.1  # 10%
MAX_DECREASE = 0.05  # 5%
MIN_PRICE = 0.01
MAX_PRICE = 1000.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "stock_price_simulator.txt"  # name of output file

price = INITIAL_PRICE
print("${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    print("${:,.2f}".format(price))
    print()

# things to do no 1. add a day counter and format the output
# initialise a loop count as 0
# loop count will count each instance and will help the user see the price on a particular instance
loop_count = 0
price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    loop_count += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)

    print("On day {} price is: ${:,.2f}".format(loop_count, price))
    print()

# things to do no 2. changing the constants

MAX_INCREASE = 0.175  # 17.5%
MIN_PRICE = 1
MAX_PRICE = 100.0

loop_count = 0
price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price))

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    loop_count += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)

    print("On day {} price is: ${:,.2f}".format(loop_count, price))
    print()

# things to do no 3 ... print the program output to file
out_file = open(OUTPUT_FILE, 'w')
loop_count = 0
price = INITIAL_PRICE
print("Starting price: ${:,.2f}".format(price), file=out_file)

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    loop_count += 1
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)

    print("On day {} price is: ${:,.2f}".format(loop_count, price), file=out_file)
    print()
out_file.close()
