from game import GameObject
import pygame
import config


class Map(GameObject):
    def process(self) -> None:
        self.screen.fill('white')

        for i in range(0, config.BLOCKS_PER_LINE):
            for j in range(0, config.BLOCKS_PER_LINE):
                pygame.draw.rect(self.screen, 'black', [i * config.PLAYER_SIZE, j * config.PLAYER_SIZE, config.PLAYER_SIZE, config.PLAYER_SIZE], 1)
