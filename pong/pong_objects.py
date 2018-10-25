# Collection of game objects used in Pong, i.e. Ball, Player, HumanPlayer,
# BotPLayer, ...

try:
    import sys
    import pygame
except ImportError as err:
    print(err)
    sys.exit()


class Ball(pygame.sprite.Sprite):
    """Ball that is used to play with in Pong. Moves accross screen and is
    reflected at paddles and horizontal screen borders.
    Returns: Ball object
    Functions: update, calcNewPos
    Attributes: area, vector"""

    def __init__(self, vector, r=5):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2*r, 2*r))
        # remove black background
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        pygame.draw.circle(self.image, pygame.Color(255, 255, 255), (r, r), r)
        self.vector = vector
        self.area = pygame.display.get_surface()

    def update():
        return

    def calcNewPos():
        return
