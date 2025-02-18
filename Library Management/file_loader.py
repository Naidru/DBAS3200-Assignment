import csv
from main import Book

data = [
    ["ID", "Title", "Author", "Year Published"]
]

filename = "books.csv"


def get_data():
    books = []
    try:
        with open(filename, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                book = Book(row["Title"], row["Author"], row["Year Published"])
                books.append(book)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Starting with an empty library.")
    except IOError as e:
        print(f"File error: {e}")
    return books


def save_data(library):
    i = 1
    for book in library.books:
        data.append([i, book.get_title(), book.get_author(), book.year_published])
        i += 1
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)

            for row in data:
                try:
                    writer.writerow(row)  # Writing one row at a time
                except Exception as e:
                    print(f"Error writing row {row}: {e}")

        print("Book data saved successfully.")

    except IOError as e:
        print(f"File error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")