
print("Number Sequences")

x_int = int(input("Enter the value of x: "))
y_int = int(input("Enter the value of y: "))

choice = input('(A) Show the even numbers from x to y\n(B) Show the '
               'odd numbers from x to y\n(C) Show the squares from '
               'x to y\n(Q) Exit the program').capitalize()

while choice != 'Q':
    if choice == 'A':
        for i in range(x_int, y_int + 1):
            if i % 2 == 0:
                print(i, end=" ")
        print()

    elif choice == 'B':
        for i in range(x_int, y_int + 1):
            if i % 2:
                print(i, end=' ')
        print()

    elif choice == 'C':
        for i in range(x_int, y_int +1):
            print(i**2, end=' ')
        print()

    else:
        print("Invalid choice")
    choice = input('(A) Show the even numbers from x to y\n(B) Show the '
                   'odd numbers from x to y\n(C) Show the squares from '
                   'x to y\n(Q) Exit the program').capitalize()

if choice == 'Q':
    print("Thank you")



