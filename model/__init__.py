import random
from entity.player import Player
from entity.fire import Fire
from entity.animal import Animal
from common import config

import logging
logger = logging.getLogger(__name__)
logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)

class Model:
    def __init__(self) -> None:
        self._all_animals = []
        self._all_fires = []
        self.player = Player()

    def is_player_alive(self):
        """
        Yet to design additional game mechanics to pose a threat to the player
        """
        return True
    
    def add_animal(self, thresh=0.875):
        r = random.random()
        if r >= thresh:
            x = random.randint(1, config.TERM_WIDTH-1)
            y = random.randint(1, config.TERM_HEIGHT-5)
            self._all_animals.append(Animal(x,y))

    def tick_forward(self):
        self.add_animal()
        pass
