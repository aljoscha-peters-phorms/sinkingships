import curses
import time
from curses import wrapper

def main(stdscr):
    # Clear screen
    
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_YELLOW)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_GREEN)
    curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_WHITE)
    BLUE_AND_YELLOW = curses.color_pair(1)
    RED_AND_GREEN = curses.color_pair(2)
    blue_and_white = curses.color_pair(3)

    counter_win = curses.newwin(1,20,10,10)
    
    for i in range(100):
        counter_win.clear()
        color = blue_and_white
        if i % 2 == 0:
            color = BLUE_AND_YELLOW
        counter_win.addstr(f'Count: {i}', color)
        counter_win.refresh()
        time.sleep(0.1)
    stdscr.getch()

wrapper(main)