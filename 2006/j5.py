"""
CCC '06 J5 - CCC Othello
Find this problem at:
https://dmoj.ca/problem/ccc06j5
"""

raw = input().split()
choice = raw.pop(0)
board = [[-1 for _ in range(9)] for _ in range(9)]

# Initial board configurations
if choice == 'a':
    board[4][4] = 1
    board[5][5] = 1
    board[4][5] = 0
    board[5][4] = 0
elif choice == 'b':
    for i in range(1, 9):
        board[9 - i][i] = 1
    for i in range(1, 9):
        board[i][i] = 0
elif choice == 'c':
    for i in range(1, 9):
        board[i][5] = 1
        board[i][6] = 1
    for i in range(1, 9):
        board[i][3] = 0
        board[i][4] = 0

player = 0
for _ in range(int(raw.pop(0))):
    r, c = int(raw.pop(0)), int(raw.pop(0))
    board[r][c] = player

    to_check = []

    # Generate check path for up & down
    for i in (list(range(r + 1, 9)), list(range(r - 1, 0, -1))):
        to_check.append(list(zip(i, [c] * len(i))))

    # Generate check path for left & right
    for i in (list(range(c - 1, 0, -1)), list(range(c + 1, 9))):
        to_check.append(list(zip([r] * len(i), i)))

    # Generate check path for diagonals
    for cs in (range(c + 1, 9), range(c - 1, 0, -1)):
        for change in (1, -1):
            new = []
            nr = r + change
            for nc in cs:
                if 1 > nr or nr > 8 or 1 > nc or nc > 8:
                    break
                new.append((nr, nc))
                nr += change
            to_check.append(new)

    # Check in all directions
    for check in to_check:
        n_board = [row[::] for row in board]
        for nr, nc in check:
            if board[nr][nc] == -1:
                break
            elif board[nr][nc] == player:
                board = [row[::] for row in n_board]
                break
            else:
                n_board[nr][nc] = player

    player = 0 if player else 1

b_count = w_count = 0
for row in board:
    b_count += row.count(0)
    w_count += row.count(1)

print(b_count, w_count)
