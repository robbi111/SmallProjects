import sys, pygame
pygame.init()

size = width, height = 640, 480
speed = [0, 1]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
paddle = pygame.Rect((0,0), (20, 80))

while 1:
    tick1 = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    # ballrect = ballrect.move(speed)
    # if ballrect.left < 0 or ballrect.right > width:
    #     speed[0] = -speed[0]
    # if ballrect.top < 0 or ballrect.bottom > height:
    #     speed[1] = -speed[1]

    paddle = paddle.move(speed)
    if paddle.top < 0 or paddle.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    pygame.draw.rect(screen, white, paddle)
    # screen.blit(ball, ballrect)
    pygame.display.flip()

    tick2 = pygame.time.get_ticks()
    pygame.time.wait(40-(tick2-tick1))