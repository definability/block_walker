class AbstractDrawer(object):

  _instance = dict()

  def __new__(cls):
    if cls not in cls._instance:
      cls._instance[cls] = super(AbstractDrawer, cls).__new__(cls)
    return cls._instance[cls]

  def draw(self, object_type, position, state):
    """Add object of `object_type` in `state` to `position` of scene"""
    raise NotImplementedError()

  def render(self):
    """Render all objects"""
    raise NotImplementedError()
