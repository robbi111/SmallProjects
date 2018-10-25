# Little Pong implementation

VERSION = "0"

# color constants RGB format
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# some constants for the game
SIZE = (500, 500)

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
    random.seed()
    pygame.init()
    pygame.display.set_caption('Pong')
    screen = pygame.display.set_mode(SIZE)
    ball = po.Ball(0)
    screen.fill(BLACK)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

        screen.fill(BLACK)
        screen.blit(ball.image, (random.randrange(SIZE[0]),
                    random.randrange(SIZE[1])))
        pygame.display.flip()
        pygame.time.delay(1000)

if __name__ == "__main__":
    main()
