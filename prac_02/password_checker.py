"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

#
# def main():
#     """Program to get and check a user's password."""
#     print("Please enter a valid password")
#     print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
#           "characters, and contain:")
#     print("\t1 or more uppercase characters")
#     print("\t1 or more lowercase characters")
#     print("\t1 or more numbers")
#     if SPECIAL_CHARS_REQUIRED:
#         print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
#     password = input("> ")
#     while not is_valid_password(password):
#         print("Invalid password!")
#         password = input("> ")
#     print("Your {}-character password is valid: {}".format(len(password),
#                                                            password))
#
#
# def is_valid_password(password):
#     """Determine if the provided password is valid."""
#     # TODO: if length is wrong, return False
#
#     count_lower = 0
#     count_upper = 0
#     count_digit = 0
#     count_special = 0
#     for char in password:
#         # TODO: count each kind of character (use str methods like isdigit)
#         lower_case = char.islower()
#         count_lower += lower_case       # checking for and counting lower case characters
#
#         upper_case = char.isupper()
#         count_upper += upper_case       # checking for and counting upper case characters
#
#         digits = char.isdigit()
#         count_digit += digits           # checking for and counting digits
#
#         special_char = " "
#         if char in SPECIAL_CHARACTERS:  # checking for and counting number of special characters
#             special_char += char
#             # print("special char chek", special_char)
#             count_special = len(special_char)
#
#     # print('lower count is ', count_lower)
#     # print('upper count is ', count_upper)
#     # print("digits are ", count_digit)
#     # print("special characters ", count_special)
#
#     # TODO: if any of the 'normal' counts are zero, return False
#     # TODO: if special characters are required, then check the count of those
#     # and return False if it's zero
#     if count_lower == 0:
#         return False
#     elif count_upper == 0:
#         return False
#     elif count_digit == 0:
#         return False
#     elif count_special == 0:
#         return False
#
#     # if we get here (without returning False), then the password must be valid
#     return True

# main()

# password checker proper code


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print("Your password must be between {} and {} "
          "characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")

    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print("Your {}-character password is valid: {}".format(len(password),
                                                           password))


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # if length is wrong, return False
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0

    for char in password:
        lower_case = char.islower()
        count_lower += lower_case       # checking for and counting lower case characters

        upper_case = char.isupper()
        count_upper += upper_case       # checking for and counting upper case characters

        digits = char.isdigit()
        count_digit += digits           # checking for and counting digits

        special_char = " "
        if char in SPECIAL_CHARACTERS:  # checking for and counting number of special characters
            special_char += char
            count_special = len(special_char)

    # if any of the 'normal' counts are zero, return False
    # if special characters are required, then check the count of those
    # and return False if it's zero
    if count_lower == 0:
        return False
    elif count_upper == 0:
        return False
    elif count_digit == 0:
        return False
    elif count_special == 0:
        return False

    return True


main()
