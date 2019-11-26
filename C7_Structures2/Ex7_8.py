ROWS = 'ABC'
COLUMNS = '123'


def print_board(b):
    for row in ROWS:
        print("     |     |     ")
        for column in COLUMNS:
            print(
                f"  {b[row + column] if row + column in b else ' '}  {'|' if COLUMNS.find(column) != len(COLUMNS) - 1 else ''}",
                end="")
        print("\n     |     |     ")
        if ROWS.find(row) != len(ROWS) - 1:
            print("-----+-----+-----")


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


player = "O"
board = {}
while not victory(board, player):
    player = "X" if player == "O" else "O"
    board[input(f"Player {str(1 if player == 'X' else 2)}: ")] = player
    print_board(board)
