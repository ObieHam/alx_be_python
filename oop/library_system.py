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

  def __str__(self):
    """
    Returns a string representation of the book in a general format.

    Returns:
      str: A string in the format "Book: Title by Author".
    """

    return f"Book: {self.title} by {self.author}"

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

  def __str__(self):
    """
    Returns a string representation of the EBook with specific details.

    Returns:
      str: A string in the format "EBook: Title by Author, File Size: X KB".
    """

    return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

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

  def __str__(self):
    """
    Returns a string representation of the PrintBook with specific details.

    Returns:
      str: A string in the format "PrintBook: Title by Author, Page Count: X".
    """

    return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

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
      print(book)  # Use the __str__ method of each book object

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
  my_library.add_book(digital_novel
