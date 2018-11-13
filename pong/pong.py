# Little Pong implementation

VERSION = "0"

# color constants RGB format
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# some constants for the game
SIZE = (800, 640)
BALL_RADIUS = 5

try:
    import sys
    import random
    import math
    import os
    import pygame
    import pong_objects as po
    from pygame.locals import *
except ImportError as err:
    print(err)
    sys.exit()


def main():
    # general initialisation
    game_speed = 60
    random.seed()
    pygame.init()
    pygame.key.set_repeat(1000, 100)
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption('Pong')
    # set up black background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)
    # Clock object to control game speed
    timer = pygame.time.Clock()
    # game objects
    start_angle = random.random()*2*math.pi - math.pi
    start_speed = 2*BALL_RADIUS - 1
    ball = po.Ball((SIZE[0]/2, SIZE[1]/2), (start_angle, start_speed),
                   BALL_RADIUS)
    # main game loop
    screen.blit(background, (0, 0))
    screen.blit(ball.image, ball.get_pos())
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_UP:
                    game_speed += 5
                if event.key == K_DOWN:
                    game_speed -= 5
                if event.key == K_SPACE:
                    ball.toggle_open_sides()
                    print(ball.opensides)
        screen.blit(background, ball.rect, ball.rect)
        ball.update()
        screen.blit(ball.image, ball.get_pos())
        pygame.display.flip()
        timer.tick(game_speed)

if __name__ == "__main__":
    main()
