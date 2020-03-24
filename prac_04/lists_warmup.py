
numbers = [3, 1, 4, 1, 5, 9, 2]

"""numbers[0]  value will be 3   
numbers[-1]    value will be 2
numbers[3]     value will be 1
numbers[:-1]   value will be [3, 1, 4, 1, 5, 9, 2] nb only goes to 9 not all the way to the
                                                 last number
numbers[3:4]   value will be 1
5 in numbers   value will be True
7 in numbers    value will be False
"3" in numbers   value will be False nb its a string not a number
numbers + [6, 5, 3]   value will be [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] """

"""
    Change the first element of numbers to "ten" (the string, not the number 10)
    Change the last element of numbers to 1
    Get all the elements from numbers except the first two (slice)
    Check if 9 is an element of numbers
"""
numbers[0] = "ten"
print(numbers)
numbers[-1] = 1
print(numbers)
value = numbers[2:]
print(value)
value = 9 in numbers
print(value)