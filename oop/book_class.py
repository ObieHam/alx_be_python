class Book:
  """
  A class representing a book with title, author, and publication year attributes.
  """

  def __init__(self, title, author, year):
    """
    Initializes a Book instance with the provided title, author, and year.

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
      year (int): The publication year of the book.
    """

    self.title = title
    self.author = author
    self.year = year

  def __del__(self):
    """
    Prints a message indicating the book is being deleted.

    This method is called when the Book instance is garbage collected.
    """

    print(f"Deleting {self.title}")

  def __str__(self):
    """
    Returns a string representation of the book in a human-readable format.

    Returns:
      str: A string in the format "(title) by (author), published in (year)".
    """

    return f"{self.title} by {self.author}, published in {self.year}"

  def __repr__(self):
    """
    Returns a string representation of the Book instance for code recreation.

    This method allows recreating the Book object using the returned string.

    Returns:
      str: A string that can be used to create a new Book instance:
           f"Book('{self.title}', '{self.author}', {self.year})".
    """

    return f"Book('{self.title}', '{self.author}', {self.year})"

# Example usage (can be placed in a separate script)
if __name__ == "__main__":
  # Creating an instance of Book
  my_book = Book("1984", "George Orwell", 1949)

  # Demonstrating the __str__ method
  print(my_book)  # Expected to use __str__

  # Demonstrating the __repr__ method
  print(repr(my_book))  # Expected to use __repr__

  # Deleting a book instance to trigger __del__
  del my_book
