"""
CCC '10 J5 - Knight Hop
Find this problem at:
https://dmoj.ca/problem/ccc10j5
"""

initial = tuple(map(int, input().split()))
end = tuple(map(int, input().split()))


def in_board(num):
    """
    Check if a number is in the board.

    Args:
        num = Number to check.
    """
    return num >= 1 and num <= 8


def new_moves(x, y):
    """
    Given a knight's initial position, return a list of possible moves.

    Args:
        x = Initial X-coordinate of the knight.
        y = Initial Y-coordinate of the knight.

    Returns:
        A list of possible new coordinates to move to.
    """
    moves = []
    for nx in range(x - 2, x + 3):
        if in_board(nx):
            if nx == x - 2 or nx == x + 2:
                if in_board(y + 1):
                    moves.append((nx, y + 1))
                if in_board(y - 1):
                    moves.append((nx, y - 1))
            if nx == x - 1 or nx == x + 1:
                if in_board(y + 2):
                    moves.append((nx, y + 2))
                if in_board(y - 2):
                    moves.append((nx, y - 2))
    return moves


# BFS to find the shortest path
q = [(initial, 1)]
visited = set()
while q:
    cur, step = q.pop(0)
    for new in new_moves(*cur):
        if new == end:
            print(step)
            break
        elif new not in visited:
            q.append((new, step + 1))
            visited.add(new)
    else:
        continue
    break
