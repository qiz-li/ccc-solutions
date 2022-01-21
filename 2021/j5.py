"""
CCC '20 J5/S2 - Modern Art
Find this problem at:
https://dmoj.ca/problem/ccc21s2
"""

m, n = int(input()), int(input())
ms, ns = set(), set()

for _ in range(int(input())):
    t, num = input().split()
    if t == "R":
        if num in ms:
            ms.remove(num)
        else:
            ms.add(num)
    elif t == "C":
        if num in ns:
            ns.remove(num)
        else:
            ns.add(num)

print(len(ms) * (n - len(ns)) + len(ns) * (m - len(ms)))
