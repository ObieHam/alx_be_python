import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculatorTest(unittest.TestCase):
    def setUp(self):
        """Create a SimpleCalculator instance."""
        self.calc = SimpleCalculator()  # Attribute named `calc` as required

    def test_addition(self):
        """Test addition operation."""
        self.assertEqual(self.calc.add(1, 1), 2)
        self.assertEqual(self.calc.add(1, -1), 0)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0.5, 0.5), 1)

    def test_subtraction(self):
        """Test subtraction operation."""
        self.assertEqual(self.calc.subtract(1, 1), 0)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.subtract(-1, -1), 0)
        self.assertEqual(self.calc.subtract(1, -1), 2)
        self.assertEqual(self.calc.subtract(1, 0.5), 0.5)

    def test_multiplication(self):
        """Test multiplication operation."""
        self.assertEqual(self.calc.multiply(1, 1), 1)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(-1, -1), 1)
        self.assertEqual(self.calc.multiply(1, -1), -1)
        self.assertEqual(self.calc.multiply(1, 0.5), 0.5)
        self.assertEqual(self.calc.multiply(0, 0.5), 0)

    def test_division(self):
        """Test division operation."""
        self.assertEqual(self.calc.divide(1, 1), 1)
        self.assertEqual(self.calc.divide(1, -1), -1)
        self.assertEqual(self.calc.divide(1, 0), None)
        self.assertEqual(self.calc.divide(0, 1), 0)
        self.assertEqual(self.calc.divide(1, 0.5), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)

if __name__ == "__main__":
    unittest.main()
