from unittest import TestCase, main

from classes.graphics.drawer import AbstractDrawer

class TestPointClass(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_initialization(self):
    ad = AbstractDrawer()
    self.assertIsInstance(ad, AbstractDrawer)

  def test_not_implemented_methods(self):
    ad = AbstractDrawer()
    self.assertRaises(NotImplementedError, ad.draw, None, None, None)
    self.assertRaises(NotImplementedError, ad.render)


if __name__ == '__main__':
  main()
