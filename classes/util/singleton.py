class Singleton(object):

  instance = dict()

  def __new__(cls):
    if cls not in cls.instance:
      cls.instance[cls] = super(Singleton, cls).__new__(cls)
    return cls.instance[cls]

