import sys
input = sys.stdin.readline

r, c = int(input()), int(input())
yard = [list(input().strip()) for _ in range(r)]
n_yard = [i[::] for i in yard]

moves = [input().strip() for _ in range(int(input()))]
dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

move_cords = [set() for _ in range(4)]
last = [0 for _ in range(4)]

# Find the relative coordinates for all moves in each direction
dir = y = x = 0
for move in moves:
    dir %= 4
    if move == 'F':
        y, x = y + dirs[dir][0], x + dirs[dir][1]
        for i, cord in enumerate(((y, x), (x, -y), (-y, -x),  (-x, y))):
            move_cords[i].add(cord)
    elif move == 'L':
        dir -= 1
    elif move == 'R':
        dir += 1
# Find the relative coordinates of the last move in each direction.
# This is needed to later mark the square with '*'.
for i, cord in enumerate(((y, x), (x, -y), (-y, -x),  (-x, y))):
    last[i] = cord


def out(y, x):
    return y < 0 or y >= r or x < 0 or x >= c


for y in range(r):
    for x in range(c):
        if yard[y][x] == '.':
            for dir in range(0, 4):
                ly, lx = y + last[dir][0], x + last[dir][1]
                if not out(ly, lx):
                    for ny, nx in move_cords[dir]:
                        cy, cx = y + ny, x + nx
                        if out(cy, cx) or yard[cy][cx] == 'X':
                            break
                    else:
                        n_yard[ly][lx] = '*'

for row in n_yard:
    print(''.join(row))
