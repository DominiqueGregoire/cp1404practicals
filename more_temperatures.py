"""create a temperature input file with at least 15 floats"""
import random


def main():
    temperature_input_file = open("temps_input.txt", 'w')
    random_temperature = random.uniform(-200.0, 200.0)

    for temperature in range(5):
        temperature = random_temperature
        print(temperature, file=temperature_input_file)
        random_temperature = random.uniform(-200.0, 200.0)

    temperature_input_file.close()


main()
