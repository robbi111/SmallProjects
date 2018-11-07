import pygame
from pygame.locals import *

WHITE = (255, 255, 255)


def main():
    pygame.init()
    screen = pygame.display.set_mode((500, 500), RESIZABLE)
    pygame.display.set_caption('Pong')

    # Background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)
    
    while 1:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == VIDEORESIZE:
                print(event.size)
                screen = pygame.display.set_mode(event.size, RESIZABLE)
                background = pygame.Surface(event.size)
                background = background.convert()
                background.fill(WHITE)

        screen.blit(background, (0, 0))
        pygame.display.flip()


if __name__ == '__main__':
    main()
    