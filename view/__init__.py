import curses
import _curses
import utils
from view.player_actions import PlayerActions

import numpy as np
import random
import locale
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)



class View:
    def __init__(self) -> None:
        self._game_window = curses.initscr()

    def __del__(self) -> None:
        utils.revert_curses()

    def setup(self):
        utils.setup_curses()
        self._game_window.nodelay(1)
        self._game_window.border(0)

    def get_player_input(self) -> PlayerActions:
        player_input = self._game_window.getch()

        if player_input == curses.ERR:
            return PlayerActions.NOTHING
        elif player_input == curses.KEY_LEFT:
            return PlayerActions.MOVE_PLAYER_LEFT
        elif player_input == curses.KEY_RIGHT:
            return PlayerActions.MOVE_PLAYER_RIGHT
        elif player_input == 32:                                        # Space bar pressed
            return PlayerActions.SHOOT
        elif player_input == 80 or player_input == 112:                 # P or p pressed
            return PlayerActions.PAUSE_GAME
        elif player_input == 27:                                        # Esc key pressed
            return PlayerActions.QUIT_GAME
        else:
            return PlayerActions.MISCLICKED
        
    def print_field(self) -> None:
        self.demo()
        self._game_window.refresh()         # crucial to actually displaying the modifications made to the screen






########
    def demo(self):
            animal = np.array(
            [[(10,1,1), (10,2,1), (10,3,1)], \
            [(11,1,1),(11,2,0),(11,3,1)], \
            [(12,1,1),(12,2,1),(12,3,1)]]
            )

            b = "██".encode(locale.getpreferredencoding())

            r1 = random.randint(-10,10)
            r2 = random.randint(-10,10)
            try:    #try-except block to handle errors from terminal sizing
                for i in range(len(animal)):
                    for j in range(len(animal[0])):
                        if animal[i][j][2]==1: self._game_window.addstr(animal[i][j][0]+r1,animal[i][j][1]*2 +r2, "*")
            except _curses.error:
                logger.info(f"{_curses.error}")
                pass