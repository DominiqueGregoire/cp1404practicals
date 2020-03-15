"""create a temperature input file with at least 15 floats"""
import random

quantity = int(input('Enter quantity of inputs: '))


def main():
    temps_input_file = open("temps_input.txt", 'w')

    for temperature in range(quantity):
        temperature = random.uniform(-200, 200)
        print(temperature, file=temps_input_file)

    temps_input_file.close()


main()
