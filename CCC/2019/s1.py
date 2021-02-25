"""
CCC '19 S1 - Flipper
Find this problem at:
https://dmoj.ca/problem/ccc19s1
"""

grid = [[1, 2], [3, 4]]

for action in input():
    # Move the top to the bottom
    if action == "H":
        grid.append(grid.pop(0))
    # Move the first char to the end
    elif action == "V":
        grid[1].append(grid[1].pop(0))
        grid[0].append(grid[0].pop(0))
for i in grid:
    print(i[0], i[1])
