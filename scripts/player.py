import pygame
from game import GameObject
import threading
import config


class Player(GameObject):
    def ready(self) -> None:
        self.pos = [0, 0]
        self.direction = "right"
        self.running = True
        threading.Thread(target=self.move).start()

    def stop(self) -> None:
        self.running = False

    def get_position(self) -> list:
        return [self.pos[0] * config.PLAYER_SIZE, self.pos[1] * config.PLAYER_SIZE]

    def move(self) -> None:
        while self.running:
            if self.direction == "up":
                self.pos[1] -= 1
            if self.direction == "down":
                self.pos[1] += 1
            if self.direction == "left":
                self.pos[0] -= 1
            if self.direction == "right":
                self.pos[0] += 1

            if self.pos[0] > config.BLOCKS_PER_LINE - 1:
                self.pos[0] = 0
            if self.pos[0] < 0:
                self.pos[0] = config.BLOCKS_PER_LINE - 1

            if self.pos[1] > config.BLOCKS_PER_LINE - 1:
                self.pos[1] = 0
            if self.pos[1] < 0:
                self.pos[1] = config.BLOCKS_PER_LINE - 1

            pygame.time.wait(500)

    def process(self) -> None:
        pygame.draw.rect(self.screen, 'green', self.get_position() + [config.PLAYER_SIZE, config.PLAYER_SIZE])

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.direction != "down":
            self.direction = "up"
        if keys[pygame.K_s] and self.direction != "up":
            self.direction = "down"
        if keys[pygame.K_a] and self.direction != "right":
            self.direction = "left"
        if keys[pygame.K_d] and self.direction != "left":
            self.direction = "right"
