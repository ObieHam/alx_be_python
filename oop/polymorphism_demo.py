import math

class Shape:
  """
  A base class representing a generic shape.
  """

  def area(self):
    """
    Abstract method to calculate the area of a shape.

    Raises a NotImplementedError as derived classes should implement this method.
    """

    raise NotImplementedError("Subclasses must implement area()")

class Rectangle(Shape):
  """
  A derived class representing a rectangle shape.
  """

  def __init__(self, length, width):
    """
    Initializes a Rectangle instance with length and width attributes.

    Args:
      length (float): The length of the rectangle.
      width (float): The width of the rectangle.
    """

    self.length = length
    self.width = width

  def area(self):
    """
    Overrides the base class area() method to calculate the area of a rectangle.

    Returns:
      float: The calculated area of the rectangle (length x width).
    """

    return self.length * self.width

class Circle(Shape):
  """
  A derived class representing a circle shape.
  """

  def __init__(self, radius):
    """
    Initializes a Circle instance with a radius attribute.

    Args:
      radius (float): The radius of the circle.
    """

    self.radius = radius

  def area(self):
    """
    Overrides the base class area() method to calculate the area of a circle.

    Returns:
      float: The calculated area of the circle (pi * radius^2).
    """

    return math.pi * self.radius ** 2  # Corrected line with double underscore

# Example usage (can be placed in a separate script)
if __name__ == "__main__":
  shapes = [
      Rectangle(10, 5),
      Circle(7)
  ]

  for shape in shapes:
      print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")
