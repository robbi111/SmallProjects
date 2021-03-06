# Collection of game objects used in Pong, i.e. Ball, Player, HumanPlayer,
# BotPLayer, ...

try:
    import sys
    import math
    import pygame
    from pong import colors, game_dim
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
        self.image.fill(colors["BLACK"])
        self.image.set_colorkey(colors["BLACK"])
        self.image.set_alpha(255)
        pygame.draw.circle(self.image, colors["WHITE"], (r, r), r)
        self.opensides = False

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

    def get_pos(self):
        return self.rect

    def move(self, offset):
        self.rect.move_ip(offset[0], offset[1])

    def calcnewpos(self, rect, vector):
        (angle, z) = vector
        (dx, dy) = (z*math.cos(angle), z*math.sin(angle))
        newpos = self.rect.move(dx, dy)

        if not self.area.contains(newpos):
            tl = not self.area.collidepoint(newpos.topleft)
            tr = not self.area.collidepoint(newpos.topright)
            bl = not self.area.collidepoint(newpos.bottomleft)
            br = not self.area.collidepoint(newpos.bottomright)
            if tl and tl and br and bl:
                angle = angle - math.pi
            elif tr and tl:
                angle = -angle
            elif br and bl:
                angle = -angle
            elif tl and bl:
                if self.opensides:
                    z = 0
                angle = math.pi - angle
            elif tr and br:
                if self.opensides:
                    z = 0
                angle = math.pi - angle

        self.vector = (angle, z)
        return newpos

    def toggle_open_sides(self):
        self.opensides = ~self.opensides


class Paddle(pygame.sprite.Sprite):

    def __init__(self, side):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(game_dim["PADDLE_SIZE"])
        self.rect = self.image.get_rect()
        self.area = pygame.display.get_surface().get_rect()
        self.movepos = 0
        if side == "left":
            self.rect.x = 0
        elif side == "right":
            self.rect.right = self.area.width
        self.rect.centery = self.area.height/2
        self.image.fill(colors["WHITE"])
        
    def update(self, *args):
        newpos = self.rect.move(0, self.movepos)
        self.movepos = 0
        if not self.area.contains(newpos):
            if newpos.top < 0:
                newpos.top = 0
            elif newpos.bottom > self.area.height:
                newpos.bottom = self.area.height
        self.rect = newpos

    def moveup(self, step):
        self.movepos = self.movepos - step

    def movedown(self, step):
        self.movepos = self.movepos + step
