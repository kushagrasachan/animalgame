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
        self.score = 0

    def tick_forward(self) -> None:
        self.add_animal()
        self.move_all_fires()
        self.handle_collisions()
        pass

    def add_animal(self, thresh:int = 0.875) -> None:
        r = random.random()
        if r >= thresh:
            x = random.randint(1, config.TERM_WIDTH-1)
            y = random.randint(1, config.TERM_HEIGHT-5)
            self._all_animals.append(Animal(x,y))

    def add_fire(self) -> None:
        x, y = self.player.x, self.player.y
        self._all_fires.append(Fire(x,y))
        self._all_fires.append(Fire(x,y-1)) #hacky way to deal with collision printing

    def move_all_fires(self) -> None:
        for idx, fire in enumerate(self._all_fires):
            if fire.y > 0:
                fire.y -= 1
            else:
                self._all_fires.pop(idx)
        pass
    
    def handle_collisions(self) -> None:
        for f_idx, fire in enumerate(self._all_fires):
            for a_idx, animal in enumerate(self._all_animals):
                if (fire.x == animal.x and fire.y == animal.y):
                    self._all_fires.pop(f_idx)
                    self._all_animals.pop(a_idx)
                    self.score += 1

    def is_player_alive(self) -> None:
        """
        Yet to design additional game mechanics to pose a threat to the player
        """
        return True

