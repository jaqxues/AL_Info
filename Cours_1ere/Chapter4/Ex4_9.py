import pygame
import sys
from pygame.locals import *

SIZE = 350, 350
CELL_SIZE = 100, 100
LINE_WIDTH = 5
FPS = 30

offsets = tuple((s - 3 * cs - 2 * LINE_WIDTH) // 2 for s, cs in zip(SIZE, CELL_SIZE))
pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()


def draw_board():
    screen.fill(Color('white'))

    def _draw_line(start, end):
        pygame.draw.line(screen, Color('black'), start, end, LINE_WIDTH)

    for i in range(2):
        y = CELL_SIZE[1] * (1 + i) + offsets[1]
        _draw_line((offsets[0], y), (SIZE[0] - offsets[0], y))
    for i in range(2):
        x = CELL_SIZE[0] * (1 + i) + offsets[1]
        _draw_line((x, offsets[1]), (x, SIZE[1] - offsets[1]))


def draw_coin(player, i, j):
    COIN_SIZE = 80, 80
    if player == 0:
        pygame.draw.circle(screen, Color('red'),
                           (offsets[0] + CELL_SIZE[0] * i + CELL_SIZE[0] // 2,
                            offsets[1] + CELL_SIZE[1] * j + CELL_SIZE[1] // 2), 40, 5)
    elif player == 1:
        top = (offsets[0] + CELL_SIZE[0] * i,
               offsets[1] + CELL_SIZE[1] * j)
        coin_offs = (CELL_SIZE[0] - COIN_SIZE[0]) // 2, (CELL_SIZE[1] - COIN_SIZE[1]) // 2
        pygame.draw.line(screen, Color('blue'),
                         (top[0] + coin_offs[0], top[1] + coin_offs[1]),
                         (top[0] + CELL_SIZE[0] - coin_offs[0], top[1] + CELL_SIZE[1] - coin_offs[1]), 5)
        pygame.draw.line(screen, Color('blue'),
                         (top[0] + CELL_SIZE[0] - coin_offs[0], top[1] + coin_offs[1]),
                         (top[0] + coin_offs[0], top[1] + CELL_SIZE[1] - coin_offs[1]), 5)
    else:
        raise Exception()


def victory(player):
    return all(board[i][i] == player for i in range(3)) \
           or all(board[i][2 - i] == player for i in range(3)) \
           or any(all(board[i][j] == player for i in range(3)) for j in range(3))


board = [[None] * 3 for _ in range(3)]
current = 0
done = False
v = -1
draw_board()
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
            break
        if evt.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]:
            if v != -1:
                continue
            x, y = pygame.mouse.get_pos()
            if x not in range(offsets[0], SIZE[0] - offsets[0]) or y not in range(offsets[1], SIZE[1] - offsets[0]):
                continue

            x, y = (x - offsets[0]) // CELL_SIZE[0], (y - offsets[1]) // CELL_SIZE[1]
            if board[x][y] is not None:
                continue
            board[x][y] = current
            draw_coin(current, x, y)

            if victory(current):
                v = 1
            current = (current + 1) % 2
    if v != -1:
        pygame.display.set_caption(f'Player {v + 1} won!')
    elif all(None not in board[i] for i in range(3)):
        pygame.display.set_caption(f'Draw')
    else:
        pygame.display.set_caption(f'Player {current + 1} can play...')
    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
