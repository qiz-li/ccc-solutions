"""
CCC '11 J5 - Unfriend
Find this problem at:
https://dmoj.ca/problem/ccc11j5
"""

n = int(input())

# Put nodes into adjacency list
adjacent = [[] for _ in range(n + 1)]
for i in range(n - 1):
    adjacent[int(input())].append(i + 1)

subset = set()
all_sub = []


def subsets(k):
    """
    Generate all subsets from k to n-1

    Args:
        k = Start of subset
    """
    if k == n:
        all_sub.append(subset.copy())
    else:
        subset.add(k)
        subsets(k + 1)
        subset.remove(k)
        subsets(k + 1)


subsets(1)
count = 0
for subset in all_sub:
    for friend in range(1, n):
        # Only count subsets who include
        # the parent node (friend to be removed)
        # and all its children (invitees of that friend)
        if (friend in subset and
                not all(invitee in subset for invitee in adjacent[friend])):
            break
    else:
        count += 1

print(count)
