"""
CCC '04 J5 - Fractals
Find this problem at:
https://dmoj.ca/problem/ccc04j5
"""

level, width, check = map(int, input().split())
fractals = [(0, width, 1, 1, 1)]

for _ in range(level):
    nfs = []
    for fractal in fractals:
        sx, ex, sy, ey, dir = fractal
        # Line is horizontal
        if sy == ey:
            # Get new width
            nw = abs(sx - ex) // 3
            # Map out new X lines
            nfs.append((sx, sx + nw, sy, ey, dir))
            nfs.append((ex - nw, ex, sy, ey, dir))
            nfs.append((sx + nw, ex - nw, sy +
                        dir * nw, sy + dir * nw, dir))
            # Map out new Y lines
            nsy, ney = sorted((sy + dir * nw, ey))
            nfs.append((sx + nw, sx + nw, nsy, ney, -1))
            nfs.append((ex - nw, ex - nw, nsy, ney, 1))
        # Line is vertical
        else:
            # Get new width
            nw = abs(sy - ey) // 3
            # Map out new Y lines
            nfs.append((sx, ex, sy, sy + nw, dir))
            nfs.append((sx, ex, ey - nw, ey, dir))
            nfs.append((sx + dir * nw, sx + dir * nw,
                        sy + nw, ey - nw, dir))
            # Map out new X lines
            nsx, nex = sorted((sx + dir * nw, ex))
            nfs.append((nsx, nex, sy + nw, sy + nw, - 1))
            nfs.append((nsx, nex, ey - nw, ey - nw, 1))
    fractals = nfs[::]

answers = set()
for fractal in fractals:
    sx, ex, sy, ey, _ = fractal
    if sx <= check <= ex:
        for y in range(sy, ey + 1):
            answers.add(y)
print(*sorted(answers))
