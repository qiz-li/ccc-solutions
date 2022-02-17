"""
CCC '22 J5 - Square Pool
(Cannot) Find this problem (yet).
"""

# Was so close to the solution on the contest! :(

n = int(input())
trees = []
for _ in range(int(input())):
    trees.append(tuple(map(int, input().split())))
# Pretend the edges are trees
trees += [(0, 0), (n + 1, n + 1)]

# Read all segments of trees to other trees for x and y axis
all_x,  all_y = set(), set()
for x, y in trees:
    for x2, y2 in trees:
        if x != x2:
            all_x.add(tuple(sorted((x, x2))))
        if y != y2:
            all_y.add(tuple(sorted((y, y2))))


def sort_by_abs(cords):
    return list(sorted(cords, key=lambda cord: abs(
        cord[0] - cord[1]), reverse=True))


trees = trees[:-2]
# Sort by the distance between the two trees
all_x, all_y = sort_by_abs(all_x), sort_by_abs(all_y)

total = []
for i in range(2):
    # Sort trees by top to bottom/left to right
    trees = sorted(trees, key=lambda x: x[i])
    # Test the square of the distance between the two trees.
    # If there is a tree in the square move the square to
    # the bottom/right of the tree.
    for s, e in all_x if i else all_y:
        s2, e2 = 0, abs(s - e)
        for tree in trees:
            if i and s < tree[0] < e and s2 < tree[1] < e2:
                e2 += abs(tree[1] - s2) + 1
                s2 = tree[1] + 1
            elif not i and s < tree[1] < e and s2 < tree[0] < e2:
                e2 += abs(tree[0] - s2) + 1
                s2 = tree[0] + 1
            # Square went out of bounds, is not valid
            if e2 > n + 1:
                break
        else:
            total.append(abs(s - e) - 1)
            break

print(max(total))
