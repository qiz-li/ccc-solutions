"""
CCC '13 J5/S3 - Chances of Wining
Find this problem at:
https://dmoj.ca/problem/ccc13s3
"""

t = int(input())
played = [set() for _ in range(5)]
points = [0 for _ in range(5)]

for _ in range(int(input())):
    a, b, sa, sb = map(int, input().split())
    played[a].add(b)
    played[b].add(a)
    if sa > sb:
        points[a] += 3
    elif sb > sa:
        points[b] += 3
    else:
        points[a] += 1
        points[b] += 1


def play_games(played, points, start_i):
    total = 0
    for i in range(start_i, 5):
        for j in range(1, 5):
            # Teams have not played each other
            if j not in played[i] and j != i:
                # Record that teams played each other
                played[j].add(i)
                played[i].add(j)
                # Team A won three points
                total += play_games(
                    [ts.copy() for ts in played],
                    points[:i] + [points[i] + 3] + points[i + 1:], i)
                # Team B won three points
                total += play_games(
                    [ts.copy() for ts in played],
                    points[:j] + [points[j] + 3] + points[j + 1:], i)
                # Both teams won one point
                points[i] += 1
                points[j] += 1
    # Our team is the top team
    if all(points[i] < points[t] for i in range(1, 5) if i != t):
        total += 1

    return total


print(play_games(played, points, 1))
