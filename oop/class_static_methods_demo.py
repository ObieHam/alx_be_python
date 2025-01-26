class Calculator:
  """
  A class for performing basic arithmetic operations.
  """

  calculation_type = "Arithmetic Operations"  # Class attribute

  @staticmethod
  def add(a, b):
    """
    Static method to add two numbers.

    Args:
      a (int): The first number.
      b (int): The second number.

    Returns:
      int: The sum of a and b.
    """

    return a + b

  @classmethod
  def multiply(cls, a, b):
    """
    Class method to multiply two numbers.

    Args:
      cls (class): The Calculator class.
      a (int): The first number.
      b (int): The second number.

    Returns:
      int: The product of a and b.
    """

    print(f"Calculation type: {cls.calculation_type}")
    return a * b

# Example usage (can be placed in a separate script)
if __name__ == "__main__":
  # Using the static method
  sum_result = Calculator.add(10, 5)
  print(f"The sum is: {sum_result}")

  # Using the class method
  product_result = Calculator.multiply(10, 5)
  print(f"The product is: {product_result}")
