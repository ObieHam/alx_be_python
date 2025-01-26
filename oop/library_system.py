class Book:
  """
  A base class representing a book with title and author attributes.
  """

  def __init__(self, title, author):
    """
    Initializes a Book instance with the provided title and author.

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
    """

    self.title = title
    self.author = author

class EBook(Book):
  """
  A derived class representing an electronic book with additional file size attribute.
  """

  def __init__(self, title, author, file_size):
    """
    Initializes an EBook instance with title, author, and file size.

    Args:
      title (str): The title of the ebook.
      author (str): The author of the ebook.
      file_size (int): The file size of the ebook in KB.
    """

    super().__init__(title, author)
    self.file_size = file_size

class PrintBook(Book):
  """
  A derived class representing a printed book with additional page count attribute.
  """

  def __init__(self, title, author, page_count):
    """
    Initializes a PrintBook instance with title, author, and page count.

    Args:
      title (str): The title of the printed book.
      author (str): The author of the printed book.
      page_count (int): The number of pages in the printed book.
    """

    super().__init__(title, author)
    self.page_count = page_count

class Library:
  """
  A class representing a library that manages a collection of books.
  """

  def __init__(self):
    """
    Initializes a Library instance with an empty list to store books.
    """

    self.books = []

  def add_book(self, book):
    """
    Adds a Book, EBook, or PrintBook instance to the library collection.

    Args:
      book (Book, EBook, or PrintBook): The book to be added to the library.
    """

    self.books.append(book)

  def list_books(self):
    """
    Prints details of each book in the library, including specific attributes.
    """

    for book in self.books:
      if isinstance(book, EBook):
        print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
      elif isinstance(book, PrintBook):
        print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
      else:
        print(f"Book: {book.title} by {book.author}")

# Example usage (can be placed in a separate script)
if __name__ == "__main__":
  # Create a Library instance
  my_library = Library()

  # Create instances of each type of book
  classic_book = Book("Pride and Prejudice", "Jane Austen")
  digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
  paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

  # Add books to the library
  my_library.add_book(classic_book)
  my_library.add_book(digital_novel)
  my_library.add_book(paper_novel)

  # List all books in the library
  my_library.list_books()
