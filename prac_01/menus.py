
name = input("Enter name: ").capitalize()
menu_choice = input('(H)ello\n(G)oodbye\n(Q)uit').capitalize()

while menu_choice != "Q":
    if menu_choice == "H":
        print("Hello", name)
    elif menu_choice == "G":
        print('Goodbye', name)
    else:
        print("Invalid message")
    menu_choice = input('(H)ello\n(G)oodbye\n'
                        '(Q)uit').capitalize()

if menu_choice == "Q":
    print("Finished.")
