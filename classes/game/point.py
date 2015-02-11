from classes.exceptions.point import *

class Point:

  def __init__(self, x, y=None):
    if x.__class__ in [list, tuple] and len(x) > 1:
      try:
        self.x, self.y = x
      except ValueError:
        raise IllegalPointCoordinatesNumber(x)
    elif x.__class__ == self.__class__:
      self.x = x.x, x.y
    elif x.__class__ == int and y.__class__ == int:
      self.x, self.y = x, y
    elif x.__class__ == float or y.__class__ == float:
      raise NonIntegerPointCoordinates([x, y])
    elif y == None and x.__class__ not in [list, tuple]:
      raise IllegalPointCoordinatesNumber(x, 1)
    elif y == None:
      raise IllegalPointCoordinatesNumber(x)
    else:
      raise IllegalPointArguments([x,y])

  def __iadd__(self, point):
    self.x += point.x
    self.y += point.y

  def __add__(self, point):
    return self.__class__(self.x + point.x, self.y + point.y)
