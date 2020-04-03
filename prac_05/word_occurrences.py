"""Create a program to count the occurrences of words in a string.
The program will ask the user for a string,
then print the counts of how many of each word are in the file.
"""

word_occurrences_dict = {}   # initialize an empty dictionary
word_string = input("Enter the text: ")    # get a string of text from user
print("Text: ", word_string)

for word in word_string.split():     # split the string into individual words
    # append the word and the amount of times it occurs in the string to the dictionary
    word_occurrences_dict[word] = word_occurrences_dict.get(word, 0) + 1

# sort and print the unique words in the dictionary
unique_words = list(word_occurrences_dict.keys())
print(unique_words)
unique_words.sort()
print(unique_words)


#    retrieves and displays formatted word/occurrence pair
for word in unique_words:
    print("{} : {}".format(word, word_occurrences_dict[word]))

# print(word_occurrences_dict)
