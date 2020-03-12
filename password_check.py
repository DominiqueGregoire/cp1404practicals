"""Checks that a password has at least the minimum length specified"""
def main():

minimum_password_length = int(input("Enter minimum password length: "))

password = input('Enter password')

while len(password) < 8:
    print('Password invalid. Please enter a password with at least {} '
          'characters.'.format(minimum_password_length))
    password = input('Enter password')

print("*" * len(password))
