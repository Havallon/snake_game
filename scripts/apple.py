import config
import pygame
import random
from game import GameObject


class Apple(GameObject):
    def ready(self) -> None:
        self.pos = [random.randint(0, config.BLOCKS_PER_LINE - 1), random.randint(0, config.BLOCKS_PER_LINE - 1)]

    def get_position(self) -> list:
        pos = [self.pos[0] * config.PLAYER_SIZE, self.pos[1] * config.PLAYER_SIZE]
        while pos[0] == self.pos[0] and pos[1] == self.pos[1]:
            pos = [self.pos[0] * config.PLAYER_SIZE, self.pos[1] * config.PLAYER_SIZE]
        return pos

    def respawn(self) -> None:
        self.pos = [random.randint(0, config.BLOCKS_PER_LINE - 1), random.randint(0, config.BLOCKS_PER_LINE - 1)]

    def process(self) -> None:
        pygame.draw.rect(
            self.screen,
            'red',
            self.get_position() + [config.PLAYER_SIZE, config.PLAYER_SIZE],
            config.PLAYER_SIZE,
            int(config.PLAYER_SIZE / 2)
        )
