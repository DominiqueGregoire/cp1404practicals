"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue
        new_name = get_fixed_filename(filename)
        print("\nRenaming {} to {}\n".format(filename, new_name))

        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):       # still have to find out how to fix a couple of the files
                                        #    unsure how to go about it???

    """Return a 'fixed' version of filename."""
    print(filename)
    i = 0
    section1 = ''
    section2 = ''
    section3 = ''

    for i, letter in enumerate(filename[0:-4]):
        if '_' in filename:
            continue
            # print(filename)   # for debugging

        elif letter.isupper():
            index = filename.find(letter)
            section1 = filename[:index]
            section2 = filename[index:]
            section3 = section1 + " " + section2
            # print("section 1 is: {}\nsection 2 is: {}\nsection 3 is: {}"
            #       .format(section1, section2, section3))  # for debugging

            corrected_section = section3  # print("corrected section is; ", corrected_section)
            filename = corrected_section
            if filename.startswith(" "):
                # print(filename)       # for debugging
                filename = filename[1:]
                # print(filename)       # for debugging

    # print('\n', filename)

    new_name = filename.replace(" ", "_").replace(".TXT", ".txt").replace('__', '_')

    # print(filename)
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        print("Directory:", directory_name)
        print("\tcontains subdirectories:", subdirectories)
        print("\tand files:", filenames)
        print("(Current working directory is: {})".format(os.getcwd()))

        # Add a loop to rename the files
        for filename in filenames:
            os.path.join(directory_name, filename)

            filename = os.path.join(directory_name, filename)

            renamed_file = get_fixed_filename(filename)

            os.path.join(directory_name, renamed_file)

            os.rename(filename, renamed_file)


main()
# demo_walk()
