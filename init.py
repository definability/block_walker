import operator

# http://stackoverflow.com/a/497931/1305036
class stuple(tuple):
  def __add__(self, other):
    return self.__class__(map(operator.add, self, other))

MAP   = [
    '####################',
    '#                  #',
    '#                  #',
    '#                  #',
    '#                  #',
    '#                  #',
    '#                  #',
    '#           0      #',
    '#                  #',
    '#        @         #',
    '#                  #',
    '#                  #',
    '#                  #',
    '#                  #',
    '#                  #',
    '#                  #',
    '#                  #',
    '#                  #',
    '#                  #',
    '####################'
    ]

def find_ship(field):
  ship_column  = -1
  ship_row     = -1
  for row in field:
    ship_row += 1
    try:
      ship_column = row.index('@')
      field[ship_row] = field[ship_row].replace('@', '*')
      break
    except:
      continue
  return (ship_row, ship_column)
