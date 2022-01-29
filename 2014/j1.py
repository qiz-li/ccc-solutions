"""
CCC '14 J1 - Triangle Times
Find this problem at:
https://dmoj.ca/problem/ccc14j1
"""

ts = tuple(map(int, (input() for _ in range(3))))
sts = sum(ts)


if all(0 for t in ts if t != 60):
    print("Equilateral")
elif sts == 180:
    if ts[0] in ts[1:] or ts[2] in ts[:2]:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
