import pygame
import sys
from math import dist, pi
from random import randrange
from pygame.locals import *

SIZE = 400
COLOR_IN, COLOR_OUT = Color('green'), Color('red')

pygame.init()
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('Monte-Carlo method')

nb_total = nb_in = 0
done = False
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True

    p = randrange(SIZE), randrange(SIZE)
    if inside := dist((0, 0), p) <= SIZE:
        nb_in += 1
    nb_total += 1
    screen.set_at(p, COLOR_IN if inside else COLOR_OUT)
    pygame.display.update()

print('Total Number of Points:', nb_total)
print('Number of Points drawn inside the circle:', nb_in)
print('Approximation of Pi:', approx := 4 * nb_in / nb_total)
print('Absolute value of delta:', abs(approx - pi))

pygame.quit()
sys.exit()
