class Book:
    """A class representing a book with a title, author, and availability status."""
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as available."""
        self._is_checked_out = False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """A class to manage a collection of books."""
    def __init__(self):
        self._books = []

    def add_book(self, book):
        """Add a book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark a book as checked out by its title."""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    print(f"You have successfully checked out '{title}'.")
                    return
                else:
                    print(f"'{title}' is already checked out.")
                    return
        print(f"'{title}' is not in the library collection.")

    def return_book(self, title):
        """Mark a book as returned by its title."""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    print(f"You have successfully returned '{title}'.")
                    return
                else:
                    print(f"'{title}' was not checked out.")
                    return
        print(f"'{title}' is not in the library collection.")

    def list_available_books(self):
        """Print a list of all available books."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
