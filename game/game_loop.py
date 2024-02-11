from .game_object import GameObject
import pygame
import config


class GameLoop:
    def __init__(self, game_object_list: list[GameObject] = []) -> None:
        pygame.init()
        self.game_objects: list[GameObject] = []
        self.screen = pygame.display.set_mode(config.SCREEN_SIZE)

        for obj in game_object_list:
            self.game_objects.append(obj(self.screen))

        self.running = True
        self.clock = pygame.time.Clock()
        self.__run()

    def __run(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            for obj in self.game_objects:
                obj.process()

            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
