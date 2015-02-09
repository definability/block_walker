#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/TrevorBasinger/Python-Curses-Demo
# Curses docs: https://docs.python.org/2/library/curses.html
import curses, traceback, operator, copy

# http://stackoverflow.com/a/497931/1305036
class stuple(tuple):
  def __add__(self, other):
    return self.__class__(map(operator.add, self, other))

KEY_MOVE_UP     = 'k'
KEY_MOVE_DOWN   = 'j'
KEY_MOVE_LEFT   = 'h'
KEY_MOVE_RIGHT  = 'l'

KEYS  = [KEY_MOVE_UP, KEY_MOVE_DOWN,  KEY_MOVE_LEFT,  KEY_MOVE_RIGHT]
MOVES = [(0,-1),      (0,1),          (-1,0),         (1,0)         ]
SHIP  = ['^',         'v',            '<',            '>'           ]
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

def main(stdscr):
  global screen
  global ship
  ship = '@'
  global field, columns, rows
  #columns = rows = 20
  #field = [' ' * columns] * rows
  field = copy.deepcopy(MAP)
  screen = stdscr.subwin(0, 0)
  #screen.box() # Wrap screen window in box
  #screen.resize(columns,rows)
  # Get window diminsions
  y, x = screen.getmaxyx()
  global ship_x, ship_y;
  # Sets the cursor to center the ship on screen
  #ship_x = (x/2)
  #ship_y = (y/2)
  ship_x, ship_y = find_ship(field)
  if ship_x < 0 or ship_y < 0:
    raise Exception('Error!')
  # Add string to screen
  redraw_map()
  screen.addstr(ship_y, ship_x, ship) 
  screen.refresh() # Refresh to populate screen with data

  global won
  won = False

  c = screen.getkey() # Get char
  while c != 'q': # Exit loop if char caught is 'q'
    if c.lower() in KEYS:
      redraw_map()
      move_ship(c)
      draw_ship()
    if c == ' ':
      make_block()
      redraw_map()
      draw_ship()
    if game_over():
      break
    c = screen.getkey()

  screen.clear()
  screen.box() # Wrap screen window in box
  y, x = screen.getmaxyx()
  if won:
    text = "You won!"
  else:
    text = "You lose!"
  screen.addstr(y/2, x/2 - len(text)/2, text)
  screen.refresh()

  c = screen.getkey() # Get char
  while c != 'q': # Exit loop if char caught is 'q'
    c = screen.getkey() # Get char

  return

def game_over():
  global ship_x, ship_y;
  if MAP[ship_y][ship_x] == '0':
    global won
    won = True
    return True
  else:
    return False

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

def redraw_map():
  screen.clear()
  #screen.box()
  #screen.resize(20,20)
  #for i in range(len(MAP)-1):
  #  for j in range(len(MAP[i])):
  #    screen.addstr(i, j, '*')
  screen.addstr(0, 0, "\n".join(field))
  return

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

if __name__ == '__main__':
  try:
    # Initialize curses
    stdscr=curses.initscr()

    # Turn off echoing of keys, and enter cbreak mode,
    # where no buffering is performed on keyboard input
    curses.noecho()
    curses.cbreak()

    # In keypad mode, escape sequences for special keys
    # will be interpreted and a special value like
    # curses.KEY_LEFT will be returned
    stdscr.keypad(1)
    curses.curs_set(0) # Hide cursor position

    main(stdscr) # enter main loop
  except curses.error:
    # In the event of error, restore terminal to sane state
    traceback.print_exc() # Print the exception
    print(curses.ERR)
  except KeyboardInterrupt:
    # Caught KeyboardInterrupt (Gets rid of stacktrace)
    # Set everything back to normal before exit
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
    exit()
  finally:
    # Set everything back to normal
    stdscr.keypad(0)
    curses.echo()
    curses.nocbreak()
    curses.endwin()
