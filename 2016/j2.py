"""
CCC '16 J2 - Magic Squares
Find this problem at:
https://dmoj.ca/problem/ccc16j2
"""

grid = []
for _ in range(4):
    grid.append(list(map(int, input().split())))

l_sum = sum(grid[0])
for line in grid[1:] + list(zip(*grid)):
    if sum(line) != l_sum:
        print("not magic")
        break
else:
    print("magic")
