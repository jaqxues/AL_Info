import re

ROWS = 'ABC'
COLUMNS = '123'


def print_board(b):
    for row in ROWS:
        print('     |     |     ')
        for column in COLUMNS:
            print(
                f"  {b[row + column] if row + column in b else ' '} ",
                f"{'|' if COLUMNS.find(column) != len(COLUMNS) - 1 else ''}",
                end='')
        print('\n     |     |     ')
        if ROWS.find(row) != len(ROWS) - 1:
            print('-----+-----+-----')


def victory(b: dict, p: str):
    fields = [[], []]
    for x in range(3):
        fields[0].append(ROWS[x] + COLUMNS[x])
        fields[1].append(ROWS[x] + COLUMNS[2 - x])
    for x in range(3):
        fields.append([ROWS[x] + COLUMNS[y] for y in range(3)])
        fields.append([ROWS[y] + COLUMNS[x] for y in range(3)])
    for aligned_fields in fields:
        for field in aligned_fields:
            if field not in b or b[field] != p:
                break
        else:
            return True
    return False


def is_finished(_board):
    for row in ROWS:
        for col in COLUMNS:
            if row + col not in _board:
                return False
    return True


player = 'O'
board = {}
field_regex = re.compile('[A-C][1-3]')

while not victory(board, player):
    if is_finished(board):
        print('Stopping')
        break

    def swap_player():
        global player
        player = 'X' if player == 'O' else 'O'
    swap_player()

    # Field name as identifier in board
    field = input(f"Player {str(1 if player == 'X' else 2)}: ").upper()

    if field not in board and field_regex.match(field):
        board[field] = player
    else:
        print('Invalid Field')
        # Player gets changed every iteration. Swapping twice to allow retry
        swap_player()
    print_board(board)
else:
    print('Player', player, 'won')
