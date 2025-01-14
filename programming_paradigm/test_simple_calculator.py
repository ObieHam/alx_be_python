import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculatorTest(unittest.TestCase):
    def setUp(self):
        """Create a SimpleCalculator instance."""
        self.calculator = SimpleCalculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertEqual(self.calculator.add(1, -1), 0)
        self.assertEqual(self.calculator.add(-1, -1), -2)
        self.assertEqual(self.calculator.add(0.5, 0.5), 1)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(1, 1), 0)
        self.assertEqual(self.calculator.subtract(-1, 1), -2)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(1, -1), 2)
        self.assertEqual(self.calculator.subtract(1, 0.5), 0.5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(1, 1), 1)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(-1, -1), 1)
        self.assertEqual(self.calculator.multiply(1, -1), -1)
        self.assertEqual(self.calculator.multiply(1, 0.5), 0.5)
        self.assertEqual(self.calculator.multiply(0, 0.5), 0)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(1, 1), 1)
        self.assertEqual(self.calculator.divide(1, -1), -1)
        self.assertEqual(self.calculator.divide(1, 0), None)
        self.assertEqual(self.calculator.divide(0, 1), 0)
        self.assertEqual(self.calculator.divide(1, 0.5), 2)
        self.assertEqual(self.calculator.divide(5, 2), 2.5)

if __name__ == "__main__":
    unittest.main()
