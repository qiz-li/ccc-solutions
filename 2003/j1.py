"""
CCC '03 J1 - Trident
Find this problem at:
https://dmoj.ca/problem/ccc03j1
"""

tine, spacing, handle = int(input()), int(input()), int(input())

for _ in range(tine):
    for i in range(2):
        print('*', end='')
        print(' ' * spacing, end='')
    print('*')

width = spacing * 2 + 3
print('*' * width)

for _ in range(handle):
    print(' ' * (width // 2) + '*')
