from entity.player import Player
from entity.fire import Fire

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

class Model:
    def __init__(self) -> None:
        self._all_animals = []
        self._all_fires = []
        self.player = Player()

    def is_player_alive(self):

        return True
    
    def tick_forward(self):
        pass
