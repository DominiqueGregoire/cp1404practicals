"""
Create a program that will sort files into sub-directories.
"""
import os
import shutil


def main():

    # change directory to FilesToSort and list files in the directory
    os.chdir('FilesToSort')
    filenames = os.listdir('.')
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    file_extensions = ['.jpg', '.doc', '.docx', '.png', '.gif', '.txt', '.xls', '.xlsx']
    categories = []

    # need to use try/except to avoid FileExistsError
    for extension in file_extensions:
        category = extension[1:]
        print('category - {}'.format(category))
        if category not in categories:
            categories.append(category)
            try:
                os.mkdir(category)

            except:
                FileExistsError

    # move the files into their respective new directories

        for file in filenames:
            # print(extension)        # for debugging

            if file.endswith(extension):
                # print(file)         # for debugging
                # print(category)     # for debugging
                shutil.move(file, category)


main()
