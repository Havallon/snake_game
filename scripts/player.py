import pygame
import threading
import config
import gc
from game import GameObject
from .apple import Apple


class SnakeBody:
    def __init__(self, x, y):
        self.pos = [x, y]

    def get_position(self) -> list:
        return [self.pos[0] * config.PLAYER_SIZE, self.pos[1] * config.PLAYER_SIZE]


class Player(GameObject):
    def ready(self) -> None:
        self.pos = [0, 0]
        self.direction = "right"
        self.running = True
        self.apple = self.get_apple_object()
        self.tails: list[SnakeBody] = []
        threading.Thread(target=self.move).start()

    def get_apple_object(self) -> Apple:
        for obj in gc.get_objects():
            if isinstance(obj, Apple):
                return obj
        return None

    def stop(self) -> None:
        self.running = False

    def get_position(self) -> list:
        return [self.pos[0] * config.PLAYER_SIZE, self.pos[1] * config.PLAYER_SIZE]

    def move(self) -> None:
        while self.running:
            temp_pos = []
            for k, v in enumerate(self.tails):
                temp_pos.append([v.pos[0], v.pos[1]])
            for k, v in enumerate(self.tails):
                if k == 0:
                    v.pos[0] = self.pos[0]
                    v.pos[1] = self.pos[1]
                else:
                    v.pos[0] = temp_pos[k - 1][0]
                    v.pos[1] = temp_pos[k - 1][1]

            if self.direction == "up":
                self.pos[1] -= 1
            if self.direction == "down":
                self.pos[1] += 1
            if self.direction == "left":
                self.pos[0] -= 1
            if self.direction == "right":
                self.pos[0] += 1

            self.get_apple_collision()

            if self.pos[0] > config.BLOCKS_PER_LINE - 1:
                self.pos[0] = 0
            if self.pos[0] < 0:
                self.pos[0] = config.BLOCKS_PER_LINE - 1

            if self.pos[1] > config.BLOCKS_PER_LINE - 1:
                self.pos[1] = 0
            if self.pos[1] < 0:
                self.pos[1] = config.BLOCKS_PER_LINE - 1

            pygame.time.wait(200)

    def get_apple_collision(self):
        if self.pos[0] == self.apple.pos[0] and self.pos[1] == self.apple.pos[1]:
            self.apple.respawn()
            if len(self.tails) == 0:
                self.tails.append(SnakeBody(self.pos[0], self.pos[1]))
            else:
                tail = self.tails[-1]
                self.tails.append(SnakeBody(tail.pos[0], tail.pos[1]))

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

        for k, v in enumerate(self.tails):
            pygame.draw.rect(self.screen, 'green', v.get_position() + [config.PLAYER_SIZE, config.PLAYER_SIZE], config.PLAYER_SIZE, int(config.PLAYER_SIZE / 2))
