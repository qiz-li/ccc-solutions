"""
CCC '07 J5 - Keep on Truckin'
Find this problem at:
https://dmoj.ca/problem/ccc07j5
"""

d_min, d_max = int(input()), int(input())
motels = [0, 990, 1010, 1970, 2030, 2940, 3060,
          3930, 4060, 4970, 5030, 5990, 6010, 7000]
for _ in range(int(input())):
    motels.append(int(input()))
memoize = {}


def drive(start):
    if start == 7000:
        return 1
    if start not in memoize:
        total = 0
        for motel in motels:
            # Total possibly routes will be all routes from
            # all motels that can be reached from this motel
            if start + d_min <= motel <= start + d_max:
                total += drive(motel)
        memoize[start] = total
    return memoize[start]


print(drive(0))
