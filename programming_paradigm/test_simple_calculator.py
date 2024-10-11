import unittest
from simple_calculator import SimpleCalculator

class TestClass(unittest.TestCase):

  def test_addition(self):
    calc = SimpleCalculator()
    result = calc.add(3,5)
    self.assertEqual(result,8)
  
  def test_subtraction(self):
    calc = SimpleCalculator()
    result = calc.subtract(5,3)
    self.assertEqual(result,2)

  def test_multiplication(self):
    calc = SimpleCalculator()
    result = calc.multiply(5,3)
    self.assertEqual(result,15)
  
  def test_division(self):
    calc = SimpleCalculator()
    result = calc.divide(4,2)
    self.assertEqual(result,2)
  
  def test_division_by_zero(self):
    calc = SimpleCalculator()
    result = calc.divide(4,0)
    self.assertEqual(result,None)

if __name__ == "__main__":
  unittest.main()