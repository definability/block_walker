from unittest import TestCase, main

from classes.util.singleton import Singleton

class TestPointClass(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_only_instance(self):
    instance_a = Singleton()
    instance_b = Singleton()
    self.assertTrue(instance_a is instance_b)

  def test_inheritance(self):
    class A(Singleton):
      pass
    class B(Singleton):
      pass
    instance_a = A()
    instance_b = B()
    self.assertFalse(instance_a is instance_b)

if __name__ == '__main__':
  main()
