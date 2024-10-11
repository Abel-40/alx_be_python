import unittest
from simple_calculator import SimpleCalculator

class TestClass(unittest.TestCase):
  def test_addition(self):
    calc = SimpleCalculator()
    self.assertEqual(calc.add(3,5),8)
  
  def test_subtraction(self):
    calc = SimpleCalculator()
    self.assertEqual(calc.subtract(5,3),2)

  def test_multiplication(self):
    calc = SimpleCalculator()
    self.assertEqual(calc.multiply(5,3),15)
  
  def test_division(self):
    calc = SimpleCalculator()
    self.assertEqual(calc.divide(4,2),2)
  
  def test_division_by_zero(self):
    calc = SimpleCalculator()
    self.assertEqual(calc.divide(4,0),None)

if __name__ == "__main__":
  unittest.main()