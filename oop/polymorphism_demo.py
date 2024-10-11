import math
class Shape:
  def area(self):
    raise NotImplementedError
  
class Rectangle(Shape):
  def __init__(self,length,width):
    self.length = length
    self.width = width

  def area(self):
    result = self.length * self.width
    return result
class Circle(Shape):
  def __init__(self, radius):
    self.radius = radius
    self.pi = math.pi
  def area(self):
    result = self.pi * (self.radius * self.radius)
    return result