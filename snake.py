# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
running = True
dt = 0
pygame.display.set_caption("Snake Game")

rect_x = 0
rect_y = 0
direction = "rigth"

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.rect(screen, 'green', [rect_x, rect_y, 40, 40], 40)

    for i in range(0, 10):
        for j in range(0, 10):
            pygame.draw.rect(screen, 'white', [i*40, j*40, 40, 40], 1)

    if direction == "up":
        rect_y -= 40 * dt
    if direction == "down":
        rect_y += 40 * dt
    if direction == "left":
        rect_x -= 40 * dt
    if direction == "rigth":
        rect_x += 40 * dt

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and direction != "down":
        direction = "up"
    if keys[pygame.K_s] and direction != "up":
        direction = "down"
    if keys[pygame.K_a] and direction != "rigth":
        direction = "left"
    if keys[pygame.K_d] and direction != "left":
        direction = "rigth"

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
