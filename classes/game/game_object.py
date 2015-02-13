from copy import deepcopy

from classes.exceptions.game_object import *

class GameObject(object):

  def __init__(self, position, drawer, state):
    self._position  = position
    self._drawer    = drawer
    self.set_state(state)

  def draw(self):
    self._drawer.draw(type(self), self.position, self.state)

  def check_state(self, state):
    return True

  def set_state(self, state):
    if self.check_state(state):
      self._state = state
    else:
      raise InvalidGameObjectState(state)

  def get_state(self):
    return self._state
