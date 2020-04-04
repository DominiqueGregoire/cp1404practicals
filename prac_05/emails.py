"""Stores users' emails (unique keys) and names (values) in a dictionary.
The program will keep asking the user for their email until they enter a blank one."""


def main():

    names_and_emails_dict = {}
    email = input("Email: ")
    while email != '':
        is_name_correct = input("Is your name {}? (Y/n)".format(get_name_from_email(email)))

        if is_name_correct[0].upper() == "Y":
            names_and_emails_dict[email] = get_name_from_email(email)
        elif is_name_correct[0].lower() == 'n':
            name = input('Name: ')
            names_and_emails_dict[email] = name
        email = input('Email: ')

    for email, name in names_and_emails_dict.items():
        print('{}  ({})'.format(name, email))


def get_name_from_email(email):
    """Removes the portion before the @ and returns it as a name"""
    names = email[:email.find("@")].title()
    names = names.split('.')

    return ' '.join(names)


main()
