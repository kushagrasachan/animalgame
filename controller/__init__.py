import time

import view
import model
from view.player_actions import PlayerActions
from common.directions import Directions

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)


class Controller:
    def __init__(self) -> None:
        self._view = view.View()
        self._model = model.Model()
        self._view.setup()
        self.continue_execution = True

    def play(self):    
        while self.continue_execution:
            self.tick_forward()
            time.sleep(0.4)
            # self._view._game_window.timeout(300)

    def tick_forward(self):
        # player_action = self._view.get_player_input()
        # logger.info(f"tick_forward called, player input received was {player_action}")

        if (self._model.is_player_alive() == False):
            logger.info(f"player unalive?")
            self.continue_execution = False
        else:
            self._handle_player_input()

        self._model.tick_forward()

        self._view.print_field()

    def _handle_player_input(self):
        player_action = self._view.get_player_input()
        logger.info(f"handling inputs, got {player_action}")

        while player_action == PlayerActions.MISCLICKED:
            logger.info("misclicked")
            player_action = self._view.get_player_input()

        if player_action == PlayerActions.MOVE_PLAYER_RIGHT:
            self._model.player.move(Directions.RIGHT)
        elif player_action == PlayerActions.MOVE_PLAYER_LEFT:
            self._model.player.move(Directions.LEFT)
        elif player_action == PlayerActions.SHOOT:
            self._model.player.shoot()
        elif player_action == PlayerActions.PAUSE_GAME:
            # busy waiting as Pause
            player_action = self._view.get_player_input()
            while player_action != PlayerActions.PAUSE_GAME and player_action != PlayerActions.QUIT_GAME:
                player_action = self._view.get_player_input()
                time.sleep(0.1)
        elif player_action == PlayerActions.QUIT_GAME:
            self.continue_execution = False
