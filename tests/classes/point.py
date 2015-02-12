from unittest import TestCase, main

from classes.game.point import Point
from classes.exceptions.point import *

class TestPointClass(TestCase):

  def setUp(self):
    pass

  def test_regular_initialization(self):
    point = Point(0,0)
    self.assertEqual(point.x, 0)
    self.assertEqual(point.y, 0)

  def test_regular_initialization_place(self):
    point = Point(0,1)
    self.assertEqual(point.x, 0)
    self.assertEqual(point.y, 1)
    point = Point(1,0)
    self.assertEqual(point.x, 1)
    self.assertEqual(point.y, 0)

  def test_str(self):
    self.assertEqual(str(Point(0,0)), 'Point(0,0)')
    self.assertEqual(str(Point(1,0)), 'Point(1,0)')
    self.assertEqual(str(Point(0,1)), 'Point(0,1)')
    self.assertEqual(str(Point(1,1)), 'Point(1,1)')
    self.assertEqual(str(Point(123,7654)), 'Point(123,7654)')

  def test_eq(self):
    self.assertEqual(Point(0,0), Point(0,0))
    point = Point(1,0)
    self.assertEqual(point, Point(1,0))
    self.assertEqual(point, point)
    point = Point(0,1)
    self.assertEqual(point, Point(0,1))
    point1, point2 = Point(1,1), Point(1,1)
    self.assertEqual(point1, point2)

  def test_neq(self):
    point = Point(1,1)
    self.assertNotEqual(point, Point(0,0))
    point1, point2 = Point(1,0), Point(0,1)
    self.assertNotEqual(point1, point2)
    self.assertFalse(Point(0,0) != Point(0,0))
    point1, point2 = Point(0,0), Point(0,0)
    self.assertFalse(point1 != point2)
    self.assertFalse(point1 != point1)

  def test_list_initialization(self):
    self.assertEqual(Point([1,1]), Point(1,1))

  def test_tuple_initialization(self):
    self.assertEqual(Point((1,1)), Point(1,1))

  def test_dictionary_initialization(self):
    self.assertEqual(Point({'x': 1, 'y': 0}), Point(1,0))
    self.assertEqual(Point({'y': 1, 'x': 0}), Point(0,1))

  def test_add(self):
    point1 = Point(1,0)
    point2 = Point(0,1)
    point3 = point1 + point2
    self.assertEqual(point3, Point(1,1))
    self.assertEqual(point1, Point(1,0))
    self.assertEqual(point2, Point(0,1))
    self.assertEqual(Point(1,2) + Point(3,4), Point(4,6))

  def test_iadd(self):
    point1 = Point(1,0)
    point2 = Point(0,1)
    point1 += point2
    self.assertEqual(point1, Point(1,1))
    self.assertEqual(point2, Point(0,1))

  def test_sub(self):
    point1 = Point(1,1)
    point2 = Point(0,1)
    point3 = point1 - point2
    self.assertEqual(point3, Point(1,0))
    self.assertEqual(point1, Point(1,1))
    self.assertEqual(point2, Point(0,1))
    self.assertEqual(Point(3,4) - Point(1,2), Point(2,2))

  def test_isub(self):
    point1 = Point(1,1)
    point2 = Point(0,1)
    point1 -= point2
    self.assertEqual(point1, Point(1,0))
    self.assertEqual(point2, Point(0,1))

  def test_exception_non_integer_coordinates(self):
    current_exception = NonIntegerPointCoordinates 
    self.assertRaises(current_exception, Point, (0.0, 0.0))
    self.assertRaises(current_exception, Point, (0.0, 0))
    self.assertRaises(current_exception, Point, (0, 0.0))
    self.assertRaises(current_exception, Point, ((0.0, 0)))
    self.assertRaises(current_exception, Point, ([0, 0.0]))
    self.assertRaises(current_exception, Point, ({'x': 0, 'y': 0.0}))
    self.assertRaises(current_exception, Point, ({'x': 0.0, 'y': 0}))
    self.assertRaises(current_exception, Point, ({'x': 0.0, 'y': 0.0}))

  def test_exception_coordinates_key_error(self):
    current_exception = CoordinatesKeyError
    self.assertRaises(current_exception, Point, {'u': 0, 'v': 0})
    self.assertRaises(current_exception, Point, {'x': 0, 'v': 0})
    self.assertRaises(current_exception, Point, {'u': 0, 'y': 0})

  def test_exception_illegal_point_coordinates_number(self):
    current_exception = IllegalPointCoordinatesNumber
    self.assertRaises(current_exception, Point, 0)
    self.assertRaises(current_exception, Point, (0, 0, 0))
    self.assertRaises(current_exception, Point, (0))
    self.assertRaises(current_exception, Point, ((0, 0, 0)))
    self.assertRaises(current_exception, Point, [0])
    self.assertRaises(current_exception, Point, [0,0,0])
    self.assertRaises(current_exception, Point, ({'x': 0, 'y': 0, 'z': 0}))

if __name__ == '__main__':
  main()
