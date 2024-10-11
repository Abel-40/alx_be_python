import unittest
from simple_calculator import SimpleCalculator

class TestClass(unittest.TestCase):

  def __init__(self):
    self.calc = SimpleCalculator()

  def test_addition(self):
    self.assertEqual(self.calc.add(3,5),8)
  
  def test_subtraction(self):
    self.assertEqual(self.calc.subtract(5,3),2)

  def test_multiply(self):
    self.assertEqual(self.calc.multiply(5,3),15)
  
  def test_divide(self):
    self.assertEqual(self.calc.divide(4,2),2)
  
  def test_division_by_zero(self):
    self.assertEqual(self.calc.divide(4,0),None)

if __name__ == "__main__":
  unittest.main()
