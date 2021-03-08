import pygame
import sys
from pygame.locals import *

BOARD_SIZE = 7, 6
GAME_SIZE = 420, 360
UI_CTL_SIZE = GAME_SIZE[0], 60
SIZE = GAME_SIZE[0], GAME_SIZE[1] + UI_CTL_SIZE[1]
FPS = 30


def draw_coin(s, i, j, c):
    offset = 5
    diameter = 50
    color = {
        0: Color('yellow'),
        1: Color('red'),
        2: Color('gray')
    }[c]
    pygame.draw.circle(s, color, (int((GAME_SIZE[0] / BOARD_SIZE[0]) * i) + diameter // 2 + offset,
                                  int((GAME_SIZE[1] / BOARD_SIZE[1]) * j) + diameter // 2 + offset), diameter // 2)


def draw_board(s):
    pygame.draw.rect(s, Color('blue'), (0, 0, GAME_SIZE[0], GAME_SIZE[1]))
    for i in range(BOARD_SIZE[0]):
        for j in range(BOARD_SIZE[1]):
            draw_coin(s, i, j, 2)
    pygame.draw.rect(s, Color('white'), (0, GAME_SIZE[1], SIZE[0], SIZE[1]))
    pygame.draw.rect(s, Color('green'), (30, GAME_SIZE[1] + 10, 120, 30))
    pygame.draw.rect(s, Color('pink'), (SIZE[0] // 2 + 30, GAME_SIZE[1] + 10, 120, 30))


def victory(player):
    # Vertical
    for i in range(BOARD_SIZE[0]):
        for pj in range(BOARD_SIZE[1] - 3):
            if all(board[i][j + pj] == player for j in range(4)):
                return True
    # Horizontal
    for j in range(BOARD_SIZE[1]):
        for pi in range(BOARD_SIZE[0] - 3):
            if all(board[i + pi][j] == player for i in range(4)):
                return True

    # Diagonals
    for pi in range(BOARD_SIZE[0] - 3):
        for pj in range(BOARD_SIZE[1] - 3):
            if all(board[i + pi][i + pj] == player for i in range(4)):
                return True
            if all(board[3 - i + pi][3 - i + pj] == player for i in range(4)):
                return True
    return False


pygame.init()
screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
board = [[None] * BOARD_SIZE[1] for _ in range(BOARD_SIZE[0])]
draw_board(screen)
current = 0
v = -1
actions = []


def update_played():
    global current, v
    if victory(current):
        v = current
    else:
        v = -1
    current = (current + 1) % 2


done = False
while not done:
    for evt in pygame.event.get():
        if evt.type == QUIT:
            done = True
            break
        if evt.type == MOUSEBUTTONDOWN and pygame.mouse.get_pressed(3)[0]:
            x, y = pygame.mouse.get_pos()
            if y > GAME_SIZE[1]:
                # Pressed Green Button
                if Rect(30, GAME_SIZE[1] + 10, 120, 30).collidepoint(x, y):
                    board = [[None] * BOARD_SIZE[1] for _ in range(BOARD_SIZE[0])]
                    current = 0
                    v = -1
                    actions = []
                    draw_board(screen)
                if Rect(SIZE[0] // 2 + 30, GAME_SIZE[1] + 10, 120, 30).collidepoint(x, y):
                    if actions:
                        i, j = actions.pop()
                        board[i][j] = None
                        draw_coin(screen, i, j, 2)
                        update_played()
                break

            if v >= 0:
                break
            i = x // (GAME_SIZE[0] // BOARD_SIZE[0])
            for j in range(len(board[i]) - 1, -1, -1):
                if board[i][j] is None:
                    board[i][j] = current
                    draw_coin(screen, i, j, current)
                    actions.append((i, j))
                    update_played()
                    if all(board[i][j] is not None for i in range(BOARD_SIZE[0]) for j in range(BOARD_SIZE[1])):
                        v = -2
                    break
            else:
                # No place found in row, not doing anything
                pass

    if v >= 0:
        pygame.display.set_caption(f'Player {v + 1} won!')
    elif v == -1:
        pygame.display.set_caption(f'Player {current + 1} can play...')
    elif v == -2:
        pygame.display.set_caption('Draw')

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
sys.exit()
