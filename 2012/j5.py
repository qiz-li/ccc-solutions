"""
CCC '12 J5 - A Coin Game
Find this problem at:
https://dmoj.ca/problem/ccc12s4
"""

# NOTE: This solution is intended only for the J5 where n < 5.
# Code runs but becomes quite slow after n > 5. It will TLE.
# See j5.cpp for S4 solution (n < 8).

import sys


def generate_key(pos):
    key = ''
    for i in pos:
        key += ''.join(map(str, i))
        key += '-'
    return key[:-1]


def solve(n):
    pos = [[int(i)] for i in sys.stdin.readline().split()]
    visited = set()
    target = generate_key([[i] for i in range(1, n + 1)])
    q = [(pos, 0)]

    while q:
        pos, step = q.pop(0)
        key = generate_key(pos)
        if key == target:
            return step
        elif key not in visited:
            visited.add(key)
            for idx in range(n):
                if idx != n - 1:
                    if (pos[idx] and (not pos[idx + 1] or
                                      pos[idx + 1][-1] > pos[idx][-1])):
                        n_pos = [i[::] for i in pos]
                        n_pos[idx + 1].append(n_pos[idx].pop())
                        q.append((n_pos, step + 1))
                if idx != 0:
                    if (pos[idx] and (not pos[idx - 1] or
                                      pos[idx - 1][-1] > pos[idx][-1])):
                        n_pos = [i[::] for i in pos]
                        n_pos[idx - 1].append(n_pos[idx].pop())
                        q.append((n_pos, step + 1))

    return "IMPOSSIBLE"


n = int(sys.stdin.readline())
while n != 0:
    print(solve(n))
    n = int(sys.stdin.readline())
