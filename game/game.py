import threading
import pygame


class Game:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.running = True
        self.thread = threading.Thread(target=self.__run)

        self.ready()
        self.thread.start()

    def ready(self) -> None:
        pass

    def process(self) -> None:
        pass

    def __run(self) -> None:
        while self.running:
            self.process()

    def stop(self) -> None:
        self.running = False
