from game import GameObject
import pygame
import config


class Map(GameObject):
    def process(self) -> None:
        self.screen.fill('white')
