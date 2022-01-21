"""
CCC '01 J5/S3 - Strategic Bombing
Find this problem at:
https://dmoj.ca/problem/ccc01s3
"""

from collections import defaultdict

roads = defaultdict(set)
while True:
    road = input()
    if road == '**':
        break
    else:
        roads[road[0]].add(road[1])
        roads[road[1]].add(road[0])


def check_connect(start, end):
    stack = ['A']
    visited = set()
    while stack:
        curr = stack.pop()
        for next in roads.get(curr, []):
            if ((curr, next) != (start, end) and
                    (curr, next) != (end, start)):
                if next == 'B':
                    return True
                elif next not in visited:
                    stack.append(next)
                    visited.add(next)
    return False


count = 0
checked = set()
for start in roads:
    for end in roads[start]:
        if ((start, end) not in checked
                and (end, start) not in checked):
            if not check_connect(start, end):
                print(f"{start}{end}")
                count += 1
            checked.add((start, end))

print(f"There are {count} disconnecting roads.")
