import pygame
import sys
from pygame.locals import *
from random import randrange, choice

SIZE = 600, 480
BG_COLOR = Color('white')
FG_COLOR = Color('blue')

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Sierpiński triangle')
screen.fill(BG_COLOR)

offset = 20

vertices = (SIZE[0] // 2, offset), (offset, SIZE[1] - offset), (SIZE[0] - offset, SIZE[1] - offset)
pygame.draw.aalines(screen, FG_COLOR, True, vertices)
p = randrange(SIZE[0]), randrange(SIZE[1])

done = False
i = 0
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
    c = choice(vertices)
    p = (c[0] + p[0]) // 2, (c[1] + p[1]) // 2
    i += 1
    if i > 9:
        screen.set_at(p, FG_COLOR)

    pygame.display.update()
pygame.quit()
sys.exit()
