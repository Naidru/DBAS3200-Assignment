# Requirements:
    #
    # 2. Define a Library Class
    # Class Name: Library
    # Purpose:
    # Since there will be only one library for your program, the Library class is used to logically isolate all operations required for managing your application's data.
    # Responsibilities:
    # The class should provide functionality for:
    # Managing the collection of books (for example, storing all the Book objects in a list).
    # Adding a book to the collection.
    # Removing a book from the collection based on its title.
    # Showing all books in the collection.
    # Filtering books by publication year.
    # Searching for books by author.
    # Handling persistent storage:
    # Loading Data: On startup, the class should load the list of books from a file (e.g., library.json or library.txt).
    # Saving Data: After any modification (or before program exit), the class should save the current list of books back to the file.
    # Implementation Note:
    # Decide for each of the operations whether it makes sense to implement them as static (class-level) methods/fields or as instance methods/fields. The design choice is up to you based on the guidance that the class is used for central data management, rather than representing multiple instances.
# 3. Persistent Storage
# File Storage:
# On Startup:
# The program should load the library's book data from persistent storage.
# On Modification or Exit:
# Whenever the library is modified (e.g., when a book is added or removed) or before the program terminates, the library should save the current list of books to the file.
# Data Format:
# You can use a structured format (e.g., JSON, CSV) or a simple text format, as long as each book's information (title, author, year_published) can be stored and later restored into Book objects.
# Implementation Suggestion:
# Consider creating helper functions (or methods) such as save_to_file(filename) and load_from_file(filename) within your Library class to manage persistent storage.
# Include appropriate error handling in case the file does not exist or if the stored data is corrupt.
# 4. Implement a Menu Loop
# Design your main program so that it repeatedly presents the following menu options to the user:
#
# Add a New Book:
#
# Prompt the user to enter the book's title, author, and year published.
# Create a new Book object with the provided data.
# Add the new book to the library's collection using the operations provided by your Library class.
# Update the persistent storage after adding the book.
# Show All Books:
#
# Display the details of every book in the library (for example, by iterating over the collection and calling each book’s describe() method).
# Filter Books by Year Published:
#
# Ask the user to enter a publication year.
# Display only those books in the library whose year_published matches the given year.
# Search Books by Author:
#
# Ask the user to enter an author's name.
# Display the books written by that author.
# Remove a Book:
#
# Prompt the user to enter the title of the book they wish to remove.
# Remove the matching book from the library’s collection.
# Update the persistent storage after removing the book.
# Exit:
#
# Provide an option (for example, option 0) to exit the program gracefully.
# Ensure that the library's current state is saved to persistent storage before the program terminates.
# 5. User Input and Validation
# Data Conversion:
# Convert user inputs to the appropriate data types (e.g., converting the year from a string to an integer).
# Error Handling:
# Implement error handling to manage invalid inputs (such as non-numeric values when a number is expected or attempting to remove a non-existent book).
# 6. Program Structure
# File Organization:
# Organize your code in a single Python file.
# Main Function:
# Encapsulate the main program logic (including the menu loop) in a main() function.
# Entry Point:
# Ensure the program starts by calling the main() function within an if __name__ == '__main__': block.
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

    def get_year(self):
        return self.year_published

    def get_author(self):
        return self.author


class Library:
    def __init__(self):
        self.books = []

    def create(self, book_title, book_author, book_year_published):
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
    library.create(book_title, book_author, book_year_published)


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
    book_list = loader.get_data()
    library = Library()
    library.overwrite_book_list(book_list)


def save_library():
    book_list = Library.get_book_list
    loader.save_data(book_list)


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
