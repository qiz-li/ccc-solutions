"""
CCC '08 J5/S5 - Nukit
Find this problem at:
https://dmoj.ca/problem/ccc08s5
"""

rules = [[2, 1, 0, 2], [1, 1, 1, 1], [0, 0, 2, 1], [0, 3, 0, 0], [1, 0, 0, 1]]
memoize = {}


def get_new_moves(cur):
    new_moves = []
    for rule in rules:
        new = cur[::]
        for i in range(4):
            new[i] -= rule[i]
            if new[i] < 0:
                break
        else:
            new_moves.append(new)
    return new_moves


def a_moves(cur):
    key = 'a' + ''.join(map(str, cur))
    if key not in memoize:
        new_moves = get_new_moves(cur)
        # All moves player A can needs to lead to a win for player B
        memoize[key] = not new_moves or all(
            b_moves(move) for move in new_moves)
    return memoize[key]


def b_moves(cur):
    key = 'b' + ''.join(map(str, cur))
    if key not in memoize:
        new_moves = get_new_moves(cur)
        # Player B only needs to have one move that wins
        memoize[key] = new_moves and any(
            a_moves(move) for move in new_moves)
    return memoize[key]


for _ in range(int(input())):
    memoize = {}
    # Check wether player B will win
    if a_moves(list(map(int, input().split()))):
        print("Roland")
    else:
        print("Patrick")
