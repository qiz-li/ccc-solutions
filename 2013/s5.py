"""
CCC '13 S5 - Factor Solitaire
Find this problem at:
https://dmoj.ca/problem/ccc13s5
"""

n = int(input())
pts = 0

while n != 1:
    for a in range(n // 2, 0, -1):
        if (n - a) % a == 0:
            n -= a
            pts += n // a
            break
print(pts)
