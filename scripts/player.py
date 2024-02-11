import pygame
from game import GameObject


class Player(GameObject):
    def ready(self) -> None:
        self.pos = [0, 0]

    def process(self) -> None:
        pygame.draw.rect(self.screen, 'black', self.pos + [40, 40])
        self.pos[0] += 10
