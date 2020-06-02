"""
Small program that will retrieve a page from wikipedia
"""
import wikipedia


def main():
    page_title = input("Please enter the page title or search phrase:  ")

    # while page_title != " ":
    #     try:
    #         wikipedia.summary(page_title)
    #
    #         print(page_title)
    #     except wikipedia.exceptions.DisambiguationError as e:
    #         print(e.options)
    #
    #     page_title = input("Please enter the page title or search phrase:  ")
    my_page = input("Please enter the page title or search phrase:  ")

    while my_page != " ":
        try:
            my_page = wikipedia.page(my_page)
            print("{}\n{}\n{}".format(my_page.title, my_page.summary, my_page.url))
        except wikipedia.exceptions.DisambiguationError as e:
            print(e.options)

        my_page = input("Please enter the page title or search phrase:  ")


main()
