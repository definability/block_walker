KEY_MOVE_UP     = 'k'
KEY_MOVE_DOWN   = 'j'
KEY_MOVE_LEFT   = 'h'
KEY_MOVE_RIGHT  = 'l'

KEYS  = [KEY_MOVE_UP, KEY_MOVE_DOWN,  KEY_MOVE_LEFT,  KEY_MOVE_RIGHT]
MOVES = [(0,-1),      (0,1),          (-1,0),         (1,0)         ]
SHIP  = ['^',         'v',            '<',            '>'           ]

def move_ship(key):
  key_index = KEYS.index(key.lower())
  global ship
  ship = SHIP[key_index]
  global ship_x, ship_y
  if key.islower():
    new_x, new_y = stuple([ship_x, ship_y]) + stuple(MOVES[key_index])
    if field[new_y][new_x] in ['*', '0']:
      ship_x, ship_y = new_x, new_y
  return

def draw_ship():
  global ship
  global ship_x, ship_y
  screen.addstr(ship_y, ship_x, ship) 
  screen.refresh() # Refresh to populate screen with data
  return

def make_block():
  global ship
  global ship_x, ship_y
  global field
  block_x, block_y = stuple([ship_x, ship_y]) + stuple(MOVES[SHIP.index(ship)])
  if MAP[block_y][block_x] not in ['#', '0']:
    field[block_y] = field[block_y][:block_x] + '*' + field[block_y][block_x+1:]
