import pygame, sys
from math import dist
from random import randrange
from pygame.locals import *

SIZE = 400, 400
FPS = 30
BG_COLOR, FG_COLOR = Color('black'), Color('white')
BALL_RADIUS = 5

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Balls')
clock = pygame.time.Clock()

balls = [(randrange(SIZE[0]), randrange(SIZE[1])) for _ in range(20)]


def verify_mouse(c):
    for b in balls:
        if dist(c, b) <= BALL_RADIUS:
            return b


done = False
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]:
            if b := verify_mouse(pygame.mouse.get_pos()):
                balls.remove(b)

    screen.fill(BG_COLOR)
    for b in balls:
        pygame.draw.circle(screen, FG_COLOR, b, 5)
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
