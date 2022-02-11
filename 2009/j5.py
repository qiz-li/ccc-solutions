"""
CCC '09 J5/S3 - Degrees Of Separation
Find this problem at:
https://dmoj.ca/problem/ccc09s3
"""

# Initial graph connections
network = [set(), {6}, {6}, {4, 5, 6, 15}, {3, 5, 6}, {3, 4, 6},
           {1, 2, 3, 4, 5, 7}, {6, 8}, {7, 9}, {8, 10, 12}, {9, 11},
           {10, 12}, {9, 11, 13}, {12, 14, 15}, {13}, {3, 13}, {17, 18},
           {16, 18}, {16, 17}, set(), set(), set(), set(), set(), set(),
           set(), set(), set(), set(), set(), set(), set(), set(), set(),
           set(), set(), set(), set(), set(), set(), set(), set(), set(),
           set(), set(), set(), set(), set(), set(), set(), set()]

cmd = input()
while cmd != 'q':
    x = int(input())

    if cmd == 'i':
        y = int(input())
        network[x].add(y)
        network[y].add(x)

    elif cmd == 'd':
        y = int(input())
        network[x].remove(y)
        network[y].remove(x)

    elif cmd == 'n':
        print(len(network[x]))

    elif cmd == 'f':
        total = set()
        for friend in network[x]:
            total = total.union(network[friend])
        # Remove any immediate friends
        for friend in network[x]:
            if friend in total:
                total.remove(friend)
        # Remove self
        if x in total:
            total.remove(x)
        print(len(total))

    elif cmd == 's':
        y = int(input())
        # BFS to find shortest path
        q = [(x, 1)]
        visited = set()
        while q:
            cur, step = q.pop(0)
            for friend in network[cur]:
                if friend == y:
                    print(step)
                    break
                if friend not in visited:
                    visited.add(friend)
                    q.append((friend, step + 1))
            else:
                continue
            break
        else:
            print("Not connected")

    cmd = input()
