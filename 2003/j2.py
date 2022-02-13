"""
CCC '03 J2 - Picture Perfect
Find this problem at:
https://dmoj.ca/problem/ccc03j2
"""

from math import sqrt

photos = int(input())
while photos > 0:
    for i in range(int(sqrt(photos)), 0, -1):
        if photos % i == 0:
            dimensions = (i, photos // i)
            print(f"Minimum perimeter is {sum(dimensions) * 2}"
                  f" with dimensions {dimensions[0]} x {dimensions[1]}")
            break
    photos = int(input())
