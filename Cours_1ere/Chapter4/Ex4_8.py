import pygame, sys
from pygame.locals import *

SIZE = 600, 200
FPS = 60
BG_COLOR, FG_COLOR = Color('white'), Color('red')

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode(SIZE)
font = pygame.font.SysFont("Palantino", 72)


def flytext(msg, duration):
    ms_dur = int(duration * 1000)
    s = font.render(msg, True, FG_COLOR)

    done = False
    while not done:
        for evt in pygame.event.get():
            if evt.type == pygame.QUIT:
                done = True

        t = pygame.time.get_ticks() % ms_dur
        d_t = 2 * (SIZE[0] - s.get_width()) / ms_dur

        screen.fill(BG_COLOR)
        screen.blit(s, (
            (t * d_t) if t <= ms_dur / 2 else (SIZE[0] - (t * d_t)),
            (SIZE[1] - s.get_height()) // 2
        ))

        clock.tick(FPS)
        pygame.display.update()


flytext('Hello World!', 10)
pygame.quit()
sys.exit()
