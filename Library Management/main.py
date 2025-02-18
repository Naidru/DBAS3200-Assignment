
import file_loader as loader


class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def describe(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year Published: {self.year_published}")
        print()

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year_published

    def get_author(self):
        return self.author


class Library:
    def __init__(self):
        self.books = []

    def create_book(self, book_title, book_author, book_year_published):
        self.books.append(Book(book_title, book_author, book_year_published))

    def delete(self, book_title):
        did_book_remove = False
        for book in self.books:
            if book.title.lower() == book_title.lower():
                self.books.remove(book)
                did_book_remove = True
                break
        if did_book_remove is not True:
            print(f"No book named {book_title} found!")
        else:
            print("Book(s) with that title have been removed.")

    def get_book_list(self):
        return self.books

    def overwrite_book_list(self, book_list):
        self.books = book_list


def new_book():
    book_title = input("Enter name of book: ")
    book_author = input("Enter author of book: ")
    while True:
        book_year_published = input("Enter year book was made: ")
        if not book_year_published.isdigit():
            print("Please input a number to be a year.")
        else:
            if 0 <= int(book_year_published) <= 9999:
                break
            else:
                print("Please input a valid 4-digit number.")
    library.create_book(book_title, book_author, book_year_published)


def remove_book():
    book_name = input("Enter name of book to remove: ")
    library.delete(book_name)


def show_all_books():
    for book in library.books:
        book.describe()


def filter_books_by_year_published():
    book_found = False
    while True:
        year_to_search = input("Enter year to search: ")
        if not year_to_search.isdigit():
            print("Please input a number to be a year.")
        else:
            if 0 <= int(year_to_search) <= 9999:
                break
            else:
                print("Please input a valid 4-digit number.")
    for book in library.books:
        if int(book.year_published) == int(year_to_search):
            book_found = True
            book.describe()
    if book_found is False:
        print("No book with the specified year found.")


def filter_books_by_author():
    book_found = False
    author_to_search = input("Enter name of author to search: ")
    for book in library.books:
        if book.get_author().lower().strip() == author_to_search.lower().strip():
            book_found = True
            book.describe()
    if book_found is False:
        print("No book with the specified author found.")


def initialize_library():
    global library
    library = Library()
    book_list = loader.get_data()
    library.overwrite_book_list(book_list)


def save_library():
    loader.save_data(library)


def main():
    initialize_library()
    print("Library Management Program")
    print("Please select a valid option!")
    print("1 - Add New Book")
    print("2 - Remove a Book")
    print("3 - Show all Books")
    print("4 - Filter Books by Year Published")
    print("5 - Exit and Save")
    print("6 - Exit without Saving")
    while True:
        menu_selection = input("Selection: ").strip().lower()
        if menu_selection == "1":
            new_book()
        elif menu_selection == "2":
            remove_book()
        elif menu_selection == "3":
            show_all_books()
        elif menu_selection == "4":
            filter_books_by_year_published()
        elif menu_selection == "5":
            save_library()
            break
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()
