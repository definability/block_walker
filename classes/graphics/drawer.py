from classes.util.singleton import Singleton

class AbstractDrawer(Singleton):

  def draw(self, object_type, position, state):
    """Add object of `object_type` in `state` to `position` of scene"""
    raise NotImplementedError()

  def render(self):
    """Render all objects"""
    raise NotImplementedError()
