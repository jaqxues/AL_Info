import pygame, sys
from math import sin, cos, pi
from pygame.locals import *
from random import randrange, uniform

SIZE = 400, 400
FPS = 20
CROSS_SIZE = 11
HALF_C = CROSS_SIZE // 2
BG_COLOR, CROSS_COLOR, LINE_COLOR = Color('black'), Color('cyan'), Color('red')

assert CROSS_SIZE % 2, 'Even number as cross size translates to asymmetric cross symbol!'

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Brownian Motion')
clock = pygame.time.Clock()

p = randrange(SIZE[0]), randrange(SIZE[1])
done = False
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True

    pygame.draw.line(screen, CROSS_COLOR, (p[0] - HALF_C, p[1] - HALF_C), (p[0] + HALF_C, p[1] + HALF_C))
    pygame.draw.line(screen, CROSS_COLOR, (p[0] - HALF_C, p[1] + HALF_C), (p[0] + HALF_C, p[1] - HALF_C))

    mod, arg = uniform(0, 30), uniform(0, 2 * pi)
    x, y = mod * cos(arg), mod * sin(arg)
    t = max(min(p[0] + x, SIZE[0]), 0), max(min(p[1] + y, SIZE[1]), 0)
    pygame.draw.line(screen, LINE_COLOR, p, t)
    p = t

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
