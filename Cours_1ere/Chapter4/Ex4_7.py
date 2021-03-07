import pygame, sys
from pygame.locals import *
from random import randint

SIZE = 400, 400
BG_COLOR, FG_COLOR = Color('white'), Color('red')

pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption('Rectangles')
rectangles = []

done = False
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == MOUSEBUTTONDOWN:
            p = pygame.mouse.get_pos()
            if (pressed := pygame.mouse.get_pressed(3))[0]:
                x, y = randint(10, 25), randint(5, 15)
                rectangles.append(pygame.Rect(
                    (max(min(p[0] - x, SIZE[0]), 0), max(min(p[1] - y, SIZE[1]), 0), x * 2, y * 2)))
            if pressed[2]:
                rectangles = [r for r in rectangles if not r.collidepoint(p)]

    screen.fill(BG_COLOR)
    for r in rectangles:
        pygame.draw.rect(screen, FG_COLOR, r, 1)

    pygame.display.update()

pygame.quit()
sys.exit()
