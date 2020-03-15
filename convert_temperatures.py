"""Create a program that will read the temps_input_txt file as fahrenheit
temperatures and convert them to Celsius.  The converted temperatures will
be then stored in a file named temps_output.txt"""


def main():
    temps_input_file = open('temps_input.txt', 'r')
    temps_output_file = open('temps_output.txt', 'w')

    for line in temps_input_file:
        # print(float(line))
        temperature = convert_fahrenheit_to_celsius(float(line))
        # temperature = convert_celsius_to_fahrenheit(float(line))
        print(temperature, file=temps_output_file)


def convert_fahrenheit_to_celsius(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)  # celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


# def convert_celsius_to_fahrenheit(celsius):
#     fahrenheit = celsius * 9.0 / 5 + 32  # fahrenheit = celsius * 9.0 / 5 + 32
#     return fahrenheit

main()
