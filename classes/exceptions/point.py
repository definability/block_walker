from os import linesep
CORRECT_COORDINATES_NUMBER = 2
STD_IPA_MSG = "You should use list or tuple of coordinates, " + \
              "or enumerate point's coordinates"

class PointInitializationError(Exception):
  def __init__(self, message):
    super(PointInitializationError, self).__init__(message)

class IllegalPointArguments(PointInitializationError):
  def __init__(self, arguments, message=STD_IPA_MSG):
    super(IllegalPointArguments, self).__init__(
          """Arguments `%s` are illegal.%s%s"""%\
          (repr(arguments), linesep, message))

class NonIntegerPointCoordinates(IllegalPointArguments):
  def __init__(self, arguments):
    super(NonIntegerPointCoordinates, self).__init__(arguments,
        "You should use integers instead")

class IllegalPointCoordinatesNumber(IllegalPointArguments):
  def __init__(self, arguments, arguments_number=-1):
    super(IllegalPointCoordinatesNumber, self).__init__(arguments,
          "You have %d integer coordinate(s), but you should have %d"%
          (len(arguments) if arguments_number == -1 else arguments_number,
           CORRECT_COORDINATES_NUMBER))

class CoordinatesKeyError(IllegalPointArguments):
  def __init__(self, arguments):
    super(CoordinatesKeyError, self).__init__(arguments,
        "You should use dictionary with items `x' and `y'")
