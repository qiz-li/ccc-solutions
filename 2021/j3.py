"""
CCC '21 J3 - Secret Instructions
Find this problem at:
https://dmoj.ca/problem/ccc21j3
"""

step = input()
prev = ''
while step != '99999':
    direction, steps = sum(map(int, step[:2])), int(step[2:])
    if direction == 0:
        print(prev, end=' ')
    elif direction % 2:
        prev = "left"
        print(prev, end=' ')
    else:
        prev = "right"
        print(prev, end=' ')
    print(steps)
    step = input()
