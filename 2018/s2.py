"""
CCC '18 S2 - Sunflowers
Find this problem at:
https://dmoj.ca/problem/ccc18s2
"""


def rotate_90(grid):
    """
    Rotate a given grid by 90 degrees.

    Args:
        grid: Grid to rotate.

    Returns:
        Grid after being rotated by 90 degrees.
    """
    new_grid = []
    for col, _ in enumerate(grid):
        new_row = []
        # Go through the rows,
        # and form new rows depending on the flower's column.
        for row in grid:
            new_row.append(row[col])
        new_grid.append(new_row)
    return new_grid[::-1]


grid = []
# Make a grid from inputs
for _ in range(int(input())):
    grid.append([int(i) for i in input().split()])

while True:
    # Checking each column
    for day, flowers in enumerate(grid):
        # Checking each row
        for idx, flower in enumerate(flowers):
            try:
                # Break if flower is bigger than next flower
                if flower >= flowers[idx + 1]:
                    break
            except IndexError:
                pass
            try:
                # Break if flower is bigger than flower below it
                if flower >= grid[day + 1][idx]:
                    break
            except IndexError:
                pass
        else:
            continue
        break
    else:
        break
    # Continue rotating grid until valid arrangement
    grid = rotate_90(grid)

# Print out flowers
for day in grid:
    print(' '.join(map(str, day)))
