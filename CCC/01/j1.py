"""
CCC '01 J1 - Dressing Up
Find this problem at:
https://dmoj.ca/problem/ccc01j1
"""

height = int(input())
# These are the two parts of the bow tie
for half in (range(1, height, 2), range(height, -1, -2)):
    # Print each line accordingly
    for i in half:
        print('*' * i + ' ' * ((height-i)*2) + '*' * i)
