"""
CCC '12 J3 - Icon Scaling
Find this problem at:
https://dmoj.ca/problem/ccc12j3
"""

scale = int(input())
for line in ('*x*', ' xx', '* *'):
    for _ in range(scale):
        for char in line:
            print(char * scale, end='')
        print()
