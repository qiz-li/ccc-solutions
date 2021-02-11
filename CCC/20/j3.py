'''
CCC '20 J3 - Art
Find this problem at:
https://dmoj.ca/problem/ccc20j3
'''

# Unzip the input into separate lists of x & y coordinates
x, y = list(zip(*[map(int, input().split(',')) for i in range(int(input()))]))

# The smallest x & y coordinates and minus one (because of frame)
print(f'{min(x)-1},{min(y)-1}')
# The largest x & y coordinates and plus one (because of frame)
print(f'{max(x)+1},{max(y)+1}')
