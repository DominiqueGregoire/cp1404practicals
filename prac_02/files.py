""" 1. get user's name and write it to a file
pseudo code
open a write file called name.text
get users name
print users name to file
close file"""

my_file = open("name.txt", "w")

name = input("Enter your name: ").title()
print(name, file=my_file)

my_file.close()

''' part 2. opens the name.txt file and prints out a message with the name in it
pseudo code
open file as a read file
read first line
print message with name
close the file'''

input_file = open("name.txt", "r")

name = input_file.readline()
print("Your name is", name)

input_file.close()

'''part 3. open the numbers.txt file
adds the first two numbers and prints out the result
pseudo code
open the file
read the first two numbers
add the numbers
print the result
close the file'''

number_file = open("numbers.txt", 'r')

first_number = int(number_file.readline())
second_number = int(number_file.readline())

result = first_number + second_number
print("The result of adding the first two numbers is: ", result)

number_file.close()

'''part 4... read and total up all the numbers in the number_file.txt
pseudo code
initialise sum as 0
open and read the file
add up all the numbers
display result
close the file'''

sum = 0
number_file = open("numbers.txt", "r")

for line in number_file:
    number = int(line.strip())
    sum += number

print("sum of all numbers in the file is", sum)

number_file.close()
