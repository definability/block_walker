from classes.exceptions.point import *

class Point(object):

  def __init__(self, x, y=None):
    # Init
    if type(x) in [list, tuple] and len(x) == 2:
      try:
        self.x, self.y = x
      except ValueError:
        raise IllegalPointCoordinatesNumber(x)
    elif type(x) is dict and len(x) == 2:
      try:
        self.x, self.y = x['x'], x['y']
      except KeyError:
        raise CoordinatesKeyError(x)
    elif type(x) is type(self):
      self.x = x.x, x.y
    else:
      self.x, self.y = x, y
    # Errors processing
    if self.x is None or self.y is None:
      if type(x) not in [list, tuple, dict]:
        raise IllegalPointCoordinatesNumber(x, 1)
      else:
        raise IllegalPointCoordinatesNumber(x)
    elif type(self.x) != int or type(self.y) != int:
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

  def __iter__(self):
    yield self.x
    yield self.y
