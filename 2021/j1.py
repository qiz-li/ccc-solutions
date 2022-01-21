"""
CCC '21 J1 - Boiling Water
Find this problem at:
https://dmoj.ca/problem/ccc21j1
"""

temp = int(input())
print(5 * temp - 400)
if temp < 100:
    print(1)
elif temp > 100:
    print(-1)
else:
    print(0)
