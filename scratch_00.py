import pygame
from map import Map
from player import Player
from game import Game
import config

pygame.init()

running = True
screen = pygame.display.set_mode((config.SCREEN_SIZE, config.SCREEN_SIZE))
clock = pygame.time.Clock()
game_objects: list[Game] = []

mapa = Map(screen)
player = Player(screen)
game_objects.append(mapa)
game_objects.append(player)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(60)


pygame.quit()
for obj in game_objects:
    obj.stop()
