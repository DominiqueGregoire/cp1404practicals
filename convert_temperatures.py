"""Create a program that will read the temps_input_txt file as fahrenheit
temperatures and convert them to Celsius.  The converted temperatures will
be then stored in a file named temps_output.txt"""


def main():
    temps_input_file = open('temps_input.txt', 'r')
    temps_output_file = open('temps_output.txt', 'w')

    for line in temps_input_file:
        line = temps_input_file.readline().strip('\n')
        print(line)
        fahrenheit = float(line)
        print(fahrenheit + 1)
#         celsius = convert_fahrenheit_to_celsius(temp)
#         print(celsius)
#
#
# def convert_fahrenheit_to_celsius(fahrenheit):
#     celsius = 5 / 9 * (fahrenheit - 32)  # celsius = 5 / 9 * (fahrenheit - 32)
#     return celsius


main()
