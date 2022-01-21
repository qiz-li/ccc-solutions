"""
CCC '21 J5/S2 - Escape Room
Find this problem at:
https://dmoj.ca/problem/ccc20s2
"""

# !Note this solution TLE on the last test batch.
# The issue can likely be solved by using a large pre-filled
# visited array instead of the current visited set.
# Refer to j5.cpp for final solution.

import sys

room = []
products = {}
x, y = int(sys.stdin.readline()), int(sys.stdin.readline())

for row in range(1, x + 1):
    new_row = []
    col = 0
    for val in map(int, sys.stdin.readline().split()):
        col += 1
        new_row.append(val)
        product = row * col
        if product in products:
            products[product].append((row - 1, col - 1))
        else:
            products[product] = [(row - 1, col - 1)]
    room.append(new_row)

visited = set()
queue = [(0, 0)]

while queue:
    curr = queue.pop(0)
    product = room[curr[0]][curr[1]]
    for next in products.get(product, []):
        if next == (x - 1, y - 1):
            print("yes")
            break
        if next not in visited:
            visited.add(next)
            queue.append(next)
    else:
        continue
    break
else:
    print("no")
