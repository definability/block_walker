class InvalidGameObjectState(Exception):
  def __init__(self, state):
    super(InvalidGameObjectState, self).__init__(
          "Invalid Game Object state %s"%repr(state))
