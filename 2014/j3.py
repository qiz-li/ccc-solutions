"""
CCC '14 J3 - Double Dice
Find this problem at:
https://dmoj.ca/problem/ccc14j3
"""

p1 = p2 = 100
for _ in range(int(input())):
    d1, d2 = map(int, input().split())
    if d1 > d2:
        p2 -= d1
    elif d2 > d1:
        p1 -= d2

print(p1)
print(p2)
