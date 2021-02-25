"""
CCC '17 J1 - Quadrant Selection
Find this problem at:
https://dmoj.ca/problem/ccc17j1
"""

x, y = int(input()), int(input())
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4)
