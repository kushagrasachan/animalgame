import curses
import _curses
import utils
from common import config
from view.player_actions import PlayerActions

import numpy as np
import random
import locale
import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

class View:
    def __init__(self) -> None:
        self._window_space = curses.initscr()
        self._game_window = curses.newwin(config.TERM_HEIGHT, config.TERM_WIDTH,0,0)
        self._statistics_window = curses.newwin(config.STAT_WIN_HEIGHT, \
                                                config.STAT_WIN_WIDTH, \
                                                0, config.TERM_WIDTH+4)

    def __del__(self) -> None:
        utils.revert_curses()

    def setup(self):
        utils.setup_curses()
        self._game_window.nodelay(1)
        self._game_window.border(0)
        self._game_window.keypad(True)
        self._statistics_window.border(0)

    def get_player_input(self) -> PlayerActions:
        player_input = self._game_window.getch()

        if player_input == curses.ERR:
            return PlayerActions.NOTHING
        elif player_input == curses.KEY_LEFT or player_input == 119:
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
        
    def print_field(self, model) -> None:
        # self.first_attempt()
        animal_glyph = "█".encode(locale.getpreferredencoding())
        player_glyph = "†Δ§Δ†".encode(locale.getpreferredencoding())
        # player_glyph = " +\n+++\n +".encode(locale.getpreferredencoding())
        fire_glyph = "•".encode(locale.getpreferredencoding())

        try:
            self._game_window.addstr(model.player.y, model.player.x+1, "     ")
            self._game_window.addstr(model.player.y, model.player.x-1, "     ")
            self._game_window.addstr(model.player.y, model.player.x, player_glyph)
        except:
            logger.info(f"{model.player.x, model.player.y}")
            # logger.info(f"{_curses.error}")
            pass

        # logger.info(f"{model}")
        # logger.info(f"{len(model._all_animals)} animals populated")
        for animal in model._all_animals:
            try:
                self._game_window.addstr(animal.y, animal.x, animal_glyph)
            except:
                pass

        for fire in model._all_fires:
            try:
                self._game_window.addstr(fire.y, fire.x, fire_glyph)
                self._game_window.addstr(fire.y+1, fire.x, " ")
            except:
                logger.info(f"fire posn: {fire.x, fire.y}")
                pass

        self._game_window.refresh()         # crucial to actually displaying the modifications made to the screen

    def print_statistics(self, score:int):
        self._statistics_window.addstr(4, 2, f"SCORE: {score}")
        self._statistics_window.refresh()





########
    def first_attempt(self):
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