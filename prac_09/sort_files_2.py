"""
CP1404 prac_09
Program to sort files according to user choice
"""
import os
import shutil


def main():
    file_extensions = ['.jpg', '.doc', '.docx', '.png', '.gif', '.txt', '.xls', '.xlsx']

    """
    ask user where to put files
    create the directories
    move files to directories
    """
# change directories
    os.chdir('FilesToSort')
    filenames = os.listdir('.')
    # print(filenames)    # for debugging

# ask user where to put files (categories):
# create a list of categories
    categories = []
    for extension in file_extensions:
        # print(extension)    # for debugging
        category = input("What category would you like to sort {} files into?\n".format(extension))
        if category not in categories:
            categories.append(category)

# create the directories
            try:
                os.mkdir(category)
            except:
                FileExistsError
            # print(extension)      # for debugging
        for file in filenames:
            # print(extension)        # for debugging
            if file.endswith(extension):
                # print(file)         # for debugging
                # print(category)     # for debugging

# move the file into the directory
                shutil.move(file, category)


main()
