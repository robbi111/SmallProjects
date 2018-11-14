# Little Pong implementation

VERSION = "0"

# color constants RGB format
colors = {"WHITE": (255, 255, 255), "BLACK": (0, 0, 0)}
# some constants for the game
game_dim = {"SIZE": (800, 640), "BALL_RADIUS": 5, "PADDLE_SIZE": (10, 100)}

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
    # delay=100ms, interval=10ms
    pygame.key.set_repeat(50, 5)
    screen = pygame.display.set_mode(game_dim["SIZE"])
    pygame.display.set_caption('Pong')
    # set up black background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(colors["BLACK"])
    # Clock object to control game speed
    timer = pygame.time.Clock()
    # game objects
    start_angle = random.random()*2*math.pi - math.pi
    start_speed = 2*game_dim["BALL_RADIUS"] - 1
    ball = po.Ball((game_dim["SIZE"][0]/2, game_dim["SIZE"][1]/2),
                   (start_angle, start_speed), game_dim["BALL_RADIUS"])
    paddle_l = po.Paddle("left")
    paddle_r = po.Paddle("right")
    paddle_group = pygame.sprite.Group(paddle_l, paddle_r)
    ball_group = pygame.sprite.Group(ball)
    # main game loop
    screen.blit(background, (0, 0))
    screen.blit(ball.image, ball.get_pos())
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit()
                if event.key == K_UP:
                    paddle_r.moveup(10)
                if event.key == K_DOWN:
                    paddle_r.movedown(10)
                if event.key == K_a:
                    paddle_l.moveup(10)
                if event.key == K_z:
                    paddle_l.movedown(10)
                if event.key == K_SPACE:
                    ball.toggle_open_sides()
                    print(ball.opensides)
        screen.blit(background, ball.rect, ball.rect)
        screen.blit(background, paddle_r.rect, paddle_r.rect)
        screen.blit(background, paddle_l.rect, paddle_l.rect)
        ball_group.update()
        paddle_group.update()
        ball_group.draw(screen)
        paddle_group.draw(screen)
        # screen.blit(ball.image, ball.get_pos())
        pygame.display.flip()
        timer.tick(game_speed)

if __name__ == "__main__":
    main()
