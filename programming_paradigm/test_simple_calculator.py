# test_simple_calculator.py
import unittest 
from simple_calculator import SimpleCalculator
class SimpleCalculatorTest(unittest.TestCase):
    def test_add(self):
        self.assertEqual(SimpleCalculator.add(1,1), 2)
        self.assertEqual(SimpleCalculator.add(1,-1), 0)
        self.assertEqual(SimpleCalculator.add(-1,-1), -2)
        self.assertEqual(SimpleCalculator.add(0.5,0.5), 1)
        
    def test_subtract(self):
        self.assertEqual(SimpleCalculator.subtract(1,1), 0)
        self.assertEqual(SimpleCalculator.subtract(-1,1), -2)
        self.assertEqual(SimpleCalculator.subtract(-1,-1), 0)
        self.assertEqual(SimpleCalculator.subtract(1,-1), 2)
        self.assertEqual(SimpleCalculator.subtract(1,0.5), 0.5)    

    def test_multiply(self):
        self.assertEqual(SimpleCalculator.multiply(1,1), 1)
        self.assertEqual(SimpleCalculator.multiply(-1,1), -1)
        self.assertEqual(SimpleCalculator.multiply(-1,-1), 1)
        self.assertEqual(SimpleCalculator.multiply(1,-1), -1)
        self.assertEqual(SimpleCalculator.multiply(1,0.5), 0.5)
        self.assertEqual(SimpleCalculator.multiply(0,0.5), 0)

    def test_divide(self):
        self.assertEqual(SimpleCalculator.divide(1,1), 1)
        self.assertEqual(SimpleCalculator.divide(1,-1), -1)
        self.assertEqual(SimpleCalculator.divide(1,0), None)
        self.assertEqual(SimpleCalculator.divide(0,1), 0)
        self.assertEqual(SimpleCalculator.divide(1,0.5), 2)
        self.assertEqual(SimpleCalculator.divide(5, 2), 2.5)
        
if __name__ == "__main__":
    unittest.main()
         
            

          
