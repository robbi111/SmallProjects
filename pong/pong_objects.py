# Collection of game objects used in Pong, i.e. Ball, Player, HumanPlayer,
# BotPLayer, ...

try:
    import sys
    import math
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

    def __init__(self, pos=(0, 0), vector=(0, 0), r=5):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2*r, 2*r))
        self.rect = self.image.get_rect()
        self.rect.move_ip(pos[0], pos[1])
        self.vector = vector
        self.area = pygame.display.get_surface().get_rect()
        # remove black background
        self.image.fill((0, 0, 0))
        self.image.set_colorkey((0, 0, 0))
        self.image.set_alpha(255)
        pygame.draw.circle(self.image, pygame.Color(255, 255, 255), (r, r), r)

    def inc_speed(self, inc):
        (angle, z) = self.vector
        self.vector = (angle, z+inc)

    def dec_speed(self, dec):
        (angle, z) = self.vector
        new_z = z - dec
        if new_z < 0:
            new_z = 0
        self.vector = (angle, new_z)

    def update(self):
        newpos = self.calcnewpos(self.rect, self.vector)
        self.rect = newpos
        (angle, z) = self.vector

        if not self.area.contains(newpos):
            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)
            if tr and tl or (br and bl):
                angle = -angle
            if tl and bl:
                # self.offcourt()
                angle = math.pi - angle
            if tr and br:
                angle = math.pi - angle
                # self.offcourt()
        self.vector = (angle, z)

    def get_pos(self):
        return self.rect

    def move(self, offset):
        self.rect.move_ip(offset[0], offset[1])

    def calcnewpos(self, rect, vector):
        (angle, z) = vector
        (dx, dy) = (z*math.cos(angle), z*math.sin(angle))
        return rect.move(dx, dy)
