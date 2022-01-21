"""
CCC '00 J5/S3 - Surfing
Find this problem at:
https://dmoj.ca/problem/ccc00s3
"""

from collections import defaultdict, deque

web = defaultdict(set)
for _ in range(int(input())):
    website = input()
    line = input()
    while '</HTML>' not in line:
        if '<A HREF="' in line:
            for link in [i.split('">')[0]
                         for i in line.split('<A HREF="')][1:]:
                print(f"Link from {website} to {link}")
                web[website].add(link)
        line = input()

start = input()
while start != "The End":
    end = input()
    q = deque([start])
    visited = set()
    while q:
        curr = q.popleft()
        for next in web.get(curr, []):
            if next == end:
                print(f"Can surf from {start} to {next}.")
                break
            elif next not in visited:
                q.append(next)
                visited.add(next)
        else:
            continue
        break
    else:
        print(f"Can't surf from {start} to {end}.")
    start = input()
