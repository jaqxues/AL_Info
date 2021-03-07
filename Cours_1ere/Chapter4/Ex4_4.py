import pygame, sys
from pygame.locals import *

SIZE = WIDTH, HEIGHT = 600, 450
FPS = 30

x_min, x_max = -2.2, 1.0
y_min, y_max = -1.2, 1.2
MAX_ITER, MAX_RADIUS = 255, 10


def row_by_row(s):
    for j in range(HEIGHT):
        for i in range(WIDTH):
            c = complex(*get_xy_value(i, j))

            z = ni = 0
            for ni in range(1, MAX_ITER):
                z = z ** 2 + c
                if z.real ** 2 + z.imag ** 2 > MAX_RADIUS ** 2:
                    break
            s.set_at((i, j), pygame.Color(255 - ni, max(255 - 2 * ni, 0), 0))
        yield True


def get_xy_value(i, j):
    return (x_max - x_min) * (i / WIDTH) + x_min, (y_max - y_min) * (j / HEIGHT) + y_min


pygame.init()
screen = pygame.display.set_mode(SIZE)
surface = pygame.surface.Surface(SIZE)
pygame.display.set_caption('Mandelbrot set')
clock = pygame.time.Clock()

done = False
iterator = row_by_row(surface)
start_drag = None
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
        elif evt.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]:
            start_drag = pygame.mouse.get_pos()
        elif evt.type == MOUSEBUTTONUP and not pygame.mouse.get_pressed(3)[0]:
            (x_min, y_min), (x_max, y_max) = get_xy_value(*start_drag), get_xy_value(*pygame.mouse.get_pos())
            if x_min > x_max:
                x_min, x_max = x_max, x_min
            if y_min > y_max:
                y_min, y_max = y_max, y_min
            iterator = row_by_row(surface)
            surface.fill(Color('black'))
            start_drag = None

    if not next(iterator, False):
        # After all rows have been drawn, limit FPS
        clock.tick(FPS)

    screen.blit(surface, (0, 0, *SIZE))
    if start_drag:
        (s1, s2), (c1, c2) = start_drag, pygame.mouse.get_pos()
        pygame.draw.rect(screen, Color('white'), (s1, s2, c1 - s1, c2 - s2), 1)

    pygame.display.update()

pygame.quit()
sys.exit()
