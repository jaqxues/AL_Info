import pygame, sys
from pygame.locals import *

SIZE = 400, 300
BG_COLOR, FG_COLOR = pygame.Color('blue'), pygame.Color('red')
SQUARE_SIZE = 20
FPS = 20

pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption('Moving Square')
x, y = SIZE[0] // 2 - SQUARE_SIZE // 2, SIZE[1] - SQUARE_SIZE
controls = {k: False for k in (K_LEFT, K_RIGHT, K_UP, K_DOWN)}

done = False
while not done:
    for evt in pygame.event.get():
        if evt.type == pygame.QUIT:
            done = True
        elif (evt.type == KEYDOWN or evt.type == KEYUP) and evt.key in controls:
            controls[evt.key] = evt.type == KEYDOWN
    if controls[K_LEFT]:
        x -= 5
    if controls[K_RIGHT]:
        x += 5
    if controls[K_UP]:
        y -= 5
    if controls[K_DOWN]:
        y += 5
    x = min(max(x, 0), SIZE[0] - SQUARE_SIZE)
    y = min(max(y, 0), SIZE[1] - SQUARE_SIZE)

    screen.fill(BG_COLOR)
    pygame.draw.rect(screen, FG_COLOR, (x, y, 20, 20))
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
