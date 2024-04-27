import curses
import _curses
import time
import locale
import logging
import numpy as np
import copy

def setup_curses() -> None:
    """
    Setup curses to we can correctly use it
    """
    # locale.setlocale(locale.LC_ALL, "")
    curses.curs_set(0)  # don't show cursor
    curses.noecho()  # don't show what is writen by the user
    curses.cbreak()  # don't wait that the user presses Enter to read what they write

def revert_curses() -> None:
    """
    Reset curses to it's original settings, then quit
    """
    curses.curs_set(1)
    curses.nocbreak()
    curses.echo()
    curses.endwin()

# ######################## ######################## #######################

logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

game_window = curses.initscr()
setup_curses()

game_window.nodelay(1)
game_window.border(0)

run = True
i = 0

animal = np.array(
        [[(10,1,1), (10,2,1), (10,3,1)], \
        [(11,1,1),(11,2,0),(11,3,1)], \
        [(12,1,1),(12,2,1),(12,3,1)]]
        )
past_animal = animal

while run:
    i = (i+1) % 5
    inp = game_window.getch()
    # print(f"**{temp==curses.ERR}**" )
    # game_window.addstr(0,15*i,f"**{temp==curses.ERR}**", curses.A_REVERSE )
    game_window.addstr(0,5*i,f"**{inp}**", curses.A_REVERSE )

    ESC = 27
    if(inp == ESC): run = False
    if run == False: curses.endwin()
    # time.sleep(0.3)
    game_window.timeout(300)

    b = "██".encode(locale.getpreferredencoding())

    try:    #try-except block to handle errors from terminal sizing
        for i in range(len(past_animal)):
            for j in range(len(past_animal[0])):
                if past_animal[i][j][2]==1: game_window.addstr(past_animal[i][j][0],past_animal[i][j][1]*2, "  ")
    except _curses.error:
        logger.info(f"{_curses.error}")
        pass

    try:    #try-except block to handle errors from terminal sizing
        for i in range(len(animal)):
            for j in range(len(animal[0])):
                if animal[i][j][2]==1: game_window.addstr(animal[i][j][0],animal[i][j][1]*2, b)
    except _curses.error:
        logger.info(f"{_curses.error}")
        pass

    past_animal = copy.deepcopy(animal)
    animal[:,:,1] = (animal[:,:,1] + 5) % 70

revert_curses()