library = []

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
    library.append(Book(book_title, book_author, book_year_published))

def show_all_books():
    for book in library:
        book.describe()

def filter_books_by_year_published():
    print()

def main():
    print("Library Management Program")
    print("Please select a valid option!")
    print("1 - Add New Book")
    print("2 - Show all Books")
    print("3 - Filter Books by Year Published")
    print("4 - Exit")
    while True:
        menu_selection = input("Selection: ").strip().lower()
        if menu_selection == "1":
            new_book()
        elif menu_selection == "2":
            show_all_books()
        elif menu_selection == "3":
            filter_books_by_year_published()
        elif menu_selection == "4":
            break
        else:
            print("Invalid selection. Please try again.")

if __name__ == "__main__":
    main()