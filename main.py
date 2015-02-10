#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://github.com/TrevorBasinger/Python-Curses-Demo
# Curses docs: https://docs.python.org/2/library/curses.html
import curses, traceback, copy
import * from init
import * from ship

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

def redraw_map():
  screen.clear()
  screen.addstr(0, 0, "\n".join(field))
  return

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
