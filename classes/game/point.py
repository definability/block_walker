from classes.exceptions.point import *

class Point:

  def __init__(self, x, y=None):
    # Init
    if x.__class__ in [list, tuple] and len(x) == 2:
      try:
        self.x, self.y = x
      except ValueError:
        raise IllegalPointCoordinatesNumber(x)
    elif x.__class__ is dict and len(x) == 2:
      try:
        self.x, self.y = x['x'], x['y']
      except KeyError:
        raise CoordinatesKeyError(x)
    elif x.__class__ is self.__class__:
      self.x = x.x, x.y
    else:
      self.x, self.y = x, y
    # Errors processing
    if self.x is None or self.y is None:
      if x.__class__ not in [list, tuple, dict]:
        raise IllegalPointCoordinatesNumber(x, 1)
      else:
        raise IllegalPointCoordinatesNumber(x)
    elif self.x.__class__ != int or self.y.__class__ != int:
      raise NonIntegerPointCoordinates([self.x, self.y])

  def __iadd__(self, point):
    self.x += point.x
    self.y += point.y
    return self

  def __add__(self, point):
    return self.__class__(self.x + point.x, self.y + point.y)

  def __isub__(self, point):
    self.x -= point.x
    self.y -= point.y
    return self

  def __sub__(self, point):
    return self.__class__(self.x - point.x, self.y - point.y)

  def __eq__(self, point):
    return self.x, self.y == point.x, point.y

  def __ne__(self, point):
    return self.x != point.x and self.y != point.y

  def __str__(self):
    return "Point(%d,%d)"%(self.x, self.y)
