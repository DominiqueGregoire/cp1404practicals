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
    print([file for file in filenames])

    file_extensions = ['jpg', 'doc', 'docx', 'png', 'gif', 'txt', 'xls', 'xlsx']

    # need to use try/except to avoid FileExistsError
    for extension in file_extensions:
        try:
            os.mkdir(extension)
            print("\nFiles in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

        except:
            FileExistsError

    # move the files into their respective new directories
    for file in filenames:
        print(file)  # for debugging
        if file.endswith('.jpg'):
            shutil.move(file, 'jpg')
        #         print(file)     # for debugging
        elif file.endswith('.doc'):
            shutil.move(file, 'doc')
        elif file.endswith('.docx'):
            shutil.move(file, 'docx')
        elif file.endswith('.gif'):
            shutil.move(file, 'gif')
        elif file.endswith('.png'):
            shutil.move(file, 'png')
        elif file.endswith('.txt'):
            shutil.move(file, 'txt')
        elif file.endswith('.xls'):
            shutil.move(file, 'xls')
        elif file.endswith('.xlsx'):
            shutil.move(file, 'xlsx')


main()
