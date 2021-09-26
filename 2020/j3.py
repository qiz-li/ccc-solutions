"""
CCC '20 J3 - Art
Find this problem at:
https://dmoj.ca/problem/ccc20j3
"""

# Unzip the input into separate lists of x & y coordinates
xs, ys = [], []
for i in range(int(input())):
    x, y = map(int, input().split(','))
    xs.append(x)
    ys.append(y)

# The smallest x & y coordinates and minus one (because of frame)
print(f'{min(xs)-1},{min(ys)-1}')
# The largest x & y coordinates and plus one (because of frame)
print(f'{max(xs)+1},{max(ys)+1}')
