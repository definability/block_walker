from unittest import TestCase, main

from classes.game.game_object import GameObject
from classes.exceptions.game_object import *

class TestPointClass(TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_invalid_state(self):
    class InvalidGameObject(GameObject):
      def check_state(self, state):
        return False
    self.assertRaises(InvalidGameObjectState, InvalidGameObject,
                                              None, None, None)

if __name__ == '__main__':
  main()
