"""
CCC '17 J2 - Shifty Sum
Find this problem at:
https://dmoj.ca/problem/ccc17j2
"""

num = total = int(input())
for i in range(int(input())):
    total += num * 10 ** (i+1)
print(total)
